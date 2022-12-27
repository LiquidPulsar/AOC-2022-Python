from pathlib import Path

HOME = Path(__file__).parent

def value(c):
    # print(27+c-ord("A") if c <= ord("Z") else 1+c-ord("a"))
    return 27+c-ord("A") if c <= ord("Z") else 1+c-ord("a")

def score(line):
    line = line.strip()
    l = len(line)//2
    # print(chr(next(iter(set(line[:l])&set(line[l:])))))
    return value(next(iter(set(line[:l])&set(line[l:]))))


with open(HOME/"input.txt","rb") as file:
    print(sum(map(score, file)))