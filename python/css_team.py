from data_google_sheet import df_team

with open("./css/style_teams.css", "w") as f_team:
    f_team.write(
         f"""

        .GL .team__logo {{
            background-color: {df_team.loc["GL","color"]};
        }}
        .GL {{
            order: {df_team.loc["GL","order"]};
        }}

        
    
        .O .team__logo {{
            background-color: {df_team.loc["O","color"]}:
        }}
        .O {{
            order: {df_team.loc["O","order"]};
        }}
        


    
        .Z .team__logo {{
            background-color: {df_team.loc["Z","color"]};
        }}
        .Z {{
            order: {df_team.loc["Z","order"]};
        }}
        

        .M .team__logo {{
            background-color: {df_team.loc["M","color"]};
        }}
        .M {{
            order: {df_team.loc["M","order"]};
        }}
        

        
        .DS .team__logo {{
            background-color: {df_team.loc["DS","color"]};
        }}
        .DS {{
            order: {df_team.loc["DS","order"]};
        }}
       
       
        
        .DU .team__logo {{
            background-color: {df_team.loc["DU","color"]};
        }}
        .DU {{
            order: {df_team.loc["DU","order"]};
        }}



        
        .OT .team__logo {{
            background-color: {df_team.loc["ÖT","color"]};
        }}
        .OT {{
            order: {df_team.loc["ÖT","order"]};
        }}



       
        .GG .team__logo {{
            background-color: {df_team.loc["GG","color"]};
        }}
        .GG {{
            order: {df_team.loc["GG","order"]};
        }}



        .CH .team__logo {{
            background-color: {df_team.loc["CH","color"]};
        }}
        .CH {{
            order: {df_team.loc["CH","order"]};
        }}


 
        .GO .team__logo {{
            background-color: {df_team.loc["GÖ","color"]};
        }}
        .GO {{
            order: {df_team.loc["GÖ","order"]};
        }}




        .GV .team__logo {{
            background-color: {df_team.loc["GV","color"]};
        }}
        .GV {{
            order: {df_team.loc["GV","order"]};
        }}


        .SC .team__logo {{
            background-color: {df_team.loc["SC","color"]};
        }}
        .SC {{
            order: {df_team.loc["SC","order"]};
        }}


        .V .team__logo {{
            background-color: {df_team.loc["V","color"]};
        }}
        .V {{
            order: {df_team.loc["V","order"]};
        }}



        .MK .team__logo {{
            background-color: {df_team.loc["MK","color"]};
        }}
        .MK {{
            order: {df_team.loc["MK","order"]};
        }}


        .SA .team__logo {{
            background-color: {df_team.loc["SA","color"]};
        }}
        .SA {{
            order: {df_team.loc["SA","order"]};
        }}
        

        .P .team__logo {{
            background-color: {df_team.loc["P","color"]};
        }}
        .P {{
            order: {df_team.loc["P","order"]};
        }}



        .R .team__logo {{
            background-color: {df_team.loc["R","color"]};
        }}
        .R {{
            order: {df_team.loc["R","order"]};
        }}



        .HS .team__logo {{
            background-color: {df_team.loc["HS","color"]};
        }}
        .HS {{
            order: {df_team.loc["HS","order"]};
        }}

        

        .CE .team__logo {{
            background-color: {df_team.loc["CE","color"]};
        }}
        .CE {{
            order: {df_team.loc["CE","order"]};
        }}


        .PP .team__logo {{
            background-color: {df_team.loc["PP","color"]};
        }}
        .PP {{
            order: {df_team.loc["PP","order"]};
        }}

        
        .HW .team__logo {{
            background-color: {df_team.loc["HW","color"]};
        }}
        .HW {{
            order: {df_team.loc["HW","order"]};
        }}



        .KR .team__logo {{
            background-color: {df_team.loc["KR","color"]};
        }}
        .KR {{
            order: {df_team.loc["KR","order"]};
        }}
        
        
        .CO .team__logo {{
            background-color: {df_team.loc["CO","color"]};
        }}
        .CO {{
            order: {df_team.loc["CO","order"]};
        }}



        .HV .team__logo {{
            background-color: {df_team.loc["HV","color"]};
        }}
        .HV {{
            order: {df_team.loc["HV","order"]};
        }}




        .BR .team__logo {{
            background-color: {df_team.loc["BR","color"]};
        }}
        .BR {{
            order: {df_team.loc["BR","order"]};
        }}


        .CA .team__logo {{
            background-color: {df_team.loc["CA","color"]};
        }}
        .CA {{
            order: {df_team.loc["CA","order"]};
        }}



        .SP .team__logo {{
            background-color: {df_team.loc["SP","color"]};
        }}
        .SP {{
            order: {df_team.loc["SP","order"]};
        }}



        .HO .team__logo {{
            background-color: {df_team.loc["HO","color"]};
        }}
        .HO {{
            order: {df_team.loc["HO","order"]};
        }}

        
        """ )


print("Python: style_teams.css compiled")