from pathlib import Path
import os

p = Path("raymond/")
if p.exists():
    print("The path is exists")

p1 = Path()
for file in p1.glob("*.txt"):
    print(file)

file_path = "raymond"
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That's a file")
    elif os.path.isdir(file_path):
        print("That's a directory")
else:
    print(f"The location '{file_path}' you provide doesn't exists")
