import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from data_google_sheet import df_team


# Visualization
# df_team["Teamname"] = df_team["short"]
# df_team.sort_values(by=["Score"],inplace=True,ascending=False)
# colors = df_team["color"]
# sns.set_palette(sns.color_palette(colors))

# plt.figure(figsize=(20,10), dpi=200)
# sns.barplot(y = 'Score', x="Teamname", data = df_team)
# plt.xlabel('Team', fontsize=20)
# plt.ylabel('Score', fontsize=20)
# plt.xticks(fontsize= 18)
# plt.yticks(fontsize= 18)
# plt.savefig("./img/Score.png" , dpi = 200)

# df_team.sort_values(by=["Originelle_Zusatzpunkte"],inplace=True,ascending=False)
# colors = df_team["color"]
# sns.set_palette(sns.color_palette(colors))

# plt.figure(figsize=(20,10), dpi=200)
# sns.barplot(y = 'Originelle_Zusatzpunkte', x="Teamname", data = df_team)
# plt.xlabel('Team', fontsize=20)
# plt.ylabel('Bonuspunkte', fontsize=20)
# plt.xticks(fontsize= 18)
# plt.yticks(fontsize= 18)
# plt.savefig("./img/Bonus.png" , dpi = 200)
# print("Python: Plots done")



df_plot = df_team[["w_points","Originelle_Zusatzpunkte","Score"]]
df_plot.reset_index(inplace=True)
df_plot.columns = [ "Team","Gesamt","Bonus","Score"]
#print(df_plot)

# plt.figure(figsize=(20,10), dpi=200)
# bar_plot1 = sns.barplot(x='Team', y='Score', data=df_plot, label="Score", color="gray")
# bar_plot2 = sns.barplot(x='Team', y='Bonus', data=df_plot, label="Bonus", color="#AA2C2E")
# plt.legend(ncol=2, loc="upper right", frameon=True,fontsize=20)
# plt.xticks(rotation=0)
# plt.xticks(fontsize= 18)
# plt.yticks(fontsize= 18)
# plt.xlabel('Team', fontsize=20)
# plt.ylabel('Punkte', fontsize=20)
# plt.savefig("./img/Gesamt.png" , dpi = 200)


plt.figure(figsize=(20,10), dpi=200)
colors = ["#AA2C2E","#D79FA0","gray"]
sns.set_palette(sns.color_palette(colors))
df_pl = pd.melt(df_plot,value_vars=["Gesamt","Score","Bonus"],id_vars="Team")
df_pl.columns = [ "Teams","Punkte","Anzahl"]
print(df_pl)
print(df_plot.dtypes)
sns.barplot(x ="Teams", y = 'Anzahl', data = df_pl, hue = "Punkte")
plt.legend(ncol=2, loc="upper right", frameon=True,fontsize=20)
plt.xticks(fontsize= 18)
plt.yticks(fontsize= 18)
plt.xlabel('Team', fontsize=20)
plt.ylabel('Punkte', fontsize=20)
plt.savefig("./img/Gesamt_unstack.png" , dpi = 200)
# plt.show()