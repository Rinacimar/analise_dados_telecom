from tokenize import cookie_re
import pandas as pd
import plotly.express as px

table = pd.read_csv("telecom_users.csv")
table = table.drop("Unnamed: 0", axis=1) #axis é o eixo de coluna ou linha;  0 = linha e 1 = coluna
#print(table.info())

table["TotalGasto"] = pd.to_numeric(table["TotalGasto"], errors="coerce")
#print(table.info())

table = table.dropna(how = "all", axis = 1)
table = table.dropna(how = "any", axis = 0)
#print(table.info())

print(table["Churn"].value_counts(normalize=True).map("{:.2%}".format)) #o .2 é de duas casas decimais

for coluna in table.columns:
    grafico = px.histogram(table, x=coluna, color="Churn")
    grafico.show()