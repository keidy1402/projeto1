# ==========================================
# EXPLICAÇÃO COMPLETA DO CÓDIGO — BLOCO ÚNICO
# ==========================================

# Importa a biblioteca Streamlit, responsável pela criação da interface web interativa.
# O apelido "st" é utilizado para facilitar as chamadas da biblioteca ao longo do código.
import streamlit as st

# Importa a biblioteca Pandas, usada para estruturar dados em tabelas (DataFrames),
# o que facilita a visualização e manipulação de informações.
import pandas as pd


# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================

# Define configurações globais da aplicação web:
# - page_title: título da aba do navegador
# - page_icon: ícone exibido na aba
# - layout="wide": faz a aplicação ocupar mais largura da tela
st.set_page_config(
    page_title="Simulador de Rotina Ideal",
    page_icon="🌿",
    layout="wide"
)


# ==========================================
# ESTILO PERSONALIZADO
# ==========================================

# Injeta código CSS dentro da aplicação para personalização visual.
# O parâmetro unsafe_allow_html=True permite renderizar HTML/CSS no Streamlit.
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

# Exibe o título principal da aplicação.
st.title("🌿 Simulador de Rotina Ideal")

# Exibe subtítulo explicativo logo abaixo do título.
st.subheader("Sua rotina está te levando onde você quer chegar?")

# Insere uma linha horizontal para separação visual.
st.markdown("---")

# Texto introdutório orientando o usuário.
st.write("""
Preencha sua rotina diária para análise:
""")


# ==========================================
# INPUTS PRINCIPAIS
# ==========================================

# Título da seção onde o usuário informa sua rotina.
st.header("Conte para nós como é sua rotina diária:")

# Divide a interface em duas colunas para melhor organização visual.
col1, col2 = st.columns(2)


# Primeira coluna de inputs.
with col1:

    # Slider para horas de sono.
    # Intervalo permitido: 0 a 12 horas | Valor padrão: 7
    sono = st.slider("Horas de sono", 0, 12, 7)

    # Slider para horas de trabalho/estudo.
    trabalho = st.slider("Trabalho / Estudo", 0, 12, 6)

    # Slider para horas de lazer.
    lazer = st.slider("Lazer", 0, 10, 2)


# Segunda coluna de inputs.
with col2:

    # Slider para tempo diário dedicado à espiritualidade.
    tempo_com_Deus = st.slider("Tempo com Deus (minutos)", 0, 120, 15)

    # Slider para horas em redes sociais.
    tela = st.slider("Redes Sociais (horas)", 0, 10, 3)

    # Slider para frequência semanal de exercícios físicos.
    exercicio = st.slider("Prática de exercícios físicos (dias/semana)", 0, 7, 3)


# ==========================================
# INPUTS EXTRAS
# ==========================================

# Título da seção de hábitos e objetivos.
st.header("Hábitos e Objetivos")

# Menu suspenso para o usuário escolher seu principal objetivo atual.
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

# Checkbox indicando se o usuário faz leitura diária.
leitura = st.checkbox("Faço leitura diária")

# Checkbox indicando se o usuário planeja o dia antecipadamente.
planejamento = st.checkbox("Planejo meu dia com antecedência")

# Linha divisória.
st.markdown("---")


# ==========================================
# BOTÃO DE ANÁLISE
# ==========================================

# Toda a lógica abaixo será executada somente após clicar no botão.
if st.button("Analisar Minha Rotina"):

    # Inicializa variável de pontuação.
    score = 0

    # Cabeçalho da análise.
    st.header("Diagnóstico da Rotina")


    # ==========================================
    # ANÁLISE DO SONO
    # ==========================================
    if sono >= 7:
        st.success("✔️ Você está dormindo adequadamente.")
        score += 2
    else:
        st.warning("⚠️ Sono insuficiente pode prejudicar foco e saúde.")


    # ==========================================
    # ANÁLISE DE REDES SOCIAIS
    # ==========================================
    if tela <= 2:
        st.success("✔️ Uso saudável de redes sociais.")
        score += 2
    elif tela <= 4:
        st.info("ℹ️ Uso moderado de redes sociais.")
        score += 1
    else:
        st.error("🚨 Tempo excessivo em redes sociais.")


    # ==========================================
    # ANÁLISE ESPIRITUAL
    # ==========================================
    if tempo_com_Deus >= 20:
        st.success("🙏 Excelente prioridade espiritual.")
        score += 2
    elif tempo_com_Deus > 0:
        st.info("✨ Bom começo — tente aprofundar esse hábito.")
        score += 1
    else:
        st.warning("⚠️ Nenhum tempo espiritual registrado.")


    # ==========================================
    # ANÁLISE DE EXERCÍCIOS
    # ==========================================
    if exercicio >= 5:
        st.success("✔️ Você está cuidando muito bem da sua saúde!")
        score += 2
    elif exercicio >= 3:
        st.info("🏋️ Boa frequência de exercícios.")
        score += 1
    else:
        st.warning("⚠️ Está na hora de se atentar mais à sua saúde física.")


    # ==========================================
    # LEITURA DIÁRIA
    # ==========================================
    if leitura:
        st.success("Leitura diária fortalece aprendizado contínuo.")
        score += 1


    # ==========================================
    # PLANEJAMENTO DIÁRIO
    # ==========================================
    if planejamento:
        st.success("Planejamento diário aumenta consistência.")
        score += 1


    # ==========================================
    # VALIDAÇÃO DE HORAS TOTAIS
    # ==========================================
    total_horas = sono + trabalho + lazer + tela

    # Verifica se a soma das horas ultrapassa 24h.
    if total_horas > 24:
        st.error("Sua rotina ultrapassa 24h. Ajuste necessário.")
    else:
        score += 1


    # Linha divisória.
    st.markdown("---")


    # ==========================================
    # RESULTADO FINAL
    # ==========================================
    st.header("Resultado Final")

    # Classifica o usuário de acordo com sua pontuação.
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


    # Cria três colunas para exibir métricas visuais.
    col1, col2, col3 = st.columns(3)

    col1.metric("Score Final", score)
    col2.metric("Perfil", perfil)
    col3.metric("Chance de Sucesso", f"{chance}%")


    st.markdown("---")


    # ==========================================
    # VISUALIZAÇÃO DA ROTINA
    # ==========================================
    st.header("Visualização da Rotina")

    # Organiza os dados em DataFrame.
    dados = pd.DataFrame({
        "Horas": {
            "Sono": sono,
            "Trabalho/Estudo": trabalho,
            "Lazer": lazer,
            "Redes Sociais": tela
        }
    })

    # Exibe gráfico de barras automático do Streamlit.
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

    # Sugestões condicionais de melhoria.
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
    # Esta seção gera uma rotina recomendada com base
    # no objetivo escolhido e no perfil calculado.

    st.header("Sua Rotina Personalizada")

    # A estrutura abaixo compara objetivo + perfil
    # para selecionar a rotina mais adequada.

    # O código então monta uma lista de horários/tarefas
    # personalizada para o usuário.

    # Por fim:
    st.write(f"### Rotina sugerida para seu objetivo: **{objetivo}**")

    # Loop que exibe cada item da rotina sugerida.
    for item in rotina:
        st.write(f"• {item}")


    st.markdown("---")
