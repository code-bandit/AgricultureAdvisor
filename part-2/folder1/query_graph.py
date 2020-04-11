from py2neo import Graph
#connection to Neo4j
graph = Graph("bolt://localhost:7687", auth=('neo4j', 'abc'))
query='''
	MATCH (a:Crop{name:{crop_name}})
	RETURN a.name
	'''
cropname = graph.run(query, parameters={'crop_name': 'paddy'}).evaluate()

print(cropname)

print("Getting states where the crop grown:")

query=''' MATCH(a: Crop{name:{crop_name}}) -[:MAJORLY_GROWN_IN]->(b:state)
		RETURN b.name  '''
states= graph.run(query, parameters={'crop_name': 'paddy'}).evaluate()
print(states)

print("Getting diseases that can occur:")

query=''' MATCH(a: Crop{name:{crop_name}}) -[:DISEASES_MAY_OCCUR]->(b:disease_may_occur)
		RETURN b.name  '''
diseases = graph.run(query, parameters={'crop_name': 'paddy'}).evaluate()
print(diseases)

print("Getting ph of soil that is sutibale for growing:")
query=''' MATCH(a: Crop{name:{crop_name}}) -[:SUITABLE_SOIL_PH]->(b:suitable_soil_ph)
		RETURN b.name  '''
soilph= graph.run(query, parameters={'crop_name': 'paddy'}).evaluate()
print(soilph)

print("Getting required equipments for given soil:")
query=''' MATCH(a: Crop{name:{crop_name}}) -[:EQUIPMENT_REQUIRED]->(b:required_equipment)
		RETURN b.name  '''
equipment = graph.run(query, parameters={'crop_name': 'paddy'}).evaluate()
print(equipment)

print("Getting fertilizers required:")
query=''' MATCH(a: Crop{name:{crop_name}}) -[:FERTILIZERS_REQUIRED]->(b:required_fertilizers)
		RETURN b.name  '''
fertilizers = graph.run(query, parameters={'crop_name': 'paddy'}).evaluate()
print(fertilizers)

print("Getting required soil type:")
query=''' MATCH(a: Crop{name:{crop_name}}) -[:SUITABLE_SOIL_TYPE]->(b:soiltype)
		RETURN b.name  '''
soiltype = graph.run(query, parameters={'crop_name': 'paddy'}).evaluate()
print(soiltype)
