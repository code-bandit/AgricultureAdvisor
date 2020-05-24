from py2neo import Graph
import csv

#Connection to graph database
graph = Graph("bolt://localhost:7687", auth=('neo4j', 'abc'))

# Adding uniqueness constraints.
graph.run("CREATE CONSTRAINT ON (c:Crop) ASSERT c.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (c:state) ASSERT c.name IS UNIQUE;")
graph.run("CREATE   CONSTRAINT ON (t:temp) ASSERT t.name IS UNIQUE;")#
graph.run("CREATE CONSTRAINT ON (s:soiltype) ASSERT s.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (w:weather) ASSERT w.name IS UNIQUE;")#
# graph.run("CREATE CONSTRAINT ON (m:suitable_soil_ph) ASSERT m.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (p:required_equipment) ASSERT p.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (p:required_fertilizers) ASSERT p.name IS UNIQUE;")
graph.run("CREATE CONSTRAINT ON (p:disease_may_occur) ASSERT p.name IS UNIQUE;")


#Neo4j query for constructing node for crops
def process_crop_data(crop_data):
    query = """
            UNWIND {rows} AS row

            MERGE (crop1:Crop {name:row.cropname})
        """

    run_neo_query(crop_data,query)

#Neo4j query for constructing node state of a state if not present and adding the relation bewteeb state annd crop
def process_statewise_data(state_data):
    query = """
           UNWIND {rows} AS row
           MERGE (crop:Crop {name:row.cropname})
           MERGE (state1:state {name:row.Instate})
           MERGE (crop)-[:MAJORLY_GROWN_IN]->(state1)
       """
    run_neo_query(state_data,query)


def process_temp_type_data(temp_data):
    query = """
           UNWIND {rows} AS row
           MERGE (crop:Crop {name:row.cropname})
           MERGE (temp1:temp {name:row.attemp})
           MERGE (crop)-[:GROWN_AT_TEMP]->(temp1)
       """
    run_neo_query(temp_data,query)

#Neo4j query for constructing node soil type and adding the relation between  crop and soil
def process_soil_type_data(soil_data):
    query = """
            UNWIND {rows} AS row
            MERGE (crop:Crop {name:row.cropname})
            MERGE (sr:soiltype {name:row.soilcondition})
            MERGE (crop)-[:SUITABLE_SOIL_TYPE]->(sr)
        """
    run_neo_query(soil_data,query)


def process_weather_type_data(weather_data):
    query = """
            UNWIND {rows} AS row
            MERGE (crop:Crop {name:row.cropname})
            MERGE (sr:weather {name:row.weather})
            MERGE (crop)-[:SUITABLE_WEATHER_TYPE]->(sr)
        """
    run_neo_query(weather_data,query)



#Neo4j query for constructing node ph and adding the relation between  ph  and crop
# def process_ph_type_data(ph_data):
#     query = """
#             UNWIND {rows} AS row
#             MERGE (crop:Crop {name:row.cropname})
#             MERGE (sr:suitable_soil_ph {name:row.ph})
#             MERGE (crop)-[:SUITABLE_SOIL_PH]->(sr)
#         """
#     run_neo_query(ph_data,query)
    
#Neo4j query for constructing node equipment and relation between  crop and equipment
    
def process_equipment_type_data(equipment_data):
    query = """
            UNWIND {rows} AS row
            MERGE (crop:Crop {name:row.cropname})
            MERGE (sr:required_equipment {name:row.equipment})
            MERGE (crop)-[:EQUIPMENT_REQUIRED]->(sr)
        """
    run_neo_query(equipment_data,query)

#Neo4j query for constructing node fertilizer and creating relation between fertilizer and crop
def process_fertilizer_type_data(fertilizers_data):

    query = """
            UNWIND {rows} AS row
            MERGE (crop:Crop {name:row.cropname})
            MERGE (sr:required_fertilizers {name:row.fertilizers})
            MERGE (crop)-[:FERTILIZERS_REQUIRED]->(sr)
        """
    run_neo_query(fertilizers_data,query)
#Neo4j query for constructing node diseases and creating relation between disease and crop
def process_disease_type_data(diseases_data):

    query = """
            UNWIND {rows} AS row
            MERGE (crop:Crop {name:row.cropname})
            MERGE (sr:disease_may_occur {name:row.diseases})
            MERGE (crop)-[:DISEASES_MAY_OCCUR]->(sr)
        """
    run_neo_query(diseases_data,query)

#running Neo4j query
def run_neo_query(data, query):
        graph.run(query, rows=data)

if __name__== "__main__":
    l=[]
    with open('test.csv') as csv_file:
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
    			# this_dict["ph"]=row[4]
    			this_dict["weather"]=row[4]
    			this_dict["equipment"]=row[5]
    			this_dict["fertilizers"]=row[6]
    			this_dict["diseases"]=row[7]
    			l.append(this_dict)
    		line_count+=1
    	# print(l)
        #sending data required for insertion into graph crop details
             
    	process_crop_data(l)
    l=[]
    with open('test.csv') as csv_file:
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
    with open('test.csv') as csv_file:
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
        # print(l)#sending data required for insertion into graph crop details
        process_soil_type_data(l)
    l=[]
    with open('test.csv') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        line_count=0
        for row in csv_reader:
            if line_count==0:
                print("the attributes section")
            else:
                this_dict={}
                this_dict["cropname"]=row[0]
                this_dict["attemp"]=row[2]
                l.append(this_dict)
            line_count+=1
        # print(l)#sending data required for insertion into graph crop details
        process_temp_type_data(l)
    l=[]
    with open('test.csv') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        line_count=0
        for row in csv_reader:
            if line_count==0:
                print("the attributes section")
            else:
                this_dict={}
                this_dict["cropname"]=row[0]
                this_dict["equipment"]=row[5]
                l.append(this_dict)
            line_count+=1
        # print(l)#sending data required for insertion into graph crop details
        process_equipment_type_data(l)
    l=[]
    with open('test.csv') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        line_count=0
        for row in csv_reader:
            if line_count==0:
                print("the attributes section")
            else:
                this_dict={}
                this_dict["cropname"]=row[0]
                this_dict["fertilizers"]=row[6]
                l.append(this_dict)
            line_count+=1
        # print(l)#sending data required for insertion into graph crop details
        process_fertilizer_type_data(l)
    l=[]
    with open('test.csv') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        line_count=0
        for row in csv_reader:
            if line_count==0:
                print("the attributes section")
            else:
                this_dict={}
                this_dict["cropname"]=row[0]
                this_dict["weather"]=row[4]
                l.append(this_dict)
            line_count+=1
        # print(l)#sending data required for insertion into graph crop details
        process_weather_type_data(l)
    l=[]
    with open('test.csv') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        line_count=0
        for row in csv_reader:
            if line_count==0:
                print("the attributes section")
            else:
                this_dict={}
                this_dict["cropname"]=row[0]
                this_dict["diseases"]=row[7]
                l.append(this_dict)
            line_count+=1
        # print(l)#sending data required for insertion into graph crop details
        process_disease_type_data(l)
