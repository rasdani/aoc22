INPUT = "test_input.txt"

with open(INPUT, "r") as f:
    data = f.read().strip().split("\n\n")

def compare(left, right, correct=True):
    if left == [1,[2,[3,[4,[5,6,7]]]],8,9]:
        breakpoint()
    if len(right) < len(left):
        return False
    elif len(right) > len(left):
        return True
    # TODO: use idxs instead zip, so [9] vs [8,7,6] can be compared
    for left, right in zip(left, right):
    # i = 0
    # while i < max(len(left), len(right))
        # left, right = 
        if isinstance(left, int) and isinstance(right, int):
            if left > right:
                correct = False
            else:
                correct =  True
        elif isinstance(left, list) and isinstance(right, list):
            # FIX ME: does not recurse into nested list in ex. 8
            correct = compare(left, right, correct)
        elif isinstance(left, int) != isinstance(right, int):
            if isinstance(left, int):
                left = [left] * len(right) # workaround seems fine
            else:
                right = [right] * len(left)
            correct = compare(left, right, correct)

    return correct


correct_idx = []
for i, packet in enumerate(data):
    left, right = packet.split("\n")
    left, right = eval(left), eval(right)
    correct = compare(left, right)
    if correct:
        correct_idx.append(i + 1)



print(correct_idx)
breakpoint()
