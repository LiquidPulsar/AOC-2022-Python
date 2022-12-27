from pathlib import Path

HOME = Path(__file__).parent

DATA = (HOME / "input.txt").read_text()

print(max(sum(map(int, elf.splitlines())) for elf in DATA.split("\n\n")))

print(
    max(
        sum(map(int, elf.splitlines()))
        for elf in (__import__("pathlib")
                    .Path(__file__)
                    .parent / 
                    "input.txt")
        .read_text()
        .split("\n\n")
    )
)