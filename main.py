import streamlit as st
from Adress.Adress import *
import base64



street_name = st.text_input("Give street name:") 

house_nr = st.text_input("give house number:")
postcode = st.text_input("give postcode: ")

if postcode:
    adress1 = Adress(street_name,house_nr,postcode)

    adress1.open_adress_tiff_url()

    adress1.read_adress_tiff()
    
    file_ = open("Assets/cat-typing.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    placeholder = st.empty()
    placeholder2 = st.empty()
    placeholder.text("Calculating chm, It may take about 6 minutes in the meantime enjoy this cat gif")
    cat_html =  f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">'
    placeholder2.markdown(cat_html,unsafe_allow_html=True)
    
    adress1.calculate_chm()
    
    placeholder2.empty()
    placeholder.empty()
    st.write("\n")
    st.write(adress1.get_chm())

    st.pyplot(adress1.plot_3d())
    st.plotly_chart(adress1.go_plot())