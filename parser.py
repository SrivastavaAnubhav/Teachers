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

vals = {"nodes": [], "edges": []}
for name in labels:
	nodeval = {}
	nodeval["id"] = labels[name]
	nodeval["label"] = name
	vals["nodes"].append(nodeval)

for start in graph:
	for end in graph[start]:
		edgeval = {}
		edgeval["source"] = start
		edgeval["target"] = end
		vals["edges"].append(edgeval)

with open('myGraph.json', 'w') as f:
    json.dump(vals, f)