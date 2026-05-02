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

📊 Diagnóstico completo  
📈 Visualização da rotina  
🤖 Previsão de performance futura  
🧭 Plano de melhoria personalizado  
📅 Rotina adaptativa baseada no seu perfil
""")


# ==========================================
# INPUTS PRINCIPAIS
# ==========================================
st.header("⏰ Conte para nós como é sua rotina diária:")

col1, col2 = st.columns(2)

with col1:
    sono = st.slider("🛌 Horas de sono", 0, 12, 7)
    trabalho = st.slider("📚 Trabalho / Estudo", 0, 12, 6)
    lazer = st.slider("🎮 Lazer", 0, 10, 2)

with col2:
    tempo_com_Deus = st.slider("🙏 Tempo com Deus (minutos)", 0, 120, 15)
    tela = st.slider("📱 Redes Sociais (horas)", 0, 10, 3)
    exercicio = st.slider("🏋️ Prática de exercícios físicos (dias/semana)", 0, 7, 3)


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
        st.success("📚 Leitura diária fortalece aprendizado contínuo.")
        score += 1

    # PLANEJAMENTO
    if planejamento:
        st.success("📝 Planejamento diário aumenta consistência.")
        score += 1

    # VALIDAÇÃO DE HORAS
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

    if score >= 10:
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
    # VISUALIZAÇÃO DA ROTINA
    # ==========================================
    st.header("📈 Visualização da Rotina")

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
    st.header("🤖 Previsão de Performance Futura")

    st.write(f"""
    Com base nos seus hábitos atuais, estima-se aproximadamente:

    **{chance}% de probabilidade** de você manter consistência e atingir seu objetivo de **{objetivo.lower()}**.
    """)

    st.markdown("---")


    # ==========================================
    # PLANO DE MELHORIA
    # ==========================================
    st.header("🧭 Plano de Melhoria Personalizado")

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
    # ROTINA PERSONALIZADA ADAPTATIVA
    # ==========================================
    st.header("📅 Rotina Personalizada para Seu Momento Atual")

    # Base pelo objetivo
    if objetivo == "Alta produtividade":
        rotina_base = [
            "Blocos de trabalho profundo pela manhã",
            "Planejamento diário estruturado",
            "Sessões de revisão no fim do dia"
        ]

    elif objetivo == "Equilíbrio emocional":
        rotina_base = [
            "Momentos de pausa entre atividades",
            "Desconexão digital noturna",
            "Tempo reservado para autocuidado"
        ]

    elif objetivo == "Crescimento espiritual":
        rotina_base = [
            "Devocional pela manhã",
            "Leitura espiritual diária",
            "Reflexão/oração ao fim do dia"
        ]

    elif objetivo == "Performance acadêmica":
        rotina_base = [
            "Blocos intensos de estudo",
            "Sessões de exercícios e revisão",
            "Revisão espaçada noturna"
        ]

    else:
        rotina_base = [
            "Horário fixo para acordar",
            "Checklist diário de tarefas",
            "Planejamento da noite anterior"
        ]


    # Adaptação pelo perfil
    if perfil == "Alta Performance":
        adaptacao = [
            "06:00 — Acordar",
            "06:15 — Exercício físico",
            "07:00 — Execução estratégica de alta prioridade",
            "21:00 — Revisão e planejamento avançado"
        ]

    elif perfil == "Em Evolução":
        adaptacao = [
            "07:00 — Acordar",
            "07:30 — Organizar prioridades do dia",
            "08:00 — Bloco principal de foco",
            "20:30 — Revisão simples do dia"
        ]

    else:
        adaptacao = [
            "08:00 — Acordar em horário consistente",
            "08:30 — Escolher 3 prioridades do dia",
            "10:00 — Primeiro bloco de foco curto",
            "20:00 — Preparação do dia seguinte"
        ]


    st.write(f"### Rotina sugerida para quem busca **{objetivo.lower()}** e está no perfil **{perfil}**:")

    st.markdown("#### Estrutura Estratégica")
    for item in adaptacao:
        st.write(f"• {item}")

    st.markdown("#### Hábitos Prioritários Para Seu Objetivo")
    for item in rotina_base:
        st.write(f"• {item}")

    st.markdown("---")


    # ==========================================
    # REFLEXÃO FINAL
    # ==========================================
    st.subheader("💭 Agora pense sobre a sua rotina e no seu objetivo com ela")

    st.write("""
    **Sua rotina atual está construindo a vida que você diz querer?**

    Pequenas escolhas diárias criam grandes resultados ao longo do tempo.
    """)
