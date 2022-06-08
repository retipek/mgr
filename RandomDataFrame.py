import numpy as np
import pandas as pd
from datetime import datetime
import streamlit as st
import sqlite3

aktualnaData = datetime.now()                               #aktualna data
dzien=aktualnaData.strftime("%d")                           
miesiac=aktualnaData.strftime("%m")
rok=aktualnaData.strftime("%Y")
nazwaPliku=str('dane_'+rok+'-'+miesiac+'-'+dzien+'.csv')

#print(currentDay)
#print(currentMonth)
#print(currentYear)
#fileName='dane_'+cY+'-0'+cM+'-'+cD+'.csv'
#print(fileName)
#df=pd.DataFrame(np.random.rand(200, 2), columns=['Konduktancja','Temperatura'])
#print(df)
#df.to_csv(nazwaPliku,sep=';', index=False)

st.title('Test wizualizacji na wbe serwerze')
st.header('Aktualne wartości parametrów:')
#st.metric("Data",cY+'-0'+cM+'-'+cD+' '+cH+":"+cMin)
col1, col2 = st.columns(2)
col1.metric("Konduktancja", "123 μS/cm")
col2.metric("Temperatura", "22.3 °C")


data=pd.DataFrame
d = st.date_input(
     "Proszę wybrać datę, z której będą wizualizowane dane")
d2=str(d)
fileName2='dane_'+d2+'.csv'
print(fileName2)
#print(d2)

data=pd.read_csv(fileName2, delimiter=';')
print(data)
st.dataframe(data)
wynik=data.columns
st.line_chart(data['Konduktancja'])
#st.altair_chart(data['Konduktancja'])
st.line_chart(data['Temperatura'])

