import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

covid_data = pd.read_csv("covid_data.csv")

covid_data = covid_data.iloc[:,[2,3,-7,-6,-5,-4]]
#print(covid_data.head(10))

#print(covid_data.isnull().sum())

covid_data["Province_State"].fillna(value="",inplace=True)
#print(covid_data.isnull().sum())

groupedByCountry = covid_data.groupby("Country_Region")

top10confirmed = groupedByCountry["Confirmed"].sum().nlargest(10)
figure1 = px.scatter(top10confirmed, x=top10confirmed.index, y="Confirmed", size="Confirmed", size_max=150, color=top10confirmed.index, title="Top 10 Covid Countries")
figure1.write_html("top10CovidCountries.html", auto_open=False)

top10deaths = groupedByCountry["Deaths"].sum().nlargest(10)
figure2 = px.bar(top10deaths, x="Deaths", y=top10deaths.index, title="Top 10 Coutries By Covid Deaths", color=top10deaths.index, orientation='h')
figure2.write_html("top10CovidDeaths.html", auto_open=False)

top5statesOfTheUS = groupedByCountry.get_group("US").nlargest(5,"Confirmed")
figure3 = go.Figure(data=[go.Bar(name="Confirmed Cases", x=top5statesOfTheUS["Confirmed"], y=top5statesOfTheUS["Province_State"], orientation='h'),
                go.Bar(name="Deaths", x=top5statesOfTheUS["Deaths"], y=top5statesOfTheUS["Province_State"], orientation='h')])
figure3.update_layout(title="Covid Cases in the US", height=700)
figure3.write_html("USCovidCases.html", auto_open=True)
