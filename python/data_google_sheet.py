import json
import unidecode


import gspread
import pandas as pd


# Connect to google sheet
gc = gspread.service_account(filename='forms-tour-de-schneck-7a82ceba1539.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1eHuUXIXMmwADt9B6cpSuLWSNGAWvgYTps6rU6FHEZRQ/edit?resourcekey#gid=174414602')
print("Python: Connected to google sheet")


# Get the data
worksheet = sh.worksheet("Ergebnisse")
list_of_dicts = worksheet.get_all_records()
df_original = pd.DataFrame(list_of_dicts)

worksheet_color = sh.worksheet("Stationsübersicht")
color_list = worksheet_color.get_all_records()
color_df = pd.DataFrame(color_list)
stations_df = color_df[["Stationen","Bezeichnung","Ort","svg_station","id_station"]].iloc[0:12]
stations_df["Station"] = stations_df["Stationen"]

# Data summary for teams and stations
df_tmp = df_original.groupby(["Team", "Station"]).last().reset_index()
df = df_tmp[["Team", "Station", "Score", "Originelle_Zusatzpunkte"]].drop_duplicates().dropna()
df_color = color_df[["Gruppennamen","short","color"]].dropna().iloc[0:28]
df_color["Gruppe"] = df_color["Gruppennamen"]
all_teams = df_color["Gruppe"]

# teams summary
df_team_tmp = df.groupby("Team").sum()
df_team_tmp["Gruppe"] = df_team_tmp.index
df_team_tmp= pd.merge(df_color,df_team_tmp,on=["Gruppe"],how="outer")
df_team_tmp["Score"].fillna(0,inplace=True)
df_team_tmp["Originelle_Zusatzpunkte"].fillna(0,inplace=True)
df_team_tmp["max_score"]= 10 * 12
df_team_tmp["Score"] = df_team_tmp.apply(lambda x: int(x["Score"]), axis=1)
df_team_tmp["Originelle_Zusatzpunkte"] = df_team_tmp.apply(lambda x: int(x["Originelle_Zusatzpunkte"]), axis=1)
df_team_tmp["w_score"] = df_team_tmp.apply(lambda x: str(x["Score"]) + "/" + str(x["max_score"]),axis=1)
df_team_tmp["w_bonus"] = df_team_tmp.apply(lambda x: str(x["Originelle_Zusatzpunkte"]) + "/" + str(3*12),axis=1)
df_team_tmp["id_teams"] = df_team_tmp.apply(lambda x: unidecode.unidecode(x["short"]),axis=1)

df_team_station = pd.DataFrame(df['Team'].value_counts())
df_team_station["station_max"] = 12 
df_team_station["station_done"] = df_team_station["Team"] 
df_team_station["Gruppe"] = df_team_station.index

df_team = pd.merge(df_team_tmp,df_team_station,on="Gruppe",how='outer')
df_team.index = df_team["short"]
df_team['station_max'].fillna(12,inplace=True)
df_team["station_done"].fillna(0,inplace=True)
df_team["station_max"] = df_team.apply(lambda x: int(x["station_max"]), axis=1)
df_team["station_done"] = df_team.apply(lambda x: int(x["station_done"]), axis=1)
df_team["w_station_done"] = df_team.apply(lambda x: str(x["station_done"]) + '/' + str( x["station_max"]),axis=1)
df_team["w_points"] = df_team["Score"] + df_team["Originelle_Zusatzpunkte"]
df_team.sort_values(by=['w_points'], inplace=True, ascending=False)
df_team['order'] = list(range(df_team.shape[0]))
df_team["order"] = df_team.apply(lambda x: int(x["order"]), axis=1)


# write json for teams
dict_team = []
for index, row in df_team.iterrows():
    dict_pre = dict()
    dict_pre["name"] = row["Gruppe"]
    dict_pre["id"] = row["id_teams"]
    dict_pre["name_short"] = row["short"]
    dict_pre["score"] = row["w_score"]
    dict_pre["bonus"] = row["w_bonus"]
    dict_pre["points"] = row["w_points"]
    dict_pre["station_done"] = row["w_station_done"]

    dict_team.append(dict_pre)


with open('_data/teams.json','w',encoding='utf-8') as file:
    json.dump(dict_team, file, indent=2, ensure_ascii=False) 


# stations
df_station = pd.DataFrame(df["Station"].value_counts())
df_station["teams_max"] = 28
df_station["teams_done"] = df_station["Station"]
df_station["Station"] = df_station.index 
df_station = pd.merge(df_station,stations_df,on="Station", how="outer")
df_station["teams_max"].fillna(28,inplace=True)
df_station["teams_done"].fillna(0,inplace=True)
df_station["teams_max"] = df_station.apply(lambda x: int(x["teams_max"]), axis=1)
df_station["teams_done"] = df_station.apply(lambda x: int(x["teams_done"]), axis=1)
df_station["w_teams_done"] = df_station.apply(lambda x: str(x["teams_done"]) + '/' + str(x["teams_max"]),axis=1)

df_station["station"] = df_station.apply(lambda x: str(x["Station"])[-1],axis=1)
df_station.index = df_station["station"]


# write json for stations
dict_station = list()
for index, row in df_station.iterrows():
    dict_pre = dict()
    dict_pre["name"] = row["Station"]
    dict_pre["id"] = row["station"]
    dict_pre["teams"] = row["w_teams_done"]
    dict_pre["description"] = row["Bezeichnung"]
    dict_pre["location"] = row["Ort"]
    dict_pre["svg"] = row["svg_station"]


    dict_station.append(dict_pre)


with open('_data/stations.json','w',encoding='utf-8') as file:
    json.dump(dict_station, file, indent=2, ensure_ascii=False) 


# Example to display
# print("Score {}".format(df_team.loc["CE","w_score"]))
# print("Stationen: {}".format(df_team.loc["CE","w_station_done"]))
# print("Teamsreihnfolge: {}".format(df_team.loc["CE","order"]))
# print("Teams in Stationen: {}".format(df_station.loc["A","w_teams_done"]))
# print("Farbe: {}".format(df_team.loc["CE","color"]))
# print("Abbkürzung: {}".format(df_team.loc["CE","short"]))






