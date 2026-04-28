import streamlit as st

st.title ('Teste ECMI 2')
st.write("Esse é o meu texto")
import streamlit as st
from PIL import Image

# Carregar imagem local
try:
    image = Image.open("https://github.com/keidy1402/projeto1/blob/main/au%20au%20fofinho.jpg")  
    st.image(image, caption="Minha Imagem Local", use_column_width=True)
except FileNotFoundError:
    st.error("Imagem não encontrada. Verifique o caminho do arquivo.")
