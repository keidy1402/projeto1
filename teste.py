# ==========================================
# IMPORTAÇÃO DAS BIBLIOTECAS
# ==========================================
import streamlit as st
import pandas as pd


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
</style>
""", unsafe_allow_html=True)


# ==========================================
# CABEÇALHO PRINCIPAL
# ==========================================
st.title("🌿 Simulador de Rotina Ideal")
st.subheader("Sua rotina está te levando onde você quer chegar?")
st.markdown("---")

st.write("""
Preencha sua rotina diária para análise:
""")


# ==========================================
# INPUTS PRINCIPAIS
# ==========================================
st.header("Conte para nós como é sua rotina diária:")

col1, col2 = st.columns(2)

with col1:
    sono = st.slider("Horas de sono", 0, 12, 7)
    trabalho = st.slider("Trabalho / Estudo", 0, 12, 6)
    lazer = st.slider("Lazer", 0, 10, 2)

with col2:
    tempo_com_Deus = st.slider("Tempo com Deus (minutos)", 0, 120, 15)
    tela = st.slider("Redes Sociais (horas)", 0, 10, 3)
    exercicio = st.slider("Prática de exercícios físicos (dias/semana)", 0, 7, 3)


# ==========================================
# INPUTS EXTRAS
# ==========================================
st.header("Hábitos e Objetivos")

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

leitura = st.checkbox("Faço leitura diária")
planejamento = st.checkbox("Planejo meu dia com antecedência")

st.markdown("---")


# ==========================================
# BOTÃO DE ANÁLISE
# ==========================================
if st.button("Analisar Minha Rotina"):

    score = 0

    st.header("Diagnóstico da Rotina")

    # SONO
    if sono >= 7:
        st.success("✔️ Você está dormindo adequadamente.")
        score += 2
    else:
        st.warning("⚠️ Sono insuficiente pode prejudicar foco e saúde.")

    # REDES SOCIAIS
    if tela <= 2:
        st.success("✔️ Uso saudável de redes sociais.")
        score += 2
    elif tela <= 4:
        st.info("ℹ️ Uso moderado de redes sociais.")
        score += 1
    else:
        st.error("🚨 Tempo excessivo em redes sociais.")

    # VIDA ESPIRITUAL
    if tempo_com_Deus >= 20:
        st.success("🙏 Excelente prioridade espiritual.")
        score += 2
    elif tempo_com_Deus > 0:
        st.info("✨ Bom começo — tente aprofundar esse hábito.")
        score += 1
    else:
        st.warning("⚠️ Nenhum tempo espiritual registrado.")

    # EXERCÍCIO FÍSICO
    if exercicio >= 5:
        st.success("✔️ Você está cuidando muito bem da sua saúde!")
        score += 2
    elif exercicio >= 3:
        st.info("🏋️ Boa frequência de exercícios.")
        score += 1
    else:
        st.warning("⚠️ Está na hora de se atentar mais à sua saúde física.")

    # LEITURA
    if leitura:
        st.success("Leitura diária fortalece aprendizado contínuo.")
        score += 1

    # PLANEJAMENTO
    if planejamento:
        st.success("Planejamento diário aumenta consistência.")
        score += 1

    # VALIDAÇÃO DE HORAS
    total_horas = sono + trabalho + lazer + tela

    if total_horas > 24:
        st.error("Sua rotina ultrapassa 24h. Ajuste necessário.")
    else:
        score += 1

    st.markdown("---")


    # ==========================================
    # RESULTADO FINAL
    # ==========================================
    st.header("Resultado Final")

    if score >= 10:
        perfil = "Alta Performance"
        chance = 95
        st.success("Sua rotina está extremamente alinhada com alta performance.")

    elif score >= 6:
        perfil = "Em Evolução"
        chance = 75
        st.info("Sua rotina é boa, mas ainda possui oportunidades de melhoria.")

    else:
        perfil = "Desorganizada"
        chance = 40
        st.error("Sua rotina atual está desalinhada dos seus objetivos.")

    col1, col2, col3 = st.columns(3)

    col1.metric("Score Final", score)
    col2.metric("Perfil", perfil)
    col3.metric("Chance de Sucesso", f"{chance}%")

    st.markdown("---")


    # ==========================================
    # VISUALIZAÇÃO DA ROTINA
    # ==========================================
    st.header("Visualização da Rotina")

    dados = pd.DataFrame({
        "Horas": {
            "Sono": sono,
            "Trabalho/Estudo": trabalho,
            "Lazer": lazer,
            "Redes Sociais": tela
        }
    })

    st.bar_chart(dados)

    st.markdown("---")


    # ==========================================
    # PREVISÃO DE PERFORMANCE FUTURA
    # ==========================================
    st.header("Previsão de Performance Futura")

    st.write(f"""
    Com base nos seus hábitos atuais, estima-se aproximadamente:

    **{chance}% de probabilidade** de você manter consistência e atingir seu objetivo de **{objetivo.lower()}**.
    """)

    st.markdown("---")


    # ==========================================
    # PLANO DE MELHORIA
    # ==========================================
    st.header("Plano de Melhoria Personalizado")

    if sono < 7:
        st.write("→ Priorize dormir pelo menos 7 horas por noite.")

    if tela > 4:
        st.write("→ Reduza o tempo em redes sociais para no máximo 2 horas.")

    if tempo_com_Deus < 20:
        st.write("→ Amplie gradualmente seu tempo espiritual diário.")

    if exercicio < 3:
        st.write("→ Inclua exercícios físicos 3–5x por semana.")

    if not leitura:
        st.write("→ Comece com 10 páginas de leitura por dia.")

    if not planejamento:
        st.write("→ Reserve 5 minutos à noite para planejar o dia seguinte.")

    st.markdown("---")


    # ==========================================
    # ROTINA PERSONALIZADA
    # ==========================================
    st.header("Sua Rotina Personalizada")

    if objetivo == "Alta produtividade":

        if perfil == "Alta Performance":
            rotina = [
                "06:00 — Acordar",
                "06:15 — Exercício físico",
                "07:00 — Planejamento estratégico",
                "08:00–12:00 — Trabalho profundo / estudo",
                "14:00–18:00 — Execução de tarefas prioritárias",
                "21:00 — Revisão e planejamento do próximo dia"
            ]

        elif perfil == "Em Evolução":
            rotina = [
                "07:00 — Acordar",
                "07:30 — Organizar prioridades do dia",
                "08:00–11:00 — Bloco principal de foco",
                "14:00–17:00 — Tarefas secundárias",
                "20:30 — Revisão simples do dia"
            ]

        else:
            rotina = [
                "08:00 — Acordar em horário fixo",
                "08:30 — Escolher 3 prioridades do dia",
                "10:00 — Primeiro bloco de foco curto",
                "15:00 — Segundo bloco de foco",
                "20:00 — Preparação do dia seguinte"
            ]

    elif objetivo == "Equilíbrio emocional":

        if perfil == "Alta Performance":
            rotina = [
                "06:30 — Acordar com calma",
                "07:00 — Exercício / alongamento",
                "08:00 — Trabalho / estudo",
                "12:00 — Pausa real para almoço",
                "18:00 — Atividade relaxante",
                "21:00 — Desconexão digital"
            ]

        elif perfil == "Em Evolução":
            rotina = [
                "07:00 — Acordar sem pressa",
                "07:30 — Momento de autocuidado",
                "09:00 — Trabalho / estudo",
                "17:00 — Caminhada / lazer leve",
                "21:00 — Ritual de descanso"
            ]

        else:
            rotina = [
                "08:00 — Acordar em horário consistente",
                "08:30 — Alongamento / respiração",
                "10:00 — Atividade principal do dia",
                "18:00 — Tempo para descanso",
                "21:00 — Desligar telas"
            ]

    elif objetivo == "Crescimento espiritual":

        if perfil == "Alta Performance":
            rotina = [
                "05:30 — Devocional / oração",
                "06:15 — Leitura bíblica",
                "07:00 — Exercício / preparo do dia",
                "20:00 — Reflexão espiritual",
                "21:30 — Oração noturna"
            ]

        elif perfil == "Em Evolução":
            rotina = [
                "06:30 — Devocional matinal",
                "07:00 — Leitura bíblica",
                "19:00 — Reflexão sobre o dia",
                "21:00 — Oração noturna"
            ]

        else:
            rotina = [
                "07:30 — 10 min de oração",
                "08:00 — Versículo/reflexão do dia",
                "20:00 — Gratidão e oração"
            ]

    elif objetivo == "Performance acadêmica":

        if perfil == "Alta Performance":
            rotina = [
                "06:00 — Acordar",
                "06:30 — Revisão rápida",
                "08:00–12:00 — Estudo profundo",
                "14:00–17:00 — Exercícios / prática",
                "19:00 — Revisão espaçada"
            ]

        elif perfil == "Em Evolução":
            rotina = [
                "07:00 — Acordar",
                "08:00–10:00 — Bloco de estudo principal",
                "14:00–16:00 — Exercícios",
                "19:00 — Revisão leve"
            ]

        else:
            rotina = [
                "08:00 — Acordar",
                "09:00 — 1h de estudo focado",
                "15:00 — Exercícios práticos",
                "20:00 — Revisão rápida"
            ]

    else:  # Disciplina pessoal

        if perfil == "Alta Performance":
            rotina = [
                "05:30 — Acordar",
                "06:00 — Exercício físico",
                "07:00 — Organização do dia",
                "08:00–18:00 — Execução disciplinada",
                "21:00 — Planejamento do dia seguinte"
            ]

        elif perfil == "Em Evolução":
            rotina = [
                "06:30 — Acordar",
                "07:00 — Checklist matinal",
                "08:00–17:00 — Blocos de execução",
                "20:30 — Revisão do dia"
            ]

        else:
            rotina = [
                "08:00 — Acordar em horário fixo",
                "08:30 — Fazer a cama / rotina matinal",
                "10:00 — Primeira tarefa importante",
                "20:00 — Planejar amanhã"
            ]

    st.write(f"### Rotina sugerida para seu objetivo: **{objetivo}**")

    for item in rotina:
        st.write(f"• {item}")

    st.markdown("---")
