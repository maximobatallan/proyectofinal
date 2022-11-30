import streamlit as st
import pandas as pd


def estadia():
    huesped = pd.read_csv('huespedes.csv')

    col_list = huesped[huesped.columns[0]].values.tolist()


    tupla = tuple(col_list)

    option = st.selectbox(
        'Ingresa tu Nombre:',
    tupla, key="name")

    if st.checkbox('¡No encuentro mi nombre!'):
        st.text_input("Ingresa tu nombre", key="name1")
        nombre1 = st.session_state.name1
        
       
    col0,col1, col2, col3, col4 = st.columns(5)
    miercoles = False
    jueves = False
    viernes = False
    sabado = False
    domingo = False



    with col0:
        st.header("Mie")
        if st.checkbox('7/12'):
            miercoles = True

    with col1:
        st.header("Jue")
        if st.checkbox('8/12'):
            jueves = True

    with col2:
        st.header("Vie")
        if st.checkbox('9/12'):
            viernes = True 
    with col3:
        st.header("Sab")
        if st.checkbox('10/12'):
            sabado = True
    with col4:
        st.header("Dom")
        if st.checkbox('11/12'):
            domingo = True

        


    df = pd.read_csv('huespedes.csv')

            

    try:
        nombre = st.session_state.name1
    except:
        nombre = st.session_state.name
    

    nombre = nombre.upper()
    

    df1 =df.drop(df.index[0])

    if nombre == "":
        st.write('¡Seleccione su Nombre!')
        pass
    else:
        if nombre == "SELECCIONE UN NOMBRE":
            st.write('¡Seleccione su Nombre!')
            pass
        else:
            
            if st.button('Guardar'):
                if miercoles == True:
                    df.loc[df['Nombre'] == nombre, 'Miercoles'] = 'Si'
                else:
                    df.loc[df['Nombre'] == nombre, 'Miercoles'] = 'No'
                if jueves == True:
                    df.loc[df['Nombre'] == nombre, 'Jueves'] = 'Si'
                else:
                    df.loc[df['Nombre'] == nombre, 'Jueves'] = 'No'
                if viernes == True:
                    df.loc[df['Nombre'] == nombre, 'Viernes'] = 'Si'
                else:
                    df.loc[df['Nombre'] == nombre, 'Viernes'] = 'No'    
                if sabado == True:
                    df.loc[df['Nombre'] == nombre, 'Sabado'] = 'Si'
                else:
                    df.loc[df['Nombre'] == nombre, 'Sabado'] = 'No'               
                if domingo == True:
                    df.loc[df['Nombre'] == nombre, 'Domingo'] = 'Si'
                else:
                    df.loc[df['Nombre'] == nombre, 'Domingo'] = 'No'

                
                df.to_csv('huespedes.csv',index=False)
                df1 = df[df['Nombre'] == nombre]
                st.dataframe(df1)












