import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

df_dsa = pd.read_csv("dataset.csv")
# print(df_dsa.shape)
# print(type(df_dsa))
# print(df_dsa.dtypes)
# df_dsa.info()
# print(df_dsa.head(10))
# print(df_dsa.tail())
# print(df_dsa.columns)
# print(list(df_dsa.columns))
# print(df_dsa["Valor_Venda"].describe())
# print(df_dsa["Valor_Venda"])
# print(df_dsa.Valor_Venda)
# print(df_dsa[df_dsa.duplicated()])
# print(df_dsa[df_dsa["Valor_Venda"] > 200.0])
# print(df_dsa.isnull().sum())

df_dsa_p1 = df_dsa[df_dsa["Categoria"] == "Office Supplies"]
# print(df_dsa_p1)
# print(df_dsa["Categoria"] == "Office Supplies")
df_dsa_p1_total = df_dsa_p1.groupby("Cidade")["Valor_Venda"].sum()
# print(df_dsa_p1_total)
# print(type(df_dsa_p1_total))
# print(df_dsa_p1.groupby("Cidade")[["Valor_Venda"]].sum())
# print(type(df_dsa_p1.groupby("Cidade")[["Valor_Venda"]].sum()))

















