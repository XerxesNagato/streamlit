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
dis_btn = st.sidebar.button(f'''
<a href={dis_link}><button style="background-color:blue;">Discord</button></a>
''',
unsafe_allow_html=True))
# if dis_btn:
#         st.markdown(f'''
# <a href={dis_link}><button style="background-color:GreenYellow;">Discord</button></a>
# ''',
# unsafe_allow_html=True)

st.sidebar.header('Members:')
st.sidebar.write('Nagat__0#')
st.sidebar.write('Wahio')
st.sidebar.write('BloodyShirou')
st.sidebar.write('Frost')
st.sidebar.write('Kail0o#')
st.sidebar.write('Silver')
