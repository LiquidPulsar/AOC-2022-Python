from pathlib import Path
HOME = Path(__file__).parent

DATA = (HOME/"input.txt").read_text()

print(
    sum(sorted(
        (sum(map(int,elf.splitlines()))
        for elf in DATA.split("\n\n")),
        reverse = True
    )[:3])
)