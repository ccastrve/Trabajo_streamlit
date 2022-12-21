import streamlit as st
import pandas as pd
import numpy as np


st.title('Centros de Vacunación COVID-19')
st.write('#### Se muestran los centros de vacunación programados según ubicación geográfica \
        a nivel nacional del territorio peruano')

df_cv = pd.read_csv('CV_depurado.csv')
df_de = pd.read_csv('departamentos.csv')

opc_dep = st.selectbox('Seleccione departamento',
        df_de['departamento'])

if (opc_dep == 'TODOS'):
        total = df_cv['id_centro_vacunacion'].count()
        st.write('Total de centros de vacunación: {}'.format(total))        
        st.map(df_cv)
else:
        df_filtrado = df_cv[df_cv['departamento'] == opc_dep]
        total = df_filtrado['id_centro_vacunacion'].count()
        st.write('Total de centros de vacunación: {}'.format(total))        
        st.map(df_filtrado)


