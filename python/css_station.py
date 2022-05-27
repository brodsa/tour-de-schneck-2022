from data_google_sheet import df_station


with open("./css/style_station.css", "w") as f_station:
    f_station.write(
        f"""
        .A .station__teams::after {{
            content: \"{df_station.loc["A","w_teams_done"]}\"
        }}
        
        .B .station__teams::after {{
            content: \"{df_station.loc["B","w_teams_done"]}\"
        }}

        .C .station__teams::after {{
            content: \"{df_station.loc["C","w_teams_done"]}\"
        }}

        .D .station__teams::after {{
            content: \"{df_station.loc["D","w_teams_done"]}\"
        }}

        .E .station__teams::after {{
            content: \"{df_station.loc["E","w_teams_done"]}\"
        }}

        .F .station__teams::after {{
            content: \"{df_station.loc["F","w_teams_done"]}\"
        }}

        .G .station__teams::after {{
            content: \"{df_station.loc["G","w_teams_done"]}\"
        }}

        .H .station__teams::after {{
            content: \"{df_station.loc["H","w_teams_done"]}\"
        }}

        .I .station__teams::after {{
            content: \"{df_station.loc["I","w_teams_done"]}\"
        }}

        .J .station__teams::after {{
            content: \"{df_station.loc["J","w_teams_done"]}\"
        }}

        .K .station__teams::after {{
            content: \"{df_station.loc["K","w_teams_done"]}\"
        }}

        .L .station__teams::after {{
            content: \"{df_station.loc["L","w_teams_done"]}\"
        }}

        """ )

print("Python: style_station.css compiled")