from pathlib import Path

HOME = Path(__file__).parent

def score(ab):
    a,b = ab.split()
    a = ord(a)-ord("A")
    b = ord(b)-ord("X")

    v = 3*((b-a+1)%3)
    return 1+b + v

# print(score("A Y"))

with open(HOME / "input.txt") as file:
    print(sum(
        map(
            score,
            file
        )
    ))

# with open(HOME /"input.txt") as file:
#     print(sum(
#         1+(B:=ord(b)-ord("X"))+3*((B-ord(a)+ord('A'))%3+1)
#         for a,_,b in file.read().splitlines()
#     ))