from py2neo import Graph


graph = Graph("bolt://localhost:7687", auth=('neo4j', 'abc'))






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
