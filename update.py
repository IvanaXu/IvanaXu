#
import os
import json
import random
import pandas as pd

# vue-dark, graywhite
u = "IvanaXu"
url1 = f"https://github-readme-stats.vercel.app/api?username={u}&show_icons=true&theme=vue-dark"
url2 = f"https://github.com/anuraghazra/github-readme-stats"
url3 = f"https://github-readme-stats.vercel.app/api/top-langs/?username={u}&langs_count=8&theme=graywhite"
t = "Programming\tTimes/SinceJul.29.2021"
url4 = f"https://github-readme-stats.vercel.app/api/wakatime?username={u}&layout=compact&langs_count=8&theme=vue-dark&custom_title={t}"
# langs_count url3/url4 6/7, 8/8

stats = f"[![IvanaXu's github stats]({url1})]({url2})"
toplangs = f"""<img align="right" src="{url3}" />"""
wakatime = f"""<img src="{url4}" />"""
title = f"""{stats}\n{toplangs}\n{wakatime}\n# བཀྲ་ཤིས་བདེ་ལེགས་"""

# 
if random.random() < 0.618:
    print("@1")
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
    print(conts)
else: 
    print("@2")
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
    1、https://github.com/chinese-poetry/chinese-poetry.
    2、https://github.com/Werneror/Poetry.
    3、https://github.com/anuraghazra/github-readme-stats/issues/1215
"""
