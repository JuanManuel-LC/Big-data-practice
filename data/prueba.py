import pandas as pd

df = pd.read_csv("./data/01_datos_control_calidad_piezas.csv", encoding="latin-1")

print(df.head())
print(df.nunique())