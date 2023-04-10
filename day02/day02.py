################    Score
# A   Rock     X    1
# B   Paper    Y    2
# C   Scissors Z    3
################
# Score Outcome
# Loss  0
# Draw  3
# Win   6

# INPUT = "test_input.txt"
INPUT = "input.txt"

# If you want to get fancy solve with modular arithmetic
def result(theirs, mine):
    """Return 0 if opponent wins, 6 if I win and 3 for draw
    and add the score for your move"""
    if mine == "X":
        if theirs == "A":
            return 1 + 3
        elif theirs == "B":
            return 1 + 0
        elif theirs == "C":
            return 1 + 6
        else:
            raise RuntimeError(f"{theirs} is invalid")

    elif mine == "Y":
        if theirs == "A":
            return 2 + 6
        elif theirs == "B":
            return 2 + 3
        elif theirs == "C":
            return 2 + 0
        else:
            raise RuntimeError(f"{theirs} is invalid")

    elif mine == "Z":
        if theirs == "A":
            return 3 + 0
        elif theirs == "B":
            return 3 + 6
        elif theirs == "C":
            return 3 + 3
        else:
            raise RuntimeError(f"{theirs} is invalid")

    else:
        raise RuntimeError(f"{mine} is invalid")

### Part Two, copy pasta
def strategy(theirs, mine):
    """ 
    X: I have to loose
    Y: I have to draw
    Z: I have to win
    """ 
    if mine == "X":
        if theirs == "A":
            return 0 + 3
        elif theirs == "B":
            return 0 + 1
        elif theirs == "C":
            return 0 + 2
        else:
            raise RuntimeError(f"{theirs} is invalid")

    elif mine == "Y":
        if theirs == "A":
            return 3 + 1
        elif theirs == "B":
            return 3 + 2
        elif theirs == "C":
            return 3 + 3
        else:
            raise RuntimeError(f"{theirs} is invalid")

    elif mine == "Z":
        if theirs == "A":
            return 6 + 2
        elif theirs == "B":
            return 6 + 3
        elif theirs == "C":
            return 6 + 1
        else:
            raise RuntimeError(f"{theirs} is invalid")

    else:
        raise RuntimeError(f"{mine} is invalid")
    

f = open(INPUT, "r")
f = f.read()
f = f.splitlines()

results = []
for line in f:
    line = line.split(" ")
    # print(line)
    theirs, mine = line
    # res = result(theirs, mine)
    res = strategy(theirs, mine)    # Part 2
    # print(res)
    results.append(res)

total = sum(results)
print(f"Total: {total}")
