import streamlit as st

st.set_page_config(page_title="Regulamento ATP Península", layout="wide")

params = st.experimental_get_query_params()
if "page" in params:
    page_selected = params["page"][0]
    

pages = ["Capa", "Contracapa", "Mensagem da Diretoria", "Cronograma", "Inscrições", "Início do Campeonato", "Critério de Pontuação", "Campeonato de Duplas", "Reserva de Quadras", "Regra do Desafiante e Desafiado", "Tolerância de Tempo", "Solicitação de Ausência", "Desistência/Abandono", "Regra do Jogador que Ausenta do Torneio", "Falta de Energia ou Chuva Durante o Jogo", "Ranking", "Premiação", "Confraternização", "Funções do Presidente e Vice", "Funções do Conselho", "Regras do Grupo do Whatsapp", "Disposições Gerais", "Histórico 1", "Histórico 2", "Mensagem Final"]

page_selected = pages.index(page_selected)

page = st.sidebar.selectbox(
    "Índice",
    pages,
    index=page_selected
    )

if page == "Capa":
    st.header("Bem-vindo ao Regulamento de Tênis!")
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0001.jpg")
    
elif page == "Contracapa":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0002.jpg")
    
elif page == "Mensagem da Diretoria":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0003.jpg")
    
elif page == "Cronograma":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0004.jpg")
    
elif page == "Inscrições":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0005.jpg")
    
elif page == "Início do Campeonato":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0006.jpg")
    
elif page == "Critério de Pontuação":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0006.jpg")
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0007.jpg")
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0008.jpg")
    
elif page == "Campeonato de Duplas":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0008.jpg")
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0009.jpg")
    
elif page == "Reserva de Quadras":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0009.jpg")
    
elif page == "Regra do Desafiante e Desafiado":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0010.jpg")
    
elif page == "Tolerância de Tempo":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0010.jpg")
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0011.jpg")
    
elif page == "Solicitação de Ausência":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0011.jpg")
    
elif page == "Desistência/Abandono":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0011.jpg")
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0012.jpg")
    
elif page == "Regra do Jogador que Ausenta do Torneio":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0012.jpg")
    
elif page == "Falta de Energia ou Chuva Durante o Jogo":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0012.jpg")
    
elif page == "Ranking":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0012.jpg")
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0013.jpg")
    
elif page == "Premiação":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0013.jpg")
    
elif page == "Confraternização":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0013.jpg")
    
elif page == "Funções do Presidente e Vice":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0014.jpg")
    
elif page == "Funções do Conselho":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0014.jpg")
    
elif page == "Regras do Grupo do Whatsapp":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0015.jpg")
    
elif page == "Disposições Gerais":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0015.jpg")
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0016.jpg")
    
elif page == "Histórico 1":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0017.jpg")
    
elif page == "Histórico 2":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0018.jpg")
    
elif page == "Mensagem Final":
    st.image("REGULAMENTO 18 ATP 2024_pages-to-jpg-0019.jpg")
