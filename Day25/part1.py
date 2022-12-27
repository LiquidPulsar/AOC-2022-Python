from pathlib import Path

vals = dict(zip('210-=',range(2,-3,-1)))

def snafu_to_dec(snafu:str):
    p = 1
    res = 0
    for c in reversed(snafu):
        res += vals[c] * p
        p *= 5
    return res

def dec_to_snafu(dec:int):
    if dec == 0: return ''
    q,r = divmod(dec,5)
    return dec_to_snafu(q+(r>2)) + '012=-'[r]

# print(snafu_to_dec('1==='))
# print(5**3 - 2*(5**3-1)//4)
# print(snafu_to_dec('==='))
# print(dec_to_snafu(2022))

with open(Path(__file__).parent / "input.txt") as f:
    print(dec_to_snafu(sum(snafu_to_dec(line.strip()) for line in f)))