import pandas as pd
from datetime import datetime
import json
import numpy as np
import glob

# variables
now = datetime.today().strftime('%Y-%m-%d')
now = "2025-05-12"

# settings
prev, curr = "2025-02-18", now


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
# no indy participants in the top-5


# Indy: Wodapalooza '25
meta = {"comp": "WZA '25", "D": 150, "C": 15}
# no indy participants in the top-15

# Indy: Picsil Showdown
# https://arena.wodbuster.com/competition.aspx?id=2551
meta = {"comp": "Picsil'25", "D": 20 + 40, "C": 5}
data = data + [
    {"name": "Moritz Fiebig", "gender": "m", "place": 3, **meta},
]

# Eurasia Throwdown
# https://competitioncorner.net/ff/16639/results
meta = {"comp": "Eurasia TD", "D": 20, "C": 5}
data = data + [
    {"name": "Jan Arnd Finkenberg", "gender": "m", "place": 2, **meta},
]

# Athens Throwdown
# https://circle21.events/event?competitionId=1de15018-4b21-4cd4-a0f8-4ef8f1a92122
meta = {"comp": "Athens TD", "D": 100 - 40, "C": 10}
data = data + [
    {"name": "Verena Evelyn Reimers", "gender": "f", "place": 10, **meta},
]

# Wodland Fest
# https://competitioncorner.net/ff/15993/results
meta = {"comp": "Wodland Fest", "D": 100 - 20, "C": 20}
data = data + [
    {"name": "Moritz Fiebig", "gender": "m", "place": 2, **meta},
    {"name": "Lenn Postel", "gender": "m", "place": 14, **meta},
    {"name": "Julia Jakobsen", "gender": "f", "place": 11, **meta},
]


# French TD
# https://competitioncorner.net/ff/16541/results/details
# meta = {"comp": "French TD", "D": 100 + 20, "C": 40}
# data = data + [
#     {"name": "", "gender": "m", "place": 1, **meta},
#     {"name": "", "gender": "m", "place": 2, **meta},
#     {"name": "", "gender": "m", "place": 3, **meta},
#     {"name": "", "gender": "f", "place": 1, **meta},
#     {"name": "", "gender": "f", "place": 2, **meta},
#     {"name": "", "gender": "f", "place": 3, **meta},
# ]


# WFP Tour Event 1
# https://competitioncorner.net/ff/16060/results
# meta = {"comp": "WFP 1", "D": 150, "C": 30}



# Indy: iF3 Euros, final day,
# https://scoring.fit/1893/leaderboard
meta = {"comp": "iF3 Euros '24", "D": 100-50, "C": 7}
data = data + [
    {"name": "Julia Jakobsen", "gender": "f", "place": 2, **meta},
    {"name": "Benjamin Huxol", "gender": "m", "place": 2, **meta},
]


# Bohemian Throwdown
# https://competitioncorner.net/ff/12905/results#male_81233
meta = {"comp": "Bohemian TD", "D": 20, "C": 3}
data = data + [
    {"name": "Jan Arnd Finkenberg", "gender": "m", "place": 1, **meta},
]


# Indy: DBVfF Deutsche Meisterschaft
# https://competitioncorner.net/ff/12498/results#male_78581
meta = {"comp": "DBVfF DM'24", "D": 20, "C": 5}
data = data + [
    {"name": "Julius Kieser", "gender": "m", "place": 1, **meta},
    {"name": "Lenn Postel", "gender": "m", "place": 2, **meta},
    {"name": "Benjamin Huxol", "gender": "m", "place": 3, **meta},
    {"name": "Karl Feldmer", "gender": "m", "place": 4, **meta},
    {"name": "Noel Nagel", "gender": "m", "place": 5, **meta},
    {"name": "Julia Jakobsen", "gender": "f", "place": 1, **meta},
    {"name": "Vivien-Marie Christian", "gender": "f", "place": 2, **meta},
    {"name": "Lidia Barto", "gender": "f", "place": 3, **meta},
    {"name": "Caroline Müller-Korn", "gender": "f", "place": 4, **meta},
    {"name": "Verena Evelyn Reimers", "gender": "f", "place": 5, **meta},
]


# CISM Functional Fitness European Open
meta = {"comp": "CISM Euro'24", "D": 100 - 70, "C": 3}
data = data + [
    {"name": "Odo Federolf", "gender": "m", "place": 1, **meta},
    {"name": "Diana Vetter", "gender": "f", "place": 1, **meta},
    {"name": "Anna Hartje", "gender": "f", "place": 3, **meta},
]


# Battle the Lion
# https://competitioncorner.net/events/13742/details
meta = {"comp": "Lions '24", "D": 20, "C": 3}
data = data + [
    {"name": "Jan Arnd Finkenberg", "gender": "m", "place": 1, **meta},
    {"name": "Nick Mentzel", "gender": "m", "place": 2, **meta},
    {"name": "Jona Kemmann", "gender": "m", "place": 3, **meta},
    {"name": "Klaudia Dabrowska", "gender": "f", "place": 1, **meta},
    {"name": "Pia Zeller", "gender": "f", "place": 2, **meta},
    {"name": "Anna Hartje", "gender": "f", "place": 3, **meta},
]


# CrossFit Games, Indy,
# https://games.crossfit.com/leaderboard/finals/2024?final=225&division=1&sort=0
meta = {"comp": "CF Games '24", "D": 150+50, "C": 40}
data = data + [
    {"name": "Moritz Fiebig", "gender": "m", "place": 33, **meta},
]


# Liege Throwdown, https://competitioncorner.net/ff/13791/results#male_87808
meta = {"comp": "Liege", "D": 20, "C": 3}
data = data + [
    {"name": "Tobias Fox", "gender": "m", "place": 1, **meta},
    {"name": "Lidia Barto", "gender": "f", "place": 1, **meta},
]


# Lowlands TD
# https://competitioncorner.net/ff/12475/results#male_78462
meta = {"comp": "Low'24", "D": 100 - 20, "C": 10}
data = data + [
    {"name": "Tobias Fox", "gender": "m", "place": 2, **meta},
    {"name": "Eric Zuchold", "gender": "m", "place": 3, **meta},
    {"name": "Nick Mentzel", "gender": "m", "place": 5, **meta},
    {"name": "Leon Wagenknecht", "gender": "m", "place": 7, **meta},
]


# GTD
# https://portal.circle21.app/event?competitionId=3e2286e1-6b41-459b-8c72-bf911cf3fa38
meta = {"comp": "GTD'24", "D": 100 - 20, "C": 10}
data = data + [
    {"name": "Moritz Fiebig", "gender": "m", "place": 1, **meta},
    {"name": "Jan Arnd Finkenberg", "gender": "m", "place": 4, **meta},
    {"name": "Nick Mentzel", "gender": "m", "place": 5, **meta},
    {"name": "Felix Rehder", "gender": "m", "place": 6, **meta},
    {"name": "Christoph Verrieth", "gender": "m", "place": 9, **meta},
    {"name": "Julia Jakobsen", "gender": "f", "place": 5, **meta},
    {"name": "Jana Geertz", "gender": "f", "place": 7, **meta},
    {"name": "Lidia Barto", "gender": "f", "place": 9, **meta},
]


# Marbella Championship
# https://competitioncorner.net/ff/11879/results#male_73713
meta = {"comp": "Marbella", "D": 100 - 40, "C": 10}
data = data + [
    {"name": "Caroline Müller-Korn", "gender": "f", "place": 8, **meta},
    {"name": "Benjamin Huxol", "gender": "m", "place": 5, **meta},
]


# Swiss Throwdown,
# https://competitioncorner.net/ff/14028/results#male_89336
meta = {"comp": "Swiss TD", "D": 20, "C": 3}
data = data + [
    {"name": "Julius Kieser", "gender": "m", "place": 1, **meta},
    {"name": "Max Hinkofer", "gender": "m", "place": 3, **meta},
]


# Czech Throwdown,
# https://competitioncorner.net/ff/11801/results#male_73243
meta = {"comp": "Czech TD", "D": 20, "C": 3}
data = data + [
    {"name": "Lenn Postel", "gender": "m", "place": 1, **meta},
    {"name": "Karl Feldmer", "gender": "m", "place": 3, **meta},
    {"name": "Sarah Antonia Ziemens", "gender": "f", "place": 2, **meta},
]


# Rogue Invitational
meta = {"comp": "Rogue '24", "D": 150, "C": 15}
# no participants



# Amsterdam Throwdown
# https://competitioncorner.net/ff/14853/results#male_94600
# 23/24.Nov.'24
meta = {"comp": "Amsterdam", "D": 20, "C": 3}
data = data + [
    {"name": "Lenn Postel", "gender": "m", "place": 2, **meta},
    {"name": "Susan Treppner", "gender": "f", "place": 3, **meta},
]


# Austrian Throwdown,
# https://portal.circle21.app/event?competitionId=72d39ec9-32fa-426f-b0ba-ca976e23fb43
# 30.Nov.
meta = {"comp": "Austria TD", "D": 20, "C": 3}
# nobody in top-3


# Dubai
# 6-8.Dec.'24
# https://competitioncorner.net/events/15168/details
meta = {"comp": "Dubai '24", "D": 150, "C": 15}
data = data + [
      {"name": "Jan Arnd Finkenberg", "gender": "m", "place": 15, **meta},
]


