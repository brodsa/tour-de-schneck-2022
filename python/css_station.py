from data_google_sheet import df_station


with open("./css/style_station.css", "w") as f_station:
    f_station.write(
        f"""
        .A  {{
            order: {df_station.loc["A","id_station"]};
        }}
        
        .B {{
            order: {df_station.loc["B","id_station"]};
        }}

        .C {{
            order: {df_station.loc["C","id_station"]};
        }}

        .D {{
            order: {df_station.loc["D","id_station"]};
        }}

        .E {{
            order: {df_station.loc["E","id_station"]};
        }}

        .F {{
            order: {df_station.loc["F","id_station"]};
        }}

        .G {{
            order: {df_station.loc["G","id_station"]};
        }}

        .H {{
            order: {df_station.loc["H","id_station"]};
        }}

        .I {{
            order: {df_station.loc["I","id_station"]};
        }}

        .J {{
            order: {df_station.loc["J","id_station"]};
        }}

        .K {{
            order: {df_station.loc["K","id_station"]};
        }}

        .L {{
           order: {df_station.loc["L","id_station"]};
        }}

        """ )

print("Python: style_station.css compiled")