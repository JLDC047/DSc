import pandas as pd
import plotly.graph_objects as go

covid = pd.read_csv("WHO-COVID-19-global-data.csv")

covid["DateReported"] = pd.to_datetime(covid["DateReported"])
covid.info()

countries = covid.groupby("Country")

France = countries.get_group("France")
print(France.head(5))

main_figure = go.Figure()
main_figure.add_trace(go.Scatter(x=France["DateReported"],y=France["Cumulative_cases"],line_color="blue",fillcolor="lightblue",fill="tonexty"))
main_figure.update_layout(title="France Cases by Dates")
main_figure.write_html("figure1.html", auto_open=True)

main_figure = go.Figure()
main_figure.add_trace(go.Scatter(x=France["DateReported"],y=France["Cumulative_deaths"]))
main_figure.update_layout(title="France Deaths by Dates")
main_figure.write_html("figure2.html", auto_open=True)

main_figure = go.Figure()
main_figure.add_trace(go.Scatter(x=France["DateReported"],y=France["New_cases"]))
main_figure.update_layout(title="Daily New Cases")
main_figure.write_html("figure3.html", auto_open=True)


