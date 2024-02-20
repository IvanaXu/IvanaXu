##
import os
import json
import random
import pandas as pd

u = "IvanaXu"
theme = "dark"
"""
vue-dark
graywhite
codeSTACKr
shadow_red
shadow_green
dark
"""

url1 = f"https://github-readme-stats.vercel.app/api?username={u}&theme={theme}"# &show_icons=true&theme=vue-dark
url2 = f"https://github.com/anuraghazra/github-readme-stats"
url3 = f"https://github-readme-stats.vercel.app/api/top-langs/?username={u}&langs_count=8&theme={theme}"# &theme=graywhite

b = "&nbsp;"
t = f"Programming{b}Times{b}(Since{b}Jul.29.2021)"
url4 = f"https://github-readme-stats.vercel.app/api/wakatime?username={u}&layout=compact&langs_count=8&theme={theme}&custom_title={t}&range=all_time" #&theme=vue-dark 
# langs_count url3/url4 6/7, 8/8
# https://github.com/anuraghazra/github-readme-stats/discussions/2668

stats = f"[![IvanaXu's github stats]({url1})]({url2})"
toplangs = f"""<img align="right" src="{url3}" />"""
wakatime = f"""<img src="{url4}" />"""
wakatime_total = f"""[![wakatime](https://wakatime.com/badge/user/5043ee4a-e361-4607-9d47-d557f2005d05.svg)](https://wakatime.com/@5043ee4a-e361-4607-9d47-d557f2005d05)"""

t0 = "[![Website](https://img.shields.io/website?label="
t1 = "https%3A%2F%2Fshields.io"
tianchi = f"""{t0}&up_color=orange&up_message=Tianchi&url={t1})](https://tianchi.aliyun.com/home/science/scienceDetail?userId=1095279182618)"""
kaggle = f"""{t0}&up_color=blue&up_message=Kaggle&url={t1})](https://www.kaggle.com/ivanxu/)"""
yuque = f"""{t0}&up_color=gay&up_message=Yuque&url={t1})](https://www.yuque.com/ivanaxu)"""
leetcode = f"""{t0}&up_color=brown&up_message=Leetcode&url={t1})](https://leetcode.cn/u/ivanaxu)"""
aistduio = f"""{t0}&up_color=violet&up_message=AIstudio&url={t1})](https://aistudio.baidu.com/aistudio/personalcenter/thirdview/979775)"""
gitee = f"""{t0}&up_color=red&up_message=Gitee&url={t1})](https://gitee.com/IvanaXu)"""
monkeytype = f"""{t0}&up_color=yellow&up_message=Monkeytype&url={t1})](https://monkeytype.com/profile/IvanaXu)"""
EDA = f"""{t0}alpha&up_color=blue&up_message=EDA&url={t1})](http://eda.tangjt.cn/)"""

# latest
# title = f"""{stats}\n{toplangs}\n{wakatime}\n# བཀྲ་ཤིས་བདེ་ལེགས་\t{wakatime_total}\t{tianchi}\t{yuque}\t{leetcode}\t{aistduio}\t{gitee}"""
# title = f"""{stats}\n# བཀྲ་ཤིས་བདེ་ལེགས་\t{wakatime_total}\t{tianchi}\t{yuque}\t{leetcode}\t{aistduio}\t{gitee}"""
title = (
    # f"""{toplangs} \n\n"""
    f"""### བཀྲ་ཤིས་བདེ་ལེགས་ \n"""
    f"""- {wakatime_total} \n"""
    f"""- _Person_\t{tianchi}\t{aistduio}\t{kaggle}\t{yuque}\t{leetcode}\t{gitee}\t{monkeytype} \n"""
    f"""- _Product_\t{EDA} \n"""
    f"""- _Poetry Daily_\t02.20 \n\n"""
    # f"""> [!NOTE]\\"""
)

## 
if random.random() < 0.618:
    print("@1")
    with open(f"poetry{random.randint(0, 5)}.json", "r", encoding="utf-8") as f:
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
    
    
## Write
with open("README.md", "w") as f:
    # f.write("![](./Source/5eecf35f693f168adc0bc5ad06da35ad.jpg)")
    f.write(f"{title}\n{conts}\n")
    # f.write(latest)

## Thx
"""
    https://github.com/chinese-poetry/chinese-poetry.
    https://github.com/Werneror/Poetry.
    https://github.com/anuraghazra/github-readme-stats/issues/1215
    https://github.com/anuraghazra/github-readme-stats
    https://github.com/kautukkundan/Awesome-Profile-README-templates
    https://www.cainiaojc.com/html/html-nbsp.html
"""
