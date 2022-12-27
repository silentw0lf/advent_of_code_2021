connec = [(t[0], t[1]) for t  in [x.split("-") for x in open("input.txt").read().splitlines()]]

def rec1(graph, cave, saved):
    paths = []
    new_saved = saved + [cave]
    if cave == "end":
        return [new_saved]
    for neighbor in graph[cave]:
        if neighbor != "start" and not(neighbor in saved and neighbor[0].islower()):
            paths.extend(rec1(graph, neighbor, new_saved))
    return paths

graph = {}
for s,d in connec:
    if s not in graph:  graph[s] = set()
    if d not in graph:  graph[d] = set() 
    graph[s].add(d)
    graph[d].add(s)

print(len(rec1(graph, "start", [])))

