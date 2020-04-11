from py2neo import Graph
import csv

#Setting up connection to local graph database
graph = Graph("bolt://localhost:7687", auth=('neo4j', 'saisantosh'))

# Adding uniqueness constraints.
graph.run("CREATE CONSTRAINT ON (c:Crop) ASSERT c.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (c:state) ASSERT c.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (s:soiltype) ASSERT s.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (m:suitable_soil_ph) ASSERT m.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (p:required_equipment) ASSERT p.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (p:required_fertilizers) ASSERT p.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (p:disease_may_occur) ASSERT p.name IS UNIQUE;")
def process_crop_data(user_data):
    
    # Neo4j UNWIND query expects a list of dictionaries
    print(user_data)

    query = """
            UNWIND {rows} AS row

            MERGE (crop1:Crop {name:row.cropname})
            ON CREATE SET 
                crop1.Instate = row.Instate,
                crop1.soilcondition = row.soilcondition,
                crop1.ph = row.ph,
                crop1.equipment = row.equipment,
                crop1.fertilizers = row.fertilizers,
                crop1.diseases = row.diseases
        """

    run_neo_query(user_data,query)


def process_statewise_data(state_data):
    query = """
           UNWIND {rows} AS row
           MERGE (crop:Crop {name:row.cropname})
           MERGE (state1:state {name:row.Instate})
           MERGE (crop)-[:MAJORLY_GROWN_IN]->(state1)
       """
    run_neo_query(state_data,query)


def process_soil_type_data(soil_data):
    query = """
            UNWIND {rows} AS row
            MERGE (crop:Crop {name:row.cropname})
            MERGE (sr:soiltype {name:row.soilcondition})
            MERGE (crop)-[:SUITABLE_SOIL_TYPE]->(sr)
        """
    run_neo_query(soil_data,query)



def process_ph_type_data(ph_data):
    query = """
            UNWIND {rows} AS row
            MERGE (crop:Crop {name:row.cropname})
            MERGE (sr:suitable_soil_ph {name:row.ph})
            MERGE (crop)-[:SUITABLE_SOIL_PH]->(sr)
        """
    run_neo_query(ph_data,query)
    
    
def process_equipment_type_data(equipment_data):
    query = """
            UNWIND {rows} AS row
            MERGE (crop:Crop {name:row.cropname})
            MERGE (sr:required_equipment {name:row.equipment})
            MERGE (crop)-[:EQUIPMENT_REQUIRED]->(sr)
        """
    run_neo_query(equipment_data,query)
    
def process_fertilizer_type_data(fertilizers_data):

    query = """
            UNWIND {rows} AS row
            MERGE (crop:Crop {name:row.cropname})
            MERGE (sr:required_fertilizers {name:row.fertilizers})
            MERGE (crop)-[:FERTILIZERS_REQUIRED]->(sr)
        """
    run_neo_query(fertilizers_data,query)
def process_disease_type_data(diseases_data):

    query = """
            UNWIND {rows} AS row
            MERGE (crop:Crop {name:row.cropname})
            MERGE (sr:disease_may_occur {name:row.diseases})
            MERGE (crop)-[:DISEASES_MAY_OCCUR]->(sr)
        """
    run_neo_query(diseases_data,query)


def run_neo_query(data, query):
        graph.run(query, rows=data)

if __name__== "__main__":
    l=[]
    with open('survey_results_public_agri.csv') as csv_file:
    	csv_reader=csv.reader(csv_file,delimiter=',')
    	line_count=0
    	for row in csv_reader:
    		if line_count==0:
    			print("the attributes section")
    		else:
    			this_dict={}
    			this_dict["cropname"]=row[0]
    			this_dict["Instate"]=row[1]
    			this_dict["attemp"]=row[2]
    			this_dict["soilcondition"]=row[3]
    			this_dict["ph"]=row[4]
    			this_dict["weather"]=row[5]
    			this_dict["equipment"]=row[6]
    			this_dict["fertilizers"]=row[7]
    			this_dict["diseases"]=row[8]
    			l.append(this_dict)
    		line_count+=1
    	# print(l)
    	process_crop_data(l)
    l=[]
    with open('survey_results_public_agri.csv') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        line_count=0
        for row in csv_reader:
            if line_count==0:
                print("the attributes section")
            else:
                this_dict={}
                this_dict["cropname"]=row[0]
                this_dict["Instate"]=row[1]
                l.append(this_dict)
            line_count+=1
        # print(l)
        process_statewise_data(l)
    l=[]
    with open('survey_results_public_agri.csv') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        line_count=0
        for row in csv_reader:
            if line_count==0:
                print("the attributes section")
            else:
                this_dict={}
                this_dict["cropname"]=row[0]
                this_dict["soilcondition"]=row[3]
                l.append(this_dict)
            line_count+=1
        # print(l)
        process_soil_type_data(l)
    l=[]
    with open('survey_results_public_agri.csv') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        line_count=0
        for row in csv_reader:
            if line_count==0:
                print("the attributes section")
            else:
                this_dict={}
                this_dict["cropname"]=row[0]
                this_dict["ph"]=row[4]
                l.append(this_dict)
            line_count+=1
        # print(l)
        process_ph_type_data(l)
    l=[]
    with open('survey_results_public_agri.csv') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        line_count=0
        for row in csv_reader:
            if line_count==0:
                print("the attributes section")
            else:
                this_dict={}
                this_dict["cropname"]=row[0]
                this_dict["equipment"]=row[6]
                l.append(this_dict)
            line_count+=1
        # print(l)
        process_equipment_type_data(l)
    l=[]
    with open('survey_results_public_agri.csv') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        line_count=0
        for row in csv_reader:
            if line_count==0:
                print("the attributes section")
            else:
                this_dict={}
                this_dict["cropname"]=row[0]
                this_dict["fertilizers"]=row[7]
                l.append(this_dict)
            line_count+=1
        # print(l)
        process_fertilizer_type_data(l)
    l=[]
    with open('survey_results_public_agri.csv') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        line_count=0
        for row in csv_reader:
            if line_count==0:
                print("the attributes section")
            else:
                this_dict={}
                this_dict["cropname"]=row[0]
                this_dict["diseases"]=row[8]
                l.append(this_dict)
            line_count+=1
        # print(l)
        process_disease_type_data(l)
