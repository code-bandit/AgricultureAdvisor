from py2neo import Graph

#####################################################################
# Graph database config
#####################################################################

# Set up a link to the local graph database.
# Ideally get password from ENV variable
# graph = Graph(getenv("NEO4J_URL"), auth=(getenv("NEO4J_UID"), getenv("NEO4J_PASSWORD")))
#graph = Graph("bolt://127.0.0.1:7687", auth=('neo4j', 'neo4j'))
graph = Graph("bolt://localhost:7687", auth=('neo4j', 'saisantosh'))






query='''
	MATCH (a:Crop{name:{crop_name}})
	RETURN a.name
	'''
cursor = graph.run(query, parameters={'crop_name': 'paddy'}).evaluate()

print(cursor)

print("Getting states where the crop grown:")

query=''' MATCH(a: Crop{name:{crop_name}}) -[:MAJORLY_GROWN_IN]->(b:state)
		RETURN b.name  '''
cursor= graph.run(query, parameters={'crop_name': 'paddy'}).evaluate()
print(cursor)

print("Getting diseases that can occur:")

query=''' MATCH(a: Crop{name:{crop_name}}) -[:DISEASES_MAY_OCCUR]->(b:disease_may_occur)
		RETURN b.name  '''
cursor = graph.run(query, parameters={'crop_name': 'paddy'}).evaluate()
print(cursor)

print("Getting ph of soil that is sutibale for growing:")
query=''' MATCH(a: Crop{name:{crop_name}}) -[:SUITABLE_SOIL_PH]->(b:suitable_soil_ph)
		RETURN b.name  '''
cursor= graph.run(query, parameters={'crop_name': 'paddy'}).evaluate()
print(cursor)

print("Getting required equipments for given soil:")
query=''' MATCH(a: Crop{name:{crop_name}}) -[:EQUIPMENT_REQUIRED]->(b:required_equipment)
		RETURN b.name  '''
cursor = graph.run(query, parameters={'crop_name': 'paddy'}).evaluate()
print(cursor)

print("Getting fertilizers required:")
query=''' MATCH(a: Crop{name:{crop_name}}) -[:FERTILIZERS_REQUIRED]->(b:required_fertilizers)
		RETURN b.name  '''
cursor = graph.run(query, parameters={'crop_name': 'paddy'}).evaluate()
print(cursor)

print("Getting required soil type:")
query=''' MATCH(a: Crop{name:{crop_name}}) -[:SUITABLE_SOIL_TYPE]->(b:soiltype)
		RETURN b.name  '''
cursor = graph.run(query, parameters={'crop_name': 'paddy'}).evaluate()
print(cursor)
