import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)


def accueil():
      st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")
    
    
    
def photos_chats():
    col1, col2, col3 = st.columns(3)

    with col1:
      st.header("A cat")
      st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
      st.header("A dog")
      st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
      st.header("An owl")
      st.image("https://static.streamlit.io/examples/owl.jpg")
      
selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"]
        )
      
      
authenticator.login()

if st.session_state["authentication_status"]:
  if selection == "Accueil":
    accueil()
  elif selection == "Photos":
    photos_chats()
  # Le bouton de déconnexion
  authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')