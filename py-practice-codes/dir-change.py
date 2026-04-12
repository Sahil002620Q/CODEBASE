import subprocess

folders = {
    1: "AI-research",
    2: "py-problems",
    3: "py-projects",
    4: "python-modules",
    5: "py-practice-codes",
    6: "Python-games",
    7: "c-practice-codes",
    8: "c-projects",
    9: "DSA"
}

print("Choose project:")

for k, v in folders.items():
    print(f"[{k}] {v}")

x = int(input("Enter choice: "))

base = "ahh_shit_here_we_go_again"

if x in folders:
    path = f"{base}/{folders[x]}"
    subprocess.run(["cmd", "/k", "cd", path])