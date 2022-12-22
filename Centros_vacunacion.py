import streamlit as st
import pandas as pd
from PIL import Image



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
        st.write('Fuente: https://www.datosabiertos.gob.pe/dataset/centros-de-vacunacion')
        st.write('')
        st.write('')
        st.write('###### Clic en la cabecera de columna para ordenar ascendente/descente')
        st.dataframe(df_cv)
else:
        df_filtrado = df_cv[df_cv['departamento'] == opc_dep]
        total = df_filtrado['id_centro_vacunacion'].count()
        st.write('Total de centros de vacunación: {}'.format(total))        
        st.map(df_filtrado)
        st.write('Fuente: https://www.datosabiertos.gob.pe/dataset/centros-de-vacunacion')
        st.write('')
        st.write('')
        st.write('###### Clic en la cabecera de columna para ordenar ascendente/descente')
        st.dataframe(df_filtrado)

st.write('### Centro de vacunación por departamento')        
barras_cv = df_cv.groupby(by=['departamento']).count()
barras_cv = barras_cv.drop(['id_ubigeo', 'nombre', 'lat', 'lon', 
                                'entidad_administra', 'id_eess'], axis=1)
barras_cv = barras_cv.rename(columns={'id_centro_vacunacion':'numero de centros de vacunacion'})
barras_cv = barras_cv.reset_index()
barras_cv = barras_cv.sort_values(by = 'numero de centros de vacunacion')

st.bar_chart(barras_cv, x = 'departamento', y = 'numero de centros de vacunacion')



