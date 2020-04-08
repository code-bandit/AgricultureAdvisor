import pandas as pd
from py2neo import Graph



graph = Graph("bolt://localhost:7687", auth=('neo4j', 'abc'))


graph.run("CREATE CONSTRAINT ON (c:Crop) ASSERT c.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (c:state) ASSERT c.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (s:soiltype) ASSERT s.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (m:suitable_soil_ph) ASSERT m.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (p:required_equipment) ASSERT p.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (p:required_fertilizers) ASSERT p.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (p:disease_may_occur) ASSERT p.name IS UNIQUE;")
def read_data():
    data = pd.read_csv(

        "./data/survey_results_public_agri.csv",
        low_memory=False)
    print("Column name of data : ", data.columns)
    return data


def process_crop_data(data):
    user_data = data[['cropname','Instate', 'soilcondition', 'ph', 'equipment', 'fertilizers', 'diseases']]
    user_data =  user_data.dropna()

    # Convert data frame to list of dictionaries
    # Neo4j UNWIND query expects a list of dictionaries
    # for bulk insertion
    user_data = list(user_data.T.to_dict().values())
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


def process_statewise_data(data):
    state_data = data[['cropname', 'Instate']]
    state_data = state_data.dropna()
    state_data = list(state_data.T.to_dict().values())

    query = """
           UNWIND {rows} AS row
           MERGE (crop:Crop {name:row.cropname})
           MERGE (state1:state {name:row.Instate})
           MERGE (crop)-[:MAJORLY_GROWN_IN]->(state1)
       """
    run_neo_query(state_data,query)


def process_soil_type_data(data):
    soil_data = data[['cropname', 'soilcondition']]
    soil_data = soil_data.dropna()
    soil_data = list(soil_data.T.to_dict().values())

    query = """
            UNWIND {rows} AS row
            MERGE (crop:Crop {name:row.cropname})
            MERGE (sr:soiltype {name:row.soilcondition})
            MERGE (crop)-[:SUITABLE_SOIL_TYPE]->(sr)
        """
    run_neo_query(soil_data,query)



def process_ph_type_data(data):
    soil_data = data[['cropname', 'ph']]
    soil_data = soil_data.dropna()
    soil_data = list(soil_data.T.to_dict().values())

    query = """
            UNWIND {rows} AS row
            MERGE (crop:Crop {name:row.cropname})
            MERGE (sr:suitable_soil_ph {name:row.ph})
            MERGE (crop)-[:SUITABLE_SOIL_PH]->(sr)
        """
    run_neo_query(soil_data,query)
    
    
def process_equipment_type_data(data):
    soil_data = data[['cropname', 'equipment']]
    soil_data = soil_data.dropna()
    soil_data = list(soil_data.T.to_dict().values())

    query = """
            UNWIND {rows} AS row
            MERGE (crop:Crop {name:row.cropname})
            MERGE (sr:required_equipment {name:row.equipment})
            MERGE (crop)-[:EQUIPMENT_REQUIRED]->(sr)
        """
    run_neo_query(soil_data,query)
    
def process_fertilizer_type_data(data):
    soil_data = data[['cropname', 'fertilizers']]
    soil_data = soil_data.dropna()
    soil_data = list(soil_data.T.to_dict().values())

    query = """
            UNWIND {rows} AS row
            MERGE (crop:Crop {name:row.cropname})
            MERGE (sr:required_fertilizers {name:row.fertilizers})
            MERGE (crop)-[:FERTILIZERS_REQUIRED]->(sr)
        """
    run_neo_query(soil_data,query)
def process_disease_type_data(data):
    soil_data = data[['cropname', 'diseases']]
    soil_data = soil_data.dropna()
    soil_data = list(soil_data.T.to_dict().values())

    query = """
            UNWIND {rows} AS row
            MERGE (crop:Crop {name:row.cropname})
            MERGE (sr:disease_may_occur {name:row.diseases})
            MERGE (crop)-[:DISEASES_MAY_OCCUR]->(sr)
        """
    run_neo_query(soil_data,query)


# def process_dev_data(data):
#     dev_data = data[['Respondent', 'DevType']]
#     dev_data = dev_data.dropna()

#     s = dev_data['DevType'].str.split(';').apply(pd.Series, 1).stack()
#     s.name = "DevType"
#     del dev_data["DevType"]
#     s = s.to_frame().reset_index()
#     dev_data = pd.merge(dev_data, s, right_on='level_0', left_index = True)

#     del dev_data["level_0"]
#     del dev_data["level_1"]
#     dev_data = list(dev_data.T.to_dict().values())

#     query = """
#            UNWIND {rows} AS row
#            MERGE (person:Person {uid:row.Respondent})
#            MERGE (work:WorkType {name:row.DevType})
#            MERGE (person)-[:WORKS_IN_INDUSTRY]->(work)
           
#        """
#     run_neo_query(dev_data,query)


def run_neo_query(data, query):
    batches = get_batches(data)

    for index, batch in batches:
        print('[Batch: %s] Will add %s node to Graph' % (index, len(batch)))
        graph.run(query, rows=batch)


def get_batches(lst, batch_size=100):
    return [(i, lst[i:i + batch_size]) for i in range(0, len(lst), batch_size)]


if __name__== "__main__":
    data = read_data()
    process_crop_data(data)
    process_statewise_data(data)
    process_soil_type_data(data)
    process_ph_type_data(data)
    process_equipment_type_data(data)
    process_fertilizer_type_data(data)
    process_disease_type_data(data)
    # process_dev_data(data)
