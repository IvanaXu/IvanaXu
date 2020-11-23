import json
import random
with open(f"poetry{random.randint(0,5)}.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# vue-dark, graywhite
stats = "[![IvanaXu's github stats](https://github-readme-stats.vercel.app/api?username=IvanaXu&show_icons=true&theme=graywhite)](https://github.com/anuraghazra/github-readme-stats)"
toplangs = """[![IvanaXu's github stats](https://github-readme-stats.vercel.app/api?username=IvanaXu&show_icons=true&theme=graywhite)](https://github.com/anuraghazra/github-readme-stats)"""
# toplangs = """<img align="right" src="https://github-readme-stats.vercel.app/api/top-langs/?username=IvanaXu&langs_count=3&theme=graywhite" />"""
title = f"{stats}\n{toplangs}\n# བཀྲ་ཤིས་བདེ་ལེགས་"
ldata = [jdata for idata in data["content"] for jdata in idata["content"]]
def rdata(d):
    if 'paragraphs' not in d:
        return f"> {d['chapter']}\n> \n> " + "\n> \n> ".join(d['content']) + "\n>"
    elif 'author' not in d:
        return f"> {d['chapter']}\n> \n> " + "\n> \n> ".join(d['paragraphs']) + "\n>"
    else:
        return f"> {d['chapter']}\n> \n> {d['author']}\n> \n> " + "\n> \n> ".join(d['paragraphs']) + "\n>"
conts = rdata(random.choice(ldata))
print(conts)

with open("README.md", "w") as f:
    f.write(f"{title}\n{conts}")
"""Thx https://github.com/chinese-poetry/chinese-poetry."""