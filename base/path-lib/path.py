from pathlib import Path

p = Path("Raymond")
if p.exists():
    p.rmdir()

p1 = Path()
for file in p1.glob("*.txt"):
    print(file)