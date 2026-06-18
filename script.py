import pandas as pd
from datetime import datetime
import json
import numpy as np
import glob

# variables
now = datetime.today().strftime('%Y-%m-%d')
now = "2025-12-22"

# settings
prev, curr = "2025-08-31", now


# ----------------------------------------------------------------------------

data = []

# TEMPLATE
# meta = {"comp": "", "D": 20, "C": 3}
# data = data + [
#     {"name": "", "gender": "m", "place": 1, **meta},
#     {"name": "", "gender": "m", "place": 2, **meta},
#     {"name": "", "gender": "m", "place": 3, **meta},
#     {"name": "", "gender": "f", "place": 1, **meta},
#     {"name": "", "gender": "f", "place": 2, **meta},
#     {"name": "", "gender": "f", "place": 3, **meta},
# ]


# UAE Storm Games
# cancelled

# Indy: Wodapalooza '26
# https://competitioncorner.net/ff/19193/results
meta = {"comp": "WZA '26", "D": 150, "C": 15}
# no indy participants in the top-15

# Indy: Picsil Showdown
#meta = {"comp": "Picsil '25", "D": 20 + 40, "C": 5}
# cancelled


# Athens Throwdown
# https://circle21.events/athens-throwdown-2026-finals?tab=leaderboard
#meta = {"comp": "Athens TD '26", "D": 100 - 40, "C": 8}
# Nick Mentzel 11th, out of cutline


# MAD
# https://competitioncorner.net/ff/19407/results
meta = {"comp": "MAD '26", "D": 100 + 20, "C": 40}
data = data + [
    {"name": "Robert Dopke", "gender": "m", "place": 20, **meta},
    {"name": "Lenn Postel", "gender": "m", "place": 14, **meta},
    {"name": "Anja Keller", "gender": "f", "place": 20, **meta},
    {"name": "Sarah Kay", "gender": "f", "place": 32, **meta},
]
# Katarina Isele 41th, out of cutline

# French TD
# https://competitioncorner.net/ff/20465/results
meta = {"comp": "FTD '26", "D": 100 + 20, "C": 40}
data = data + [
    {"name": "Moritz Fiebig", "gender": "m", "place": 2, **meta},
    {"name": "Eric Zuchold", "gender": "m", "place": 29, **meta},
    {"name": "Julia Jakobsen", "gender": "f", "place": 11, **meta},
]

# WFP Tour Event 1
# https://competitioncorner.net/ff/19995/results
meta = {"comp": "WFP 1 London '26", "D": 150, "C": 38}
data = data + [
    {"name": "Anja Keller", "gender": "f", "place": 25, **meta},
    {"name": "Julius Kieser", "gender": "m", "place": 20, **meta},
]
# Vivien-Marie Christian 44th, out of cutline


# Indy: iF3 Euros, final day,
#meta = {"comp": "iF3 Euros '25", "D": 100-50, "C": 10}
# no athletes send by the DBVfF

# German Classic
# https://circle21.events/german-classics-indy-finals-2026?tab=leaderboard
meta = {"comp": "German Classic '26", "D": 20, "C": 5}
data = data + [
    {"name": "Jan Arnd Finkenberg", "gender": "m", "place": 1, **meta},
    {"name": "Christoph Verrieth", "gender": "m", "place": 2, **meta},
    {"name": "Max Hinkofer", "gender": "m", "place": 3, **meta},
    {"name": "Siegfried Kramer", "gender": "m", "place": 4, **meta},
    {"name": "Jonathan Sindel", "gender": "m", "place": 5, **meta},
    {"name": "Vroni Wirth", "gender": "f", "place": 1, **meta},
    {"name": "Charis Zach", "gender": "f", "place": 2, **meta},
    {"name": "Laura Dörr", "gender": "f", "place": 3, **meta},
    {"name": "Katharina Blank", "gender": "f", "place": 4, **meta},
    {"name": "Anna Bittner", "gender": "f", "place": 5, **meta},
]

# Eurasia Throwdown
# https://circle21.events/eurasia-throwdown-2026-final?tab=athletes
# meta = {"comp": "Eurasia TD '25", "D": 20, "C": 5}
# no athletes 


# Bohemian Throwdown
# https://circle21.events/bohemian-throwdown-2026-final?tab=leaderboard
meta = {"comp": "Bohemian TD '26", "D": 20, "C": 5}
data = data + [
    {"name": "Max Hinkofer", "gender": "m", "place": 5, **meta},
]

