
import pandas as pd

covid_data = pd.read_csv("covid_data.csv")

covid_data = covid_data.iloc[:,[2,3,-7,-6,-5,-4]]
#print(covid_data.head(10))

#print(covid_data.isnull().sum())

covid_data["Province_State"].fillna(value="",inplace=True)
#print(covid_data.isnull().sum())

groupedByCountry = covid_data.groupby("Country_Region")
print(groupedByCountry.sum()["Australia"])

