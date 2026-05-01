import streamlit as st
import pandas as pd

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Simulador de Rotina Ideal",
    page_icon="🌿",
    layout="centered"
)

# ESTILO
st.markdown("""
    <style>
    .main {
        background-color: #f7f7f7;
    }
    h1 {
        color: #2c3e50;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# TÍTULO
st.markdown("# 🌿 Simulador de Rotina Ideal")
st.markdown("### Sua rotina está te levando para onde você quer?")

st.markdown("---")

# INTRO
st.write("Responda com sinceridade. No final, você vai receber uma análise completa da sua rotina.")

# INPUTS
st.subheader("⏰ Monte sua rotina diária")

sono = st.slider("🛌 Horas de sono", 0, 12, 7)
trabalho = st.slider("📚 Trabalho / Estudo", 0, 12, 6)
lazer = st.slider("🎮 Lazer", 0, 10, 2)
tempo_com_Deus = st.slider("🙏 Tempo com Deus (minutos)", 0, 120, 10)
tela = st.slider("📱 Tempo em redes sociais (horas)", 0, 10, 3)

st.markdown("---")

# BOTÃO
if st.button("🔍 Analisar minha rotina"):

    st.subheader("📊 Análise da sua rotina")

    score = 0

    # ANÁLISE SONO
    if sono >= 7:
        st.success("✔️ Você está dormindo bem.")
        score += 2
    else:
        st.warning("⚠️ Poucas horas de sono — isso afeta foco, humor e saúde.")

    # ANÁLISE REDES SOCIAIS
    if tela > 4:
        st.error("🚨 Muito tempo em redes sociais — isso está roubando sua produtividade.")
    else:
        score += 1

    # ANÁLISE ESPIRITUAL
    if tempo_com_Deus >= 20:
        st.success("🙏 Você está priorizando sua vida espiritual.")
        score += 2
    elif tempo_com_Deus > 0:
        st.info("✨ Você começou — agora tente aumentar esse tempo.")
        score += 1
    else:
        st.warning("⚠️ Falta tempo com Deus na sua rotina.")

    # EQUILÍBRIO GERAL
    total_horas = sono + trabalho + lazer + tela

    if total_horas > 24:
        st.error("🚨 Sua rotina ultrapassa 24h — algo está fora da realidade.")
    else:
        score += 1

    st.markdown("---")

    # RESULTADO FINAL
    st.subheader("🎯 Resultado Final")

    if score >= 6:
        st.success("🔥 Rotina alinhada com seus objetivos!")
        perfil = "Produtiva e Equilibrada"
    elif score >= 4:
        st.info("⚖️ Boa rotina, mas com ajustes necessários.")
        perfil = "Em desenvolvimento"
    else:
        st.error("🚨 Sua rotina não está te levando para onde você quer.")
        perfil = "Desorganizada"

    st.write(f"**Seu perfil:** {perfil}")

    st.markdown("---")

    # GRÁFICO
    dados = pd.DataFrame({
        "Categoria": ["Sono", "Trabalho/Estudo", "Lazer", "Redes Sociais"],
        "Horas": [sono, trabalho, lazer, tela]
    })

    st.subheader("📈 Visual da sua rotina")
    st.bar_chart(dados.set_index("Categoria"))

    st.markdown("---")

    # PLANO DE MELHORIA
    st.subheader("🧭 Plano de melhoria personalizado")

    if sono < 7:
        st.write("→ Ajuste seu horário para dormir mais cedo.")

    if tela > 4:
        st.write("→ Reduza o tempo em redes sociais para até 2h/dia.")

    if tempo_com_Deus < 20:
        st.write("→ Separe pelo menos 10–20 minutos com Deus diariamente.")

    if lazer == 0:
        st.write("→ Inclua momentos de descanso — isso também é produtividade.")

    st.markdown("---")

    # FRASE FINAL
    st.markdown("### 💭 Reflexão final")
    st.write("Sua rotina atual está criando a vida que você diz que quer?")
