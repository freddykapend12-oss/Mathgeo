

import streamlit as st
import sympy as sp

st.set_page_config(page_title="MathGeo", page_icon="🌍")
st.title("🌍 Mon Outil Mathématiques & Physique")

tab1, tab2, tab3 = st.tabs(["Mathématiques", "Géotechnique & Sciences de la Terre", "Physique (Pression)"])

with tab1:
    st.header("Calcul de Dérivée")
    func_str = st.text_input("Entrez une fonction (ex: 2*x**2)")
    if st.button("Calculer la dérivée"):
        try:
            x = sp.symbols('x')
            func = sp.sympify(func_str)
            deriv = sp.diff(func, x)
            st.success(f"La dérivée est : {deriv}")
        except:
            st.error("Erreur : Vérifie ta saisie.")

with tab2:
    st.header("Boîte à outils Géotechnique")
   
    # Menu de sélection pour ne pas tout mélanger
    domaine = st.radio("Sélectionnez le domaine :",
                       ["RMR (Roche)", "Propriétés des Sols", "Contrainte", "Géochimie", "Géophysique"])

    if domaine == "RMR (Roche)":
        st.subheader("Estimation du RMR")
        ucs = st.number_input("Résistance à la compression simple (MPa) :", min_value=0.0)
        rqd = st.number_input("Indice RQD (%) :", min_value=0.0, max_value=100.0)
        if st.button("Calculer le RMR"):
            score_ucs = 7 if ucs > 100 else 4
            score_rqd = 20 if rqd > 75 else 13
            st.success(f"Score RMR estimé : {score_ucs + score_rqd}")

    elif domaine == "Propriétés des Sols":
        st.subheader("Densité humide")
        poids = st.number_input("Poids de l'échantillon (g) :", min_value=0.0)
        vol = st.number_input("Volume (cm³) :", min_value=0.01)
        if st.button("Calculer la densité"):
            st.info(f"Densité : {poids / vol:.2f} g/cm³")

    elif domaine == "Contrainte":
        st.subheader("Calcul de Contrainte (Sigma)")
        force = st.number_input("Force (N) :", min_value=0.0)
        aire = st.number_input("Aire de section (m²) :", min_value=0.0001)
        if st.button("Calculer la contrainte"):
            st.success(f"Contrainte : {force / aire:.2f} Pa")

    elif domaine == "Géochimie":
        st.subheader("Calcul de Concentration")
        masse_solute = st.number_input("Masse soluté (g) :", min_value=0.0)
        volume_solution = st.number_input("Volume solution (L) :", min_value=0.1)
        if st.button("Calculer la concentration"):
            st.info(f"Concentration : {masse_solute / volume_solution:.2f} g/L")

    elif domaine == "Géophysique":
        st.subheader("Résistivité apparente")
        k = st.number_input("Coefficient géométrique K :", min_value=0.1)
        r = st.number_input("Résistance mesurée (Ohm) :", min_value=0.0)
        if st.button("Calculer la résistivité"):
            st.success(f"Résistivité (rho) : {k * r:.2f} Ohm.m")

with tab3:
    st.header("Physique : Calcul de la Pression")
    force = st.number_input("Force appliquée (en Newtons) :", min_value=0.0)
    surface = st.number_input("Surface de contact (en m²) :", min_value=0.0001)
    if st.button("Calculer la Pression"):
        st.success(f"La pression est de {force / surface:.2f} Pascals (Pa)")
