import json
data = ""
with open('data.json') as f:
	data = json.load(f)

graph = {}
labels = {}
for pair in data:
	myID = 0
	otherID = 0

	if pair["myID"] in labels:
		myID = labels[pair["myID"]]
	else:
		myID = len(labels)
		labels[pair["myID"]] = myID

	if pair["relative"] in labels:
		otherID = labels[pair["relative"]]
	else:
		otherID = len(labels)
		labels[pair["relative"]] = otherID

	if pair["relationship"] == "student":
		fromnode = otherID
		tonode = myID
	else:
		fromnode = myID
		tonode = otherID

	if fromnode in graph:
		graph[fromnode].add(tonode)
	else:
		graph[fromnode] = set([tonode])

with open('myGraph.json', 'w') as f:
	serializedEdges = {}
	for start in graph:
		serializedEdges[start] = list(graph[start])

	g = {}
	g["nodes"] = labels
	g["edges"] = serializedEdges
	json.dump(g, f)
