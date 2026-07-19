import streamlit as st
import sympy as sp
import math

st.set_page_config(page_title="MathGeo Pro", page_icon="🌍")
st.title("🌍 Mon Outil Mathématiques & Physique")

tab1, tab2, tab3 = st.tabs(["Mathématiques", "Géotechnique", "Physique"])

with tab1:
    st.header("Calculs Mathématiques")
    choix_math = st.radio("Outil :", ["Dérivée", "Géométrie", "Trigonométrie"], key="math_r")
    if choix_math == "Dérivée":
        f = st.text_input("Fonction (ex: 2*x**2)", key="f_deriv")
        if st.button("Calculer Dérivée", key="btn_d"):
            st.success(f"Résultat : {sp.diff(sp.sympify(f), sp.symbols('x'))}")
    elif choix_math == "Géométrie":
        if st.button("Aire Rectangle", key="btn_rect"): st.write("Calcul rectangle...")
    elif choix_math == "Trigonométrie":
        if st.button("Calculer Trigonométrie", key="btn_trig"): st.write("Calcul trigo...")

with tab2:
    st.header("Géotechnique")
    domaine = st.radio("Domaine :", ["RMR", "Sols", "Contrainte"], key="geo_r")
    if domaine == "RMR":
        u = st.number_input("MPa:", key="rmr_u")
        r = st.number_input("RQD:", key="rmr_r")
        if st.button("Calculer RMR", key="btn_rmr"): st.success("Calculé")
    elif domaine == "Sols":
        if st.button("Calculer Densité", key="btn_sol"): st.write("Calculé")

with tab3:
    st.header("Physique")
    p = st.button("Calculer Pression", key="btn_press")
    if p: st.write("Résultat pression")
