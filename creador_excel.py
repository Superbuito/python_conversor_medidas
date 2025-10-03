import pandas as pd
#dataframe es la informacion  b'asica con el nombre de las piezas y centimetros para poder armar excel

data = {
    "pieza": ["Pata", "Tablero ","Puerta", "Estante", "Panel lateral"],
    "centimetros": [40, 120, 60, 30,80]
}

df= pd.DataFrame(data)

#se guarda el dataframe en un archivo excel
df.to_excel("muebles_medidas.xlsx", index=False)


