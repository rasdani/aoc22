INPUT = "test_input.txt"

with open(INPUT, "r") as f:
    data = f.read().strip().split("\n")

valves = {}
for d in data:
    d = d.split(" ")
    valve = d[1]
    flow = int(d[4][5:].rstrip(";"))
    neighbors = d[9:]
    neighbors = [n.rstrip(",") for n in neighbors]
    valves[valve] = {}
    valves[valve]["flow"] = flow
    valves[valve]["neighbors"] = neighbors


unvisited = {v: None for v in valves.keys()}
visited = {}
current = list(valves.keys())[0]
current_flow = valves[current]["flow"]
valves_list = list(valves.keys())
while unvisited:
    print(current)
    for  neighbor in valves[current]["neighbors"]:
        if neighbor in visited:
            continue

        new_flow = current_flow + valves[neighbor]["flow"]
        if new_flow > current_flow:
            visited[neighbor] = new_flow
    visited[current] = current_flow
    if current=="EE":
        breakpoint()
    try:
        del unvisited[current]
    except KeyError:
        pass
    if not unvisited:
        break
    current = sorted(visited)[-1]
    current_flow = visited[current]

breakpoint()
    

