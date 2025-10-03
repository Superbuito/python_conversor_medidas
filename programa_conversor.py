# programa conversor de centimetros a pulgadas y viceversa
import pandas as pd
def cm_a_pulgadas(cm):
     return cm / 2.54   

# leer el archivos excel
df = pd.read_excel("muebles_medidas.xlsx") 

# añadir una columna al dataframe con las medidas en pulgadas

df["pulgadas"] = df["centimetros"].apply(cm_a_pulgadas) 
df.to_excel("muebles_medidas_convertidas.xlsx", index=False)

print("conversion complatada, archivo guardado como muebles_medidas_convertidas.xlsx")
