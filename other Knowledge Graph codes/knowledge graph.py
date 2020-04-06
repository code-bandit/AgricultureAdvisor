import re
import pandas as pd
import bs4
import requests
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')

from spacy.matcher import Matcher 
from spacy.tokens import Span 

import networkx as nx

import matplotlib.pyplot as plt
from tqdm import tqdm



def get_entities(sent):
  ## chunk 1
  ent1 = ""
  ent2 = ""

  prv_tok_dep = ""    # dependency tag of previous token in the sentence
  prv_tok_text = ""   # previous token in the sentence

  prefix = ""
  modifier = ""

  #############################################################
  
  for tok in nlp(sent):
    ## chunk 2
    # if token is a punctuation mark then move on to the next token
    if tok.dep_ != "punct":
      # check: token is a compound word or not
      if tok.dep_ == "compound":
        prefix = tok.text
        # if the previous word was also a 'compound' then add the current word to it
        if prv_tok_dep == "compound":
          prefix = prv_tok_text + " "+ tok.text
      
      # check: token is a modifier or not
      if tok.dep_.endswith("mod") == True:
        modifier = tok.text
        # if the previous word was also a 'compound' then add the current word to it
        if prv_tok_dep == "compound":
          modifier = prv_tok_text + " "+ tok.text
      
      ## chunk 3
      if tok.dep_.find("subj") == True:
        ent1 = modifier +" "+ prefix + " "+ tok.text
        prefix = ""
        modifier = ""
        prv_tok_dep = ""
        prv_tok_text = ""      

      ## chunk 4
      if tok.dep_.find("obj") == True:
        ent2 = modifier +" "+ prefix +" "+ tok.text
        
      ## chunk 5  
      # update variables
      prv_tok_dep = tok.dep_
      prv_tok_text = tok.text
  #############################################################

  return [ent1.strip(), ent2.strip()]




def get_relation(sent):

  doc = nlp(sent)

  # Matcher class object 
  matcher = Matcher(nlp.vocab)

  #define the pattern 
  pattern = [{'DEP':'ROOT'}, 
            {'DEP':'prep','OP':"?"},
            {'DEP':'agent','OP':"?"},  
            {'POS':'ADJ','OP':"?"}] 

  matcher.add("matching_1", None, pattern) 

  matches = matcher(doc)
  k = len(matches) - 1

  span = doc[matches[k][1]:matches[k][2]] 

  return(span.text)



pd.set_option('display.max_colwidth', 200)


candidate_sentences = pd.read_csv("agri.csv")
candidate_sentences.shape


entity_pairs = []


for i in tqdm(candidate_sentences["sentence"]):entity_pairs.append(get_entities(i))


# extract subject
source = [i[0] for i in entity_pairs]

# extract object
target = [i[1] for i in entity_pairs]


relations = [get_relation(i) for i in tqdm(candidate_sentences['sentence'])]

kg_df = pd.DataFrame({'source':source, 'target':target, 'edge':relations})

G=nx.from_pandas_edgelist(kg_df, "source", "target", edge_attr=True, create_using=nx.MultiDiGraph())

plt.figure(figsize=(12,12))

pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
#plt.show()


from py2neo import Graph
g = Graph(uri = "bolt://localhost:7687",user = "neo4j", password = "12345")

from py2neo import Node, Relationship

def run_neo_query(data, query):
    batches = get_batches(data)

    for index, batch in batches:
        print('[Batch: %s] Will add %s node to Graph' % (index, len(batch)))
        g.run(query, rows=batch)


def get_batches(lst, batch_size=100):
    return [(i, lst[i:i + batch_size]) for i in range(0, len(lst), batch_size)]

g.delete_all()

print(len(g.nodes))
print(len(g.relationships))


user_data = kg_df[['source', 'target', 'edge']]
user_data =  user_data.dropna()
user_data = list(user_data.T.to_dict().values())


query = """
            UNWIND {rows} AS row
            MERGE (object1:Object {name:row.source})
            MERGE (object2:Object {name:row.target})
            MERGE (object1)-[:REL{type:row.edge}]->(object2)
        """

run_neo_query(user_data,query)




#print(g.exists(ab))
print(len(g.nodes))
print(len(g.relationships))