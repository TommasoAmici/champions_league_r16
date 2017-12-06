# AUTHOR: TOMMASO AMICI
# simulates draw for round of 32 in the Europa League
# prints pandas output to terminal and to draws_32_EL.csv
# the number of simulations is an int passed as argv[1]


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
    if len(match_ups) == 16:
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
    teams_pot_1 = [{"name": "Villarreal", "nation": "ES", "group": "A"},
                   {"name": "Dynamo Kyiv", "nation": "UK", "group": "B"},
                   {"name": "Braga", "nation": "PT", "group": "C"},
                   {"name": "Milan", "nation": "IT", "group": "D"},
                   {"name": "Atalanta", "nation": "IT", "group": "E"},
                   {"name": "Sheriff", "nation": "ML", "group": "F"},
                   {"name": "FCSB", "nation": "RO", "group": "G"},
                   {"name": "Arsenal", "nation": "EN", "group": "H"},
                   {"name": "Salzburg", "nation": "AU", "group": "I"},
                   {"name": "Ostersunds", "nation": "SWE", "group": "J"},
                   {"name": "Lazio", "nation": "IT", "group": "K"},
                   {"name": "Zenit", "nation": "RU", "group": "L"},
                   {"name": "CSKA Moskva", "nation": "RU", "group": "CL1"},
                   {"name": "RB Leipzig", "nation": "DE", "group": "CL2"},
                   {"name": "Atletico Madrid", "nation": "ES", "group": "CL3"},
                   {"name": "Sporting", "nation": "PT", "group": "CL4"}]

    teams_pot_2 = [{"name": "Slavia Praha", "nation": "CZ", "group": "A"},
                   {"name": "Partizan", "nation": "SRB", "group": "B"},
                   {"name": "Ludogorets", "nation": "BG", "group": "C"},
                   {"name": "AEK Athens", "nation": "GR", "group": "D"},
                   {"name": "Olympique Lyonnais", "nation": "FR", "group": "E"},
                   {"name": "Lokomotiv Moskva", "nation": "RU", "group": "F"},
                   {"name": "Viktoria Plzen", "nation": "CZ", "group": "G"},
                   {"name": "Koln", "nation": "DE", "group": "H"},
                   {"name": "Marseille", "nation": "FR", "group": "I"},
                   {"name": "Athletic Club", "nation": "ES", "group": "J"},
                   {"name": "Nice", "nation": "FR", "group": "K"},
                   {"name": "Real Sociedad", "nation": "ES", "group": "L"},
                   {"name": "Borussia Dortmund", "nation": "DE", "group": "CL5"},
                   {"name": "Celtic", "nation": "SC", "group": "CL6"},
                   {"name": "Napoli", "nation": "IT", "group": "CL7"},
                   {"name": "Spartak Moskva", "nation": "RU", "group": "CL8"}]

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
    df.to_csv("draws_32_EL.csv", sep=",")
    df_percentages = df.apply(sim_percentage, simulations=simulations)
    print(df_percentages)
    df_percentages.to_csv("draws_32_EL.csv", sep=",", mode="a")


main()
