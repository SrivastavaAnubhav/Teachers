import json
data = ""
with open('data.json') as f:
	data = json.load(f)

with open("test.txt", "w") as f:
	f.write("vals {")
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

	for name in labels:
		foo = u"{} [label={}]; ".format(labels[name], name)
		f.write(foo.encode('utf8'))

	for start in graph:
		for end in graph[start]:
			bar = u"{} -> {}; ".format(start, end)
			f.write(bar.encode('utf8'))
	f.write("}")