from pathlib import Path
from more_itertools import sliding_window
DATA = (Path(__file__).parent/"input.txt").read_text()

for i,w in enumerate(sliding_window(DATA, 14)):
    if len(set(w)) == 14:
        print(i+14)
        break