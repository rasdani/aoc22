import numpy as np

# INPUT = "test_input.txt"
INPUT = "input.txt"

with open(INPUT, "r") as f:
    data = f.read().split("\n\n")
    
monkeys = []
for dat in data:
    d = dat.split("\n")
    items = d[1]
    items = eval(items[18:])
    if isinstance(items, int): items = [items] 
    else: items = [*items]
    items = np.array(items)    # Part 2
    op = d[2][19:]
    test = d[3].split(" ")[-1]
    t = d[4].split(" ")[-1]
    f = d[5].split(" ")[-1]
    attr = {
            "items": items,
            "op": op,
            "test": int(test),
            "true": int(t),
            "false": int(f),
            "insp": 0
            }
    monkeys.append(attr)

# for _ in range(20):    # Part 1
# TODO: look into map() & reduce() or numpy
for _ in range(10000):    # made wrong tradeoff readability vs. performance
    print(_)
    for m in monkeys:
        op = m["op"]
        test = m["test"]
        items = m["items"]
        if len(items) > 1:
            # m["items"] = [eval(op) for old in m["items"]]
            # m["items"] = [int(old/3) for old in m["items"]]
            for old in items[:]:
                m["insp"] += 1
                new = eval(op)
                # new = int(new/3)    # Part 1
                if new%test == 0:
                    to = m["true"]
                    # items.pop(0)
                    np.delete(items, 0)
                    # monkeys[to]["items"].append(i.m["items"].pop(0))
                    # monkeys[to]["items"] = monkeys[to]["items"] + [m["items"].pop(0)]
                    # monkeys[to]["items"].append(new)
                    monkeys[to]["items"] = np.append(monkeys[to]["items"], new)
                else:
                    to = m["false"]
                    # items.pop(0)
                    np.delete(items, 0)
                    # monkeys[to]["items"].append(i.m["items"].pop(0))
                    # monkeys[to]["items"] = monkeys[to]["items"] + [m["items"].pop(0)]
                    # monkeys[to]["items"].append(new)
                    monkeys[to]["items"] = np.append(monkeys[to]["items"], new)

        elif items:
            m["insp"] += 1
            old = m["items"][0]
            item = eval(op)
            # item = int(item / 3)   # Part 1
            if item%test == 0:
                to = m["true"]
                # items.pop(0)
                np.delete(items, 0)
                # monkeys[to]["items"].append(item)
                monkeys[to]["items"] = np.append(monkeys[to]["items"], new)
            else:
                to = m["false"]
                # items.pop(0)
                np.delete(items, 0)
                # monkeys[to]["items"].append(item)
                monkeys[to]["items"] = np.append(monkeys[to]["items"], new)

inspections = sorted([m["insp"] for m in monkeys])
print(inspections[-2] * inspections[-1])
