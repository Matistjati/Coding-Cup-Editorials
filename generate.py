from pathlib import Path

years = {
    "2026":
        ["X", "X", ("Chalmers", "chalmers-2026.pdf")]
    ,
    "2025":
        ["X", "X", ("Chalmers", "chalmers-2025.pdf")]
    ,
    "2024":
        ["X", "X", ("Chalmers", "chalmers-2024.pdf")]
    ,
    "2023":
        ["X", "X", ("Chalmers", "chalmers-2023.pdf")]
    ,
    "2022":
        ["X", "X", ("Chalmers", "chalmers-2022.pdf")]
    ,
    "2021":
        ["X", "X", ("Chalmers", "chalmers-2021.pdf")]
    ,
}

header = ["Year", "KTH", "LTH", "Chalmers", "Competition 1", "Competition 2"]

print("""Legend:
- X: missing
- *: unofficial
- /: no contest that year

Please contact me if you have any of the missing editorials.
Also feel free to contact me if you believe you have a better version of any of the unofficial ones.
""")

print("| " + " | ".join(header) + " |")
print("|" + "|".join(["------"] * len(header)) + "|")

extensions = ["pdf", "md", "txt"]
def format_url(year, task):
    task_name = None
    task_url = None
    if isinstance(task, str):
        task_name = task
    else:
        task_name = task[0]

    suffix = ""
    for mark in ["(u)", "(t)", "*"]:
        if mark in task_name:
            suffix += mark
            task_name = task_name.replace(mark, "")
    
    if isinstance(task, str):
        task_shortname = ''.join(task_name.split()).lower()
        for ext in extensions:
            if (Path("editions") / year / f"{task_shortname}.{ext}").exists():
                extension = ext
                break
        else:
            assert 0, f"Nothing for {year}/{task_name}"
        task_url = f"editions/{year}/{task_shortname}.{extension}"
    else:
        if "https" in task[1]:
            task_url = task[1]
        else:
            task_url = f"editions/{year}/{task[1]}"

    return f"[{task_name}]({task_url}){suffix}"

tot = 0
has = 0
for year, p_list in years.items():
    if len(p_list) == 0:
        continue

    row = p_list
    while len(row)+1 < len(header):
        row.append("/")

    result = []
    for column, task in enumerate(row):
        task_name = task if isinstance(task, str) else task[0]
        if task and not task_name.startswith("/") and task_name != "X":
            tot += 1
            if "(u)" not in task:
                has += 1
            result.append(format_url(year, task))
        else:
            if not task_name.startswith("/"):
                tot += 1
            result.append(task)
    
    result = [year] + result
    print("| " + " | ".join(result) + " |")

print(f"\n\nProgress: {has/tot*100:.2f}% ({has}/{tot})")
