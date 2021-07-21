#
import os
import json
import random
import pandas as pd

# vue-dark, graywhite
stats = "[![IvanaXu's github stats](https://github-readme-stats.vercel.app/api?username=IvanaXu&show_icons=true&theme=vue-dark)](https://github.com/anuraghazra/github-readme-stats)"
toplangs = """<img align="right" src="https://github-readme-stats.vercel.app/api/top-langs/?username=IvanaXu&langs_count=3&theme=graywhite" />"""
title = f"{stats}\n{toplangs}\n# བཀྲ་ཤིས་བདེ་ལེགས་"

# 1
with open(f"poetry{random.randint(0,5)}.json", "r", encoding="utf-8") as f:
    data = json.load(f)
ldata = [jdata for idata in data["content"] for jdata in idata["content"]]

def rdata(d):
    if 'paragraphs' not in d:
        return f"> {d['chapter']}\n> \n> " + "\n> \n> ".join(d['content']) + "\n>"
    elif 'author' not in d:
        return f"> {d['chapter']}\n> \n> " + "\n> \n> ".join(d['paragraphs']) + "\n>"
    else:
        return f"> {d['chapter']}\n> \n> {d['author']}\n> \n> " + "\n> \n> ".join(d['paragraphs']) + "\n>"
conts = rdata(random.choice(ldata))
# print(conts)

# 2
ldata = [f"Poetry/{i}" for i in os.listdir("Poetry") if i.endswith(".csv")]

def rdata(d):
    d = pd.read_csv(d).sample(1).values
    return f"> {d[0][0]}\n>\n> {d[0][1]}·{d[0][2]}\n>\n> " + "\n> \n> ".join([_+"。" for _ in d[0][3].split("。") if _])
conts = rdata(random.choice(ldata))
print(conts)

# Write
with open("README.md", "w") as f:
    f.write(f"{title}\n{conts}")

# Thx
"""
    https://github.com/chinese-poetry/chinese-poetry.
    https://github.com/Werneror/Poetry.
"""