# Battle the Lion
# https://circle21.events/battle-of-the-lion-final-2026
meta = {"comp": "Lion '26", "D": 20, "C": 5}
data = data + [
    {"name": "Pia Zeller", "gender": "f", "place": 1, **meta},
    {"name": "Elena Pommer", "gender": "f", "place": 2, **meta},
    {"name": "Anna Gebel", "gender": "f", "place": 3, **meta},
    {"name": "Laura Gläsner", "gender": "f", "place": 4, **meta},
    {"name": "Christin Chollee", "gender": "f", "place": 5, **meta},

    {"name": "Niklas Plankenhorn", "gender": "m", "place": 1, **meta},
    {"name": "Manuel Rath", "gender": "m", "place": 2, **meta},
    {"name": "Patrick Klinke", "gender": "m", "place": 3, **meta},
    {"name": "Marcel Koppers", "gender": "m", "place": 4, **meta},
    {"name": "Felix Paeper", "gender": "m", "place": 5, **meta},
]

# Varna Throwdown 2025
# https://circle21.events/varna-throwdown-2026-finals
# meta = {"comp": "Varna '25", "D": 20, "C": 5}


# Alsace Throwdown 2025
# https://competitioncorner.net/ff/16498/results
meta = {"comp": "Alsace '25", "D": 20, "C": 3}
data = data + [
    {"name": "Maja Laloš", "gender": "f", "place": 2, **meta},
]
# https://competitioncorner.net/ff/20359/results


# Turku Tuomiopäivä 2025
# https://competitioncorner.net/ff/16620/results
# meta = {"comp": "Turku '25", "D": 20, "C": 5}

# UBL Italian Championship 2025
# https://app.judgerules.it/#/events/760/leaderboard
# meta = {"comp": "UBL '25", "D": 20, "C": 4}


# Indy: DBVfF Deutsche Meisterschaft
# https://competitioncorner.net/events/15263/details
meta = {"comp": "DBVfF DM'25", "D": 20, "C": 5}
data = data + [
    {"name": "Benjamin Huxol", "gender": "m", "place": 1, **meta},
    {"name": "Eric Zuchold", "gender": "m", "place": 2, **meta},
    {"name": "Karl Feldmer", "gender": "m", "place": 3, **meta},
    {"name": "Lenn Postel", "gender": "m", "place": 4, **meta},
    {"name": "Max Hinkofer", "gender": "m", "place": 5, **meta},

    {"name": "Julia Jakobsen", "gender": "f", "place": 1, **meta},
    {"name": "Vivien-Marie Christian", "gender": "f", "place": 2, **meta},
    {"name": "Jana Geertz", "gender": "f", "place": 3, **meta},
    {"name": "Franziska Bröhl", "gender": "f", "place": 4, **meta},
    {"name": "Lidia Barto", "gender": "f", "place": 5, **meta},
]

# Strength in Depth 2025
# https://circle21.events/event?competitionId=fa283049-d38a-4a0d-837f-f8420f414270&tab=leaderboard
meta = {"comp": "SiD '25", "D": 20, "C": 4}
data = data + [
    {"name": "Anja Keller", "gender": "f", "place": 3, **meta},
]


# CISM Regional Military Championships
# meta = {"comp": "CISM Euro'25", "D": 100 - 90, "C": 1}


# Marseille Throwdown
# https://competitioncorner.net/ff/16863/results#female_108983
# meta = {"comp": "Marseille '25", "D": 20, "C": 3}


# CrossFit Games, Indy
# https://games.crossfit.com/leaderboard/finals/2025?final=245&division=1&sort=0
meta = {"comp": "CF Games '25", "D": 150+50, "C": 30}
data = data + [
    {"name": "Moritz Fiebig", "gender": "m", "place": 19, **meta},
]


# Liege Throwdown
# https://competitioncorner.net/events/16388/details
meta = {"comp": "Liege '25", "D": 20, "C": 3}
data = data + [
    {"name": "Lidia Barto", "gender": "f", "place": 2, **meta},
    {"name": "Susan Treppner", "gender": "f", "place": 3, **meta},
    {"name": "Benjamin Huxol", "gender": "m", "place": 1, **meta},
    {"name": "Tobias Becker", "gender": "m", "place": 3, **meta},
]

# WFP Tour Event 2
# https://competitioncorner.net/ff/17218/results#male_111554
meta = {"comp": "WFP 2 '25", "D": 150, "C": 30}
data = data + [
    {"name": "Julius Kieser", "gender": "m", "place": 29, **meta},
]

# Lowlands TD
# https://competitioncorner.net/ff/17935/results#male_116750
meta = {"comp": "Low'25", "D": 100 - 20, "C": 10}
data = data + [
    {"name": "Sarah Kay", "gender": "f", "place": 2, **meta},
    {"name": "Sophia Frey", "gender": "f", "place": 6, **meta},
    {"name": "Judith Melcher", "gender": "f", "place": 7, **meta},
]


# German Throwdown
# https://circle21.events/german-throwdown-2025?tab=leaderboard
meta = {"comp": "GTD'25", "D": 100 - 20, "C": 10}
data = data + [
    {"name": "Julius Kieser", "gender": "m", "place": 1, **meta},
    {"name": "Karl Feldmer", "gender": "m", "place": 3, **meta},
    {"name": "Max Hinkofer", "gender": "m", "place": 5, **meta},
    {"name": "John Schäffer", "gender": "m", "place": 6, **meta},
    {"name": "Christoph Verrieth", "gender": "m", "place": 7, **meta},
    {"name": "Nick Mentzel", "gender": "m", "place": 8, **meta},
    {"name": "Tobias Becker", "gender": "m", "place": 7, **meta},

    {"name": "Julia Jakobsen", "gender": "f", "place": 1, **meta},
    {"name": "Jana Geertz", "gender": "f", "place": 4, **meta},
    {"name": "Lidia Barto", "gender": "f", "place": 6, **meta},
    {"name": "Maja Laloš", "gender": "f", "place": 7, **meta},
    {"name": "Susan Treppner", "gender": "f", "place": 9, **meta},
]


# Marbella Championship
# https://circle21.events/marbella-championship-2025-final-event?tab=leaderboard
# meta = {"comp": "Marbella '25", "D": 100 - 40, "C": 10}
# data = data + [
# ]


# Swiss Throwdown,
# https://circle21.events/swiss-throwdown-2025-finals?tab=leaderboard
meta = {"comp": "Swiss TD", "D": 20, "C": 3}
data = data + [
    {"name": "Siegfried Kramer", "gender": "m", "place": 2, **meta},
]


# Czechia Throwdown,
# https://circle21.events/czechia-throwdown-2025-finals?tab=leaderboard
meta = {"comp": "Czechia TD '25", "D": 20, "C": 5}
data = data + [
    {"name": "Jan Arnd Finkenberg", "gender": "m", "place": 1, **meta},
    {"name": "Lenn Postel", "gender": "m", "place": 2, **meta},
    {"name": "Anja Keller", "gender": "f", "place": 1, **meta},
    {"name": "Anna Bittner", "gender": "f", "place": 4, **meta},
]


# Rogue Invitational
meta = {"comp": "Rogue '24", "D": 150, "C": 15}
# no participants



# Amsterdam Throwdown
# https://competitioncorner.net/ff/18028/results#female_117289
#meta = {"comp": "Amsterdam", "D": 20, "C": 3}
#data = data + [
#]


# Austrian Throwdown,
# https://circle21.events/austrian-throwdown-2025?tab=leaderboard
meta = {"comp": "Austria TD", "D": 20, "C": 4}
data = data + [
    {"name": "Julius Kieser", "gender": "m", "place": 2, **meta},
    {"name": "Julia Jakobsen", "gender": "f", "place": 1, **meta},
]


# Dubai
# ausgefallen
#meta = {"comp": "Dubai '24", "D": 150, "C": 15}
#data = data + [
#]


# iF3 Worlds
# https://circle21.events/2025-if3-worlds-juniors-seniors-teams?tab=leaderboard
# meta = {"comp": "iF3 Worlds '25", "D": 150, "C": 6}
# data = data + [
# ]


# World Fitness Project Finals
# https://competitioncorner.net/ff/17370/results
meta = {"comp": "WFP Finals '25", "D": 200, "C": 30}
data = data + [
    {"name": "Julius Kieser", "gender": "m", "place": 28, **meta},
    {"name": "Vivien-Marie Christian", "gender": "f", "place": 26, **meta},
]




# ----------------------------------------------------------------------------
# Compute Achieved Points per competition

def achieved_points(D, C, P):
    """ Points by placing utility function
    D : competition weight
    C : cutline
    P : placing
    """
    return int(D / C * max(0, C - P + 1))

assert achieved_points(25, 30, 5) == 21


for item in data:
    item["points"] = achieved_points(item["D"], item["C"], item["place"])


# ----------------------------------------------------------------------------
# Sum best 3 competitions scores

# limit to N=3 competitions
N=3

# limit number of team scores
M=2

# sort all entries by largest points
data = sorted(data, key=lambda x: -x.get('points'))

# set team points to zero
namecnt = {}
for i in range(len(data)):
    if data[i].get("team") is not None:
        if namecnt.get(data[i]["name"], 0) >= M:  # reset pts=0
            data[i]["points"] = 0
        namecnt[data[i]["name"]] = 1 + namecnt.get(data[i]["name"], 0)
data = sorted(data, key=lambda x: -x.get('points'))


# aggregate per athlete
tab = {}
for item in data:
    if item["name"] not in tab:
        tab[item["name"]] = {
            "total": 0, "comps": 0, "gender": item["gender"], "details": [], "details2": [],
            "tiebreak": [0]*N
        }
    if len(tab[item["name"]]["details"]) < N:
        tab[item["name"]]["total"] += item["points"]
        i = tab[item["name"]]["comps"]
        tab[item["name"]]["tiebreak"][i] = item["points"]
        tab[item["name"]]["comps"] += 1
    s = f"{item['comp']} ({item['place']}.pl; {item['points']}pts)"
    tab[item["name"]]["details"].append(s)
    d = {k: v for k, v in item.items() if k in ("D", "C", "place", "comp", "points")}
    tab[item["name"]]["details2"].append(d)

# sorting: add total to sorting criteria
for key, val in tab.items():
    val["tiebreak"] = [val["total"], *val["tiebreak"]]

# sort and save json
tab = dict(sorted(tab.items(), key=lambda x: [-v for v in x[1].get('tiebreak')]))
json.dump(tab, open(f"results/data-{now}.json", "w"), indent=4)

# comma-seperated list of N competitions for "details" column
for k, v in tab.items():
    v["details"] = ", ".join(v["details"][:N])

# sort by total ranking points
df = pd.DataFrame(tab).T


# ----------------------------------------------------------------------------
# Save Rankings to CSV

def get_rank(tmp):
    d = np.diff(tmp["tiebreak"].tolist(), axis=0)
    i = 1
    rnk = [i]
    for row in d:
        if all(row == 0):
            rnk.append(i)
            i = i + 1
        else:
            i = i + 1
            rnk.append(i)
    return rnk

for gender in ("m", "f"):
    tmp = df[df["gender"]==gender].copy()
    tmp["rank"] = get_rank(tmp)
    tmp = tmp.rename_axis("name").reset_index()
    tmp = tmp[["name", "rank", "total", "comps", "details"]]
    tmp.to_csv(f"results/{gender}-{curr}.csv", index=False)
    tmp.to_json(f"results/{gender}-{curr}.json", orient="records")


# ----------------------------------------------------------------------------
# Save Ranking Changes to CSV


# search for the previous date
if prev is None:
    FILES = glob.glob(f"results/f-*.xlsx")
    FILES.sort()
    if len(FILES) > 0:
        prev = FILES[-2].split("f-")[-1].split(".xlsx")[0]

print(prev, curr)

# compute the differences
for gender in ("f", "m"):
    df_prev = pd.read_csv(f"results/{gender}-{prev}.csv", index_col=0)
    df_curr = pd.read_csv(f"results/{gender}-{curr}.csv", index_col=0)

    df_tmp = df_curr.join(df_prev, how="left", rsuffix="_prev")
    df_tmp["rank_diff"] = df_tmp["rank_prev"] - df_tmp["rank"]
    df_tmp["total_diff"] = df_tmp["total"] - df_tmp["total_prev"].fillna(0)
    df_tmp = df_tmp.rename_axis("name").reset_index()
    df_tmp = df_tmp[["name", "rank", "total", "rank_diff", "total_diff", "comps", "details"]]
    df_tmp.to_csv(f"results/{gender}c-{curr}.csv", index=False)
    df_tmp.to_json(f"results/{gender}c-{curr}.json", orient="records")

