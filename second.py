import streamlit as st
import requests
import webbrowser
import subprocess


st.set_page_config(
        page_title="DaSquad",
        page_icon="logo.png",
        layout="wide")
dis_link = 'https://discord.gg/v3FDUQ5t'

st.header('The Squad')
#st.image('logo.png')
dis_btn = st.sidebar.button('[Discord]('https://discord.gg/v3FDUQ5t'))
if dis_btn:
    #webbrowser.open_new_tab(dis_link)
    "check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")

st.sidebar.header('Members:')
st.sidebar.write('Nagat__0#')
st.sidebar.write('Wahio')
st.sidebar.write('BloodyShirou')
st.sidebar.write('Frost')
st.sidebar.write('Kail0o#')
st.sidebar.write('Silver')