# iF3 Worlds
# 15.Dez,'24
# https://portal.circle21.app/event?competitionId=beb79dfb-7d92-4bce-ad4a-06b17e17873c
meta = {"comp": "iF3 Worlds '24", "D": 150, "C": 6}
data = data + [
    {"name": "Lenn Postel", "gender": "m", "place": 3, **meta},
    {"name": "Julia Jakobsen", "gender": "f", "place": 4, **meta},
]




# ----------------------------------------------------------------------------


# Teams: Wodapalooza, Team of 3
# https://competitioncorner.net/ff/15169/results#team_96480
meta = {"comp": "WZA'25 MMM", "D": 90, "C": 30, "team": 3}
data = data + [
    {"name": "Moritz Fiebig", "gender": "m", "place": 10, **meta},
]


# Teams: CrossFit Semifinals, Team of 4
# https://games.crossfit.com/leaderboard/semifinals/2024?semifinal=237&division=11&sort=0
meta = {"comp": "CF Semis '24 MMFF", "D": 50, "C": 30, "team": 4}
data = data + [
    {"name": "Daniel Goncharov", "gender": "m", "place": 23, **meta}, # Wysh
    {"name": "Karl Feldmer", "gender": "m", "place": 23, **meta}, # Wysh
    {"name": "Sarah Antonia Ziemens", "gender": "f", "place": 23, **meta}, # Wysh
    {"name": "Vivien-Marie Christian", "gender": "f", "place": 23, **meta}, # Wysh
    {"name": "Lars Jakobeit", "gender": "m", "place": 24, **meta}, # Aorta
    {"name": "Hendrik Senf", "gender": "m", "place": 24, **meta}, # Aorta
    {"name": "Susan Treppner", "gender": "f", "place": 24, **meta}, # Aorta
    {"name": "Leon Wagenknecht", "gender": "m", "place": 3, **meta}, # Oslo Kriger PSL
    {"name": "Felix Rehder", "gender": "m", "place": 5, **meta}, # Bucher's Lab
]

# Teams: CrossFit Games, Team of 4
meta = {"comp": "CFG '24 MMFF", "D": 100, "C": 30, "team": 4}
data = data + [
    {"name": "Leon Wagenknecht", "gender": "m", "place": 20, **meta}, # Oslo Kriger PSL
    {"name": "Felix Rehder", "gender": "m", "place": 28, **meta}, # Bucher's Lab
]


# Teams: Battle the Beach, MM, FF, MF
# https://portal.circle21.app/event?competitionId=1e0b79ee-b731-4b7b-9183-25003a43ccda
meta = {"comp": "BtB '24 MM", "D": 15, "C": 1, "team": 2}
data = data + [
    {"name": "Jan Arnd Finkenberg", "gender": "m", "place": 1, **meta},
    {"name": "Odo Federolf", "gender": "m", "place": 1, **meta},
]
meta = {"comp": "BtB '24 FF", "D": 15, "C": 1, "team": 2}
data = data + [
    {"name": "Vivien-Marie Christian", "gender": "f", "place": 1, **meta},
    {"name": "Susan Treppner", "gender": "f", "place": 1, **meta},
]
meta = {"comp": "BtB '24 MF", "D": 15, "C": 1, "team": 2}
data = data + [
    {"name": "Oskar Günther", "gender": "m", "place": 1, **meta},
    {"name": "Judith Melcher", "gender": "f", "place": 1, **meta},
]


# Teams: Double Trouble, MF
# https://portal.circle21.app/event?competitionId=09edff51-5283-4076-a07a-a5f3ea98ff63
meta = {"comp": "DT '24 MF", "D": 15, "C": 1, "team": 2}
# no top-1


# Teams: iF3 Worlds, Team of 4, final day
# https://portal.circle21.app/event?competitionId=beb79dfb-7d92-4bce-ad4a-06b17e17873c
meta = {"comp": "iF3 Worlds '24 MMFF", "D": 75, "C": 6, "team": 4}
data = data + [
    {"name": "Noel Nagel", "gender": "m", "place": 3, **meta},
    {"name": "Karl Feldmer", "gender": "m", "place": 3, **meta},
    {"name": "Vivien-Marie Christian", "gender": "f", "place": 3, **meta},
    {"name": "Sarah Antonia Ziemens", "gender": "f", "place": 3, **meta},
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
    df_tmp["total_diff"] = df_tmp["total"] - df_tmp["total_prev"]
    df_tmp = df_tmp.rename_axis("name").reset_index()
    df_tmp = df_tmp[["name", "rank", "total", "rank_diff", "total_diff", "comps", "details"]]
    df_tmp.to_csv(f"results/{gender}c-{curr}.csv", index=False)
    df_tmp.to_json(f"results/{gender}c-{curr}.json", orient="records")

