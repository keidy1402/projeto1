import streamlit as st

st.title ('Teste ECMI 2')
st.write("Esse é o meu texto")
import streamlit as st
from PIL import Image

# Título do app
st.title("Exemplo de Exibição de Imagem no Streamlit")

# Carregar imagem local
try:
    image = Image.open("minha_imagem.jpg")  # Substitua pelo caminho da sua imagem
    st.image(image, caption="Minha Imagem Local", use_column_width=True)
except FileNotFoundError:
    st.error("Imagem não encontrada. Verifique o caminho do arquivo.")

# Exibir imagem a partir de uma URL
url = "https://via.placeholder.com/300"
st.image(url, caption="Imagem de URL", use_column_width=True)
