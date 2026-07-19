import streamlit as st
import sympy as sp

st.title("Mon Outil Mathématiques & Physique")

# Création des onglets pour organiser l'application
tab1, tab2, tab3 = st.tabs(["Mathématiques", "Géotechnique (RMR)", "Physique (Pression)"])

with tab1:
    st.header("Calcul de Dérivée")
    func_str = st.text_input("Entrez une fonction (ex: 2*x**2)")
    if st.button("Calculer la dérivée"):
        try:
            x = sp.symbols('x')
            func = sp.sympify(func_str) # Conversion de la chaîne en expression mathématique
            deriv = sp.diff(func, x)
            st.success(f"La dérivée est : {deriv}")
        except:
            st.error("Erreur : Vérifie ta saisie. N'oublie pas les * pour les multiplications (ex: 2*x).")

with tab2:
    st.header("Géotechnique : Estimation du RMR")
    ucs = st.number_input("Résistance à la compression simple (MPa) :", min_value=0.0)
    rqd = st.number_input("Indice RQD (%) :", min_value=0.0, max_value=100.0)
    if st.button("Calculer le RMR"):
        score_ucs = 7 if ucs > 100 else 4
        score_rqd = 20 if rqd > 75 else 13
        rmr_total = score_ucs + score_rqd
        st.success(f"Score RMR estimé : {rmr_total}")

with tab3:
    st.header("Physique : Calcul de la Pression")
    force = st.number_input("Force appliquée (en Newtons) :", min_value=0.0)
    surface = st.number_input("Surface de contact (en m²) :", min_value=0.0001)
    if st.button("Calculer la Pression"):
        pression = force / surface
        st.success(f"La pression est de {pression:.2f} Pascals (Pa)")
