import streamlit as st
import requests
import webbrowser


st.set_page_config(
        page_title="DaSquad",
        page_icon="logo.png",
        layout="wide")
dis_link = 'https://discord.gg/v3FDUQ5t'

st.header('The Squad')
#st.image('logo.png')
dis_btn = st.button('Discord')
if dis_btn:
    webbrowser.open_new_tab(dis_link)

st.header('Members:')
st.write('Nagat__0#')
st.write('Wahio')
st.write('BloodyShirou')
st.write('Frost')
st.write('Kail0o#')
st.write('Silver')
