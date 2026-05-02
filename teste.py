# ==========================================
# ROTINA PERSONALIZADA ADAPTATIVA
# ==========================================
st.header("📅 Rotina Personalizada para Seu Momento Atual")

# Base da rotina conforme objetivo
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

else:  # Disciplina pessoal
    rotina_base = [
        "Horário fixo para acordar",
        "Checklist diário de tarefas",
        "Planejamento da noite anterior"
    ]


# Ajuste conforme score/perfil
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

else:  # Desorganizada
    adaptacao = [
        "08:00 — Acordar em horário consistente",
        "08:30 — Escolher 3 prioridades do dia",
        "10:00 — Primeiro bloco de foco curto",
        "20:00 — Preparação do dia seguinte"
    ]


# Exibição da rotina
st.write(f"### Rotina sugerida para quem busca **{objetivo.lower()}** e está no perfil **{perfil}**:")

st.markdown("#### Estrutura Estratégica")
for item in adaptacao:
    st.write(f"• {item}")

st.markdown("#### Hábitos Prioritários Para Seu Objetivo")
for item in rotina_base:
    st.write(f"• {item}")
