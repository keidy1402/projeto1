Importa a biblioteca principal do Streamlit para criar a interface web 

import streamlit as st 

Importa o Pandas para manipular e estruturar dados em tabelas/dataframes 

import pandas as pd 

========================================== 

CONFIGURAÇÃO DA PÁGINA 

Define título, ícone e layout da aplicação web 

========================================== 

st.set_page_config( page_title="Simulador de Rotina Ideal", page_icon="🌿", layout="wide" ) 

========================================== 

ESTILO PERSONALIZADO (CSS) 

Permite customizar visualmente o app usando CSS 

unsafe_allow_html=True permite renderizar HTML/CSS 

========================================== 

st.markdown(""" 

""", unsafe_allow_html=True) 

========================================== 

CABEÇALHO PRINCIPAL 

Título e subtítulo da aplicação 

========================================== 

st.title("🌿 Simulador de Rotina Ideal") st.subheader("Sua rotina está te levando onde você quer chegar?") st.markdown("---") 

Texto explicativo introdutório para o usuário 

st.write(""" Preencha sua rotina diária para análise: 

“””) 

========================================== 

INPUTS PRINCIPAIS 

Área onde o usuário informa sua rotina diária 

========================================== 

st.header("⏰ Conte para nós como é sua rotina diária:") 

Divide a tela em duas colunas para melhor organização visual 

col1, col2 = st.columns(2) 

Primeira coluna com sliders 

with col1: 

# Slider para horas de sono (0 a 12 horas) 
sono = st.slider("🛌 Horas de sono", 0, 12, 7) 
 
# Slider para horas de trabalho/estudo 
trabalho = st.slider("📚 Trabalho / Estudo", 0, 12, 6) 
 
# Slider para horas de lazer 
lazer = st.slider("🎮 Lazer", 0, 10, 2) 
 

Segunda coluna com mais inputs 

with col2: 

# Slider para tempo espiritual diário em minutos 
tempo_com_Deus = st.slider("🙏 Tempo com Deus (minutos)", 0, 120, 15) 
 
# Slider para tempo em redes sociais 
tela = st.slider("📱 Redes Sociais (horas)", 0, 10, 3) 
 
# Slider para marcar prática de exercícios físicos 
exercicio = st.slider("🏋️ Prática de exercícios físicos (dias)”, 0, 7, 5)  
 

========================================== 

INPUTS EXTRAS 

Informações complementares sobre hábitos e objetivos 

========================================== 

st.header("🎯 Hábitos e Objetivos") 

Menu dropdown para selecionar objetivo principal 

objetivo = st.selectbox( "Qual seu principal objetivo atual?", [ "Alta produtividade", "Equilíbrio emocional", "Crescimento espiritual", "Performance acadêmica", "Disciplina pessoal" ] ) 

Checkbox para leitura diária 

leitura = st.checkbox("📚 Faço leitura diária") 

Checkbox para planejamento diário 

planejamento = st.checkbox("📝 Planejo meu dia com antecedência") 

st.markdown("---") 

========================================== 

BOTÃO DE ANÁLISE 

Toda a lógica abaixo só roda quando o botão é clicado 

========================================== 

if st.button("🔍 Analisar Minha Rotina"): 

# Variável de pontuação para avaliar a rotina 
score = 0 
 
st.header("Diagnóstico da Rotina") 
 
 
# ========================================== 
# ANÁLISE DO SONO 
# Se usuário dorme 7h ou mais, ganha pontos 
# ========================================== 
if sono >= 7: 

   st.success("✔️ Você está dormindo adequadamente.") 
   score += 2 
else: 
   st.warning("⚠️ Sono insuficiente pode prejudicar foco e saúde.") 
 
 
# ========================================== 
# ANÁLISE DE REDES SOCIAIS 
# Quanto menor o tempo, melhor a pontuação 
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
# Avalia prioridade dada ao tempo com Deus 
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
# EXERCÍCIO FÍSICO 
# Adiciona ponto se pratica exercício 
# ========================================== 
if exercicio: 
   if exercicio>= 5: 
   st.success("✔️ Você está cuidando da sua saúde!") 
   score += 2 
else: 
   st.warning("⚠️Está na hora de se atentar para sua saúde.") 
 
 
# Leitura diária adiciona ponto 
if leitura: 
   st.success("📚 Leitura diária fortalece aprendizado contínuo.") 
   score += 1 
 
 
# Planejamento diário adiciona ponto 
if planejamento: 
   st.success("📝 Planejamento diário aumenta consistência.") 
   score += 1 
 
 
# ========================================== 
# VALIDAÇÃO DE TOTAL DE HORAS 
# Verifica se rotina ultrapassa 24h 
# ========================================== 
total_horas = sono + trabalho + lazer + tela 
 
if total_horas > 24: 
   st.error("🚨 Sua rotina ultrapassa 24h. Ajuste necessário.") 
else: 
   score += 1 
 
st.markdown("---") 
 
 
# ========================================== 
# RESULTADO FINAL 
# Define perfil do usuário com base no score 
# ========================================== 
st.header("🎯 Resultado Final") 
 
if score >= 10: 
   perfil = "Alta Performance" 
   chance = 95 
   st.success("🔥 Sua rotina está extremamente alinhada com alta performance.") 
 
elif score >= 5: 
   perfil = "Em Evolução" 
   chance = 75 
   st.info("⚖️ Sua rotina é boa, mas ainda possui oportunidades de melhoria.") 
 
else: 
   perfil = "Desorganizada" 
   chance = 40 
   st.error("🚨 Sua rotina atual está desalinhada dos seus objetivos.") 
 
 
# Exibe métricas principais 
col1, col2, col3 = st.columns(3) 
 
col1.metric("Score Final", score) 
col2.metric("Perfil", perfil) 
col3.metric("Chance de Sucesso", f"{chance}%") 
 
st.markdown("---") 
 
 
# ========================================== 
# VISUALIZAÇÃO DOS DADOS 
# Cria DataFrame para gerar gráfico 
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
 
 
# Gráfico de barras nativo do Streamlit 
st.bar_chart(dados) 
 
st.markdown("---") 
 
 
# ========================================== 
# PREVISÃO DE PERFORMANCE FUTURA 
# Usa chance calculada heurísticamente 
# ========================================== 
st.header("🤖 Previsão de Performance Futura") 
 
st.write(f""" 
Com base nos seus hábitos atuais, estima-se aproximadamente: 
 
**{chance}% de probabilidade** de você manter consistência e atingir seu objetivo de **{objetivo.lower()}**. 
""") 
 
 
st.markdown("---") 
 
 
# ========================================== 
# PLANO DE MELHORIA PERSONALIZADO 
# Sugere ajustes com base nas respostas 
# ========================================== 
st.header("Plano de Melhoria Personalizado") 
 
if sono < 7: 
   st.write("→ Priorize dormir pelo menos 7 horas por noite.") 
 
if tela > 4: 
   st.write("→ Reduza o tempo em redes sociais para no máximo 2 horas.") 
 
if tempo_com_Deus < 20: 
   st.write("→ Amplie gradualmente seu tempo espiritual diário.") 
 
if exercicio < 5: 
   st.write("→ Inclua exercícios físicos 3–5x por semana.") 
 
if not leitura: 
   st.write("→ Comece com 10 páginas de leitura por dia.") 
 
if not planejamento: 
   st.write("→ Reserve 5 minutos à noite para planejar o dia seguinte.") 
 
st.markdown("---") 
 
 
# ========================================== 
# MENSAGEM FINAL REFLEXIVA 
# ========================================== 
st.subheader("Agora pense sobre a sua rotina e no seu objetivo com ela") 
 
st.write(""" 
**Sua rotina atual está construindo a vida que você diz querer?** 
 
Pequenas escolhas diárias criam grandes resultados ao longo do tempo. Aqui está uma rotina personalizada para você com base no seu objetivo:  
""") 
 
