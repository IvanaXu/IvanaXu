import json
import random
with open("poetry2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

title = "# བཀྲ་ཤིས་བདེ་ལེགས་"
ldata = [jdata for idata in data["content"] for jdata in idata["content"]]
rdata = lambda d: f"> {d['chapter']}\n> \n> {d['author']}\n> \n> " + "\n> \n> ".join(d['paragraphs']) + "\n>"
conts = rdata(random.choice(ldata))
print(conts)

with open("README.md", "w") as f:
    f.write(f"{title}\n{conts}")
"""Thx https://github.com/chinese-poetry/chinese-poetry."""
