from pathlib import Path

HOME = Path(__file__).parent

def score(ab):
    a,b = ab.split()
    a = ord(a)-ord("A")
    b = ord(b)-ord('X')

    v=3*b
    b=1+(a-1+b)%3

    # print(b+v)
    return b+v

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
#         3*(B:=ord(b)-ord("X"))+((ord(a)-ord('A')-1+B)%3+1)
#         for a,_,b in file.read().splitlines()
#     ))