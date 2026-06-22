from pathlib import Path

years = {
    "2026":
        [("KTH", "https://youtu.be/Meb1kap46NQ"),
         "X",
         ("Chalmers", "chalmers-2026.pdf"),
         ("PO Open", "https://typst.app/project/rSB2KmP3d2Zrfc61FLv88K")]
    ,
    "2025":
        [("KTH", "https://www.youtube.com/watch?v=_yLGiSwuoDg"),
         ("LTH", "lth-2025.pdf"),
         ("Chalmers", "chalmers-2025.pdf"),
         ("PO Open", "poopen-2025.pdf"),
         ("Lovable", "lovable-2025.pdf")]
    ,
    "2024":
        ["",
         "X",
         ("Chalmers", "chalmers-2024.pdf"),
         ("PO Open", "poopen-2024.pdf")]
    ,
    "2023":
        ["",
         "",
         ("Chalmers", "chalmers-2023.pdf"),
         ("PO Open", "poopen-2023.pdf"),
         ("LiU", "liu-2023.pdf")]
    ,
    "2022":
        [("KTH", "https://www.youtube.com/watch?v=AEHCXK_lrkw"),
         ("LTH", "lth-2022.pdf"),
         ("Chalmers", "chalmers-2022.pdf"),
         ("PO Open", "poopen-2022.pdf"),
         "Final (X)"]
    ,
    "2021":
        [("KTH", "kth-2021.pdf"),
         ("LTH", "https://www.youtube.com/watch?v=yWpvAQf-prY"),
         ("Chalmers", "chalmers-2021.pdf"),
         ("PO Open", "poopen-2021.pdf"),
         "Final (X)",
         "JobAgent (X)"]
    ,
    "2020":
        [("KTH", "kth-2020.pdf"),
         ("LTH", "lth-2020.pdf"),
         "",
         ("PO Open", "poopen-2020.pdf"),
         "Sandvik (X)"]
    ,
    "2019":
        ["X",
         "X",
         "",
         ("PO Open", "poopen-2019.pdf"),
         ("Final", "final-2019.pdf"),
         "LiU (X)",
         "Google (X)"]
    ,
    "2018":
        ["X",
         "",
         "",
         ("PO Open", "poopen-2018.pdf"),
         "Final (X)",
         "HiQ (X)",
         "LiU (X)",
         "Nova (X)"]
    ,
    "2017":
        [("KTH", "kth-2017.pdf"),
         ("LTH", "lth-2017.pdf"),
         "",
         "",
         "HiQ (X)",
         "Kattis Challenge (X)"]
    ,
    "2016":
        [("KTH", "kth-2016.pdf")]
    ,
    "2015":
        [("KTH", "kth-2015.pdf")]
    ,
    "2014":
        [("KTH", "kth-2014.pdf")]
    ,
    "2013":
        [("KTH", "kth-2013.pdf")]
    ,
    "2012":
        [("KTH", "kth-2012.pdf")]
    ,
    "2011":
        [("KTH", "kth-2011.pdf")]
    ,
}

header = ["Year", "KTH", "LTH", "Chalmers", "PO Open", "Competition 1", "Competition 2", "Competition 3", "Competition 4"]

print("""Legend:
- X: missing
- *: unofficial
- empty: no contest that year


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
        row.append("")

    result = []
    for column, task in enumerate(row):
        if task == "":
            result.append("")
            continue
        if isinstance(task, tuple):
            tot += 1
            if "(u)" not in task[0]:
                has += 1
            result.append(format_url(year, task))
            continue
        # String task: either "X" or "Name (X)"
        tot += 1
        result.append(task)

    result = [year] + result
    print("| " + " | ".join(result) + " |")

print(f"\n\nProgress: {has/tot*100:.2f}% ({has}/{tot})")
