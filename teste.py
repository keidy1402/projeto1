import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Simulador de Rotina Ideal",
    page_icon="🌿",
    layout="wide"
)

# ==========================================
# ESTILO PERSONALIZADO
# ==========================================
st.markdown("""
<style>
.main {
    background-color: #f8f9fa;
}
h1, h2, h3 {
    color: #2c3e50;
}
.stMetric {
    background-color: #ffffff;
    padding: 10px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# CABEÇALHO
# ==========================================
st.title("🌿 Simulador de Rotina Ideal")
st.subheader("Sua rotina está te levando para onde você quer?")
st.markdown("---")

st.write("""
Preencha sua rotina diária e receba:

- 📊 Diagnóstico completo
- 📈 Visualizações gráficas
- 🤖 Previsão de performance futura
- 🧭 Plano de melhoria personalizado
""")

# ==========================================
# INPUTS PRINCIPAIS
# ==========================================
st.header("⏰ Monte sua rotina diária")

col1, col2 = st.columns(2)

with col1:
    sono = st.slider("🛌 Horas de sono", 0, 12, 7)
    trabalho = st.slider("📚 Trabalho / Estudo", 0, 12, 6)
    lazer = st.slider("🎮 Lazer", 0, 10, 2)

with col2:
    tempo_com_Deus = st.slider("🙏 Tempo com Deus (minutos)", 0, 120, 15)
    tela = st.slider("📱 Redes Sociais (horas)", 0, 10, 3)
    exercicio = st.checkbox("🏋️ Pratico exercícios físicos")

# ==========================================
# INPUTS EXTRAS
# ==========================================
st.header("🎯 Hábitos e Objetivos")

objetivo = st.selectbox(
    "Qual seu principal objetivo atual?",
    [
        "Alta produtividade",
        "Equilíbrio emocional",
        "Crescimento espiritual",
        "Performance acadêmica",
        "Disciplina pessoal"
    ]
)

leitura = st.checkbox("📚 Faço leitura diária")
planejamento = st.checkbox("📝 Planejo meu dia com antecedência")

st.markdown("---")

# ==========================================
# BOTÃO DE ANÁLISE
# ==========================================
if st.button("🔍 Analisar Minha Rotina"):

    score = 0

    st.header("📊 Diagnóstico da Rotina")

    # ------------------------
    # ANÁLISE SONO
    # ------------------------
    if sono >= 7:
        st.success("✔️ Você está dormindo adequadamente.")
        score += 2
    else:
        st.warning("⚠️ Sono insuficiente pode prejudicar foco e saúde.")

    # ------------------------
    # REDES SOCIAIS
    # ------------------------
    if tela <= 2:
        st.success("✔️ Uso saudável de redes sociais.")
        score += 2
    elif tela <= 4:
        st.info("ℹ️ Uso moderado de redes sociais.")
        score += 1
    else:
        st.error("🚨 Tempo excessivo em redes sociais.")

    # ------------------------
    # VIDA ESPIRITUAL
    # ------------------------
    if tempo_com_Deus >= 20:
        st.success("🙏 Excelente prioridade espiritual.")
        score += 2
    elif tempo_com_Deus > 0:
        st.info("✨ Bom começo — tente aprofundar esse hábito.")
        score += 1
    else:
        st.warning("⚠️ Nenhum tempo espiritual registrado.")

    # ------------------------
    # EXERCÍCIO
    # ------------------------
    if exercicio:
        st.success("🏋️ Exercício físico contribui para performance e saúde.")
        score += 1

    # ------------------------
    # LEITURA
    # ------------------------
    if leitura:
        st.success("📚 Leitura diária fortalece aprendizado contínuo.")
        score += 1

    # ------------------------
    # PLANEJAMENTO
    # ------------------------
    if planejamento:
        st.success("📝 Planejamento diário aumenta consistência.")
        score += 1

    # ------------------------
    # TOTAL DE HORAS
    # ------------------------
    total_horas = sono + trabalho + lazer + tela

    if total_horas > 24:
        st.error("🚨 Sua rotina ultrapassa 24h. Ajuste necessário.")
    else:
        score += 1

    st.markdown("---")

    # ==========================================
    # RESULTADO FINAL
    # ==========================================
    st.header("🎯 Resultado Final")

    if score >= 9:
        perfil = "Alta Performance"
        chance = 95
        st.success("🔥 Sua rotina está extremamente alinhada com alta performance.")
    elif score >= 6:
        perfil = "Em Evolução"
        chance = 75
        st.info("⚖️ Sua rotina é boa, mas ainda possui oportunidades de melhoria.")
    else:
        perfil = "Desorganizada"
        chance = 40
        st.error("🚨 Sua rotina atual está desalinhada dos seus objetivos.")

    col1, col2, col3 = st.columns(3)

    col1.metric("Score Final", score)
    col2.metric("Perfil", perfil)
    col3.metric("Chance de Sucesso", f"{chance}%")

    st.markdown("---")

    # ==========================================
    # DATAFRAME
    # ==========================================
    dados = pd.DataFrame({
        "Categoria": [
            "Sono",
            "Trabalho/Estudo",
            "Lazer",
            "Redes Sociais"
        ],
        "Horas": [
            sono,
            trabalho,
            lazer,
            tela
        ]
    })

    # ==========================================
    # GRÁFICO PLOTLY
    # ==========================================
    st.header("📈 Visualização Interativa da Rotina")

    fig_pie = px.pie(
        dados,
        names="Categoria",
        values="Horas",
        title="Distribuição da Rotina Diária",
        hole=0.4
    )

    st.plotly_chart(fig_pie, use_container_width=True)

    # ==========================================
    # GRÁFICO MATPLOTLIB
    # ==========================================
    st.header("📊 Comparativo em Barras")

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(dados["Categoria"], dados["Horas"])
    ax.set_ylabel("Horas")
    ax.set_title("Horas por Categoria")

    st.pyplot(fig)

    st.markdown("---")

    # ==========================================
    # SIMULAÇÃO DE MACHINE LEARNING
    # ==========================================
    st.header("🤖 Previsão de Performance Futura")

    st.write(f"""
    Com base nos seus hábitos atuais, um modelo preditivo estimaria aproximadamente:

    **{chance}% de probabilidade** de você manter consistência e atingir seu objetivo de **{objetivo.lower()}**.
    """)

    st.caption("⚠️ Atualmente esta previsão é simulada com base em regras heurísticas e pode ser substituída por modelo de Machine Learning real futuramente.")

    st.markdown("---")

    # ==========================================
    # PLANO PERSONALIZADO
    # ==========================================
    st.header("🧭 Plano de Melhoria Personalizado")

    if sono < 7:
        st.write("→ Priorize dormir pelo menos 7 horas por noite.")

    if tela > 4:
        st.write("→ Reduza o tempo em redes sociais para no máximo 2 horas.")

    if tempo_com_Deus < 20:
        st.write("→ Amplie gradualmente seu tempo espiritual diário.")

    if not exercicio:
        st.write("→ Inclua exercícios físicos 3–5x por semana.")

    if not leitura:
        st.write("→ Comece com 10 páginas de leitura por dia.")

    if not planejamento:
        st.write("→ Reserve 5 minutos à noite para planejar o dia seguinte.")

    st.markdown("---")

    # ==========================================
    # FRASE FINAL
    # ==========================================
    st.subheader("💭 Reflexão Final")

    st.write("""
    **Sua rotina atual está construindo a vida que você diz querer?**

    Pequenas escolhas diárias criam grandes resultados ao longo do tempo.
    """)
