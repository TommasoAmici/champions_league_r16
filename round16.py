# AUTHOR: TOMMASO AMICI
# simulates draw for round of 16 in the champions league
# prints pandas output to terminal and to draws.csv
# the number of simulations (about 30% of all tries) is an int passed as argv[1]


import random
import pandas as pd
import sys


# checks if match is possible: team from different group and different nation
def valid(t1, t2):
    return t1["nation"] != t2["nation"] and t1["group"] != t2["group"]


# creates list of possible matches given a team
def possible(team1, pot2):
    return [team for team in pot2 if valid(team1, team)]


# simulates a draw
def draw(p1, p2, simulations):
    match_ups = []
    # randomly picks a team, generates list of possible matches
    while len(p1) > 0:
        t1 = random.choice(p1)
        try:
            t2 = random.choice(possible(t1, p2))
        except Exception as e:
            break
        try:
            if valid(t1, t2):
                match_ups.append((t2["name"], t1["name"]))
                p1.pop(p1.index(t1))
                p2.pop(p2.index(t2))
            else:
                continue
        except Exception as e:
            continue
    # checks that 8 matches were generated
    if len(match_ups) == 8:
        return match_ups, simulations + 1
    return [], simulations


# adds information about genereated matches to pandas dataframe
def parse_match_ups(df, match_ups):
    for match in match_ups:
        df.at[match[0], match[1]] += 1


# creates percentages of match probability, given the number of simulations
def sim_percentage(matches_num, simulations):
    return (matches_num / simulations)


def main():
    teams_pot_1 = [{"name": "Manchester United", "nation": "EN", "group": "A"},
                   {"name": "PSG", "nation": "FR", "group": "B"},
                   {"name": "Roma", "nation": "IT", "group": "C"},
                   {"name": "Barcelona", "nation": "ES", "group": "D"},
                   {"name": "Liverpool", "nation": "EN", "group": "E"},
                   {"name": "Manchester City", "nation": "EN", "group": "F"},
                   {"name": "Besiktas", "nation": "TK", "group": "G"},
                   {"name": "Tottenham", "nation": "EN", "group": "H"}]

    teams_pot_2 = [{"name": "Basel", "nation": "CH", "group": "A"},
                   {"name": "Bayern", "nation": "DE", "group": "B"},
                   {"name": "Chelsea", "nation": "EN", "group": "C"},
                   {"name": "Juventus", "nation": "IT", "group": "D"},
                   {"name": "Sevilla", "nation": "ES", "group": "E"},
                   {"name": "Shaktar", "nation": "UK", "group": "F"},
                   {"name": "Porto", "nation": "PT", "group": "G"},
                   {"name": "Real Madrid", "nation": "ES", "group": "H"}]

    df = pd.DataFrame(0, index=[t["name"] for t in teams_pot_2], columns=[
                      t["name"] for t in teams_pot_1])
    simulations = 0
    for i in range(int(sys.argv[1])):
        # makes copies of the pots to pop elements later
        p1 = teams_pot_1[:]
        p2 = teams_pot_2[:]
        match_ups, simulations = draw(p1, p2, simulations)
        # match_ups can return as an empty list
        if match_ups:
            parse_match_ups(df, match_ups)
    # print to terminal and save to .csv
    print("Simulations:", simulations)
    print(df)
    df.to_csv("draws.csv", sep=",")
    df_percentages = df.apply(sim_percentage, simulations=simulations)
    print(df_percentages)
    df_percentages.to_csv("draws.csv", sep=",", mode="a")


main()
