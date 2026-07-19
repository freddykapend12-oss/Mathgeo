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
        forme = st.selectbox("Forme", ["Rectangle", "Cercle"], key="geo_f")
        if forme == "Rectangle":
            l = st.number_input("Longueur :", key="rect_l")
            w = st.number_input("Largeur :", key="rect_w")
            if st.button("Calculer Aire", key="btn_rect"): st.success(f"Aire = {l * w}")
        else:
            r = st.number_input("Rayon :", key="cercle_r")
            if st.button("Calculer Aire", key="btn_cercle"): st.success(f"Aire = {math.pi * r**2:.2f}")

    elif choix_math == "Trigonométrie":
        angle = st.number_input("Angle en degrés :", key="trig_a")
        if st.button("Calculer Trigonométrie", key="btn_trig"):
            rad = math.radians(angle)
            st.success(f"Sinus : {math.sin(rad):.2f} | Cosinus : {math.cos(rad):.2f}")

with tab2:
    st.header("Géotechnique")
    domaine = st.radio("Domaine :", ["RMR", "Sols", "Contrainte"], key="geo_r")
    if domaine == "RMR":
        u = st.number_input("MPa:", key="rmr_u")
        r = st.number_input("RQD:", key="rmr_r")
        if st.button("Calculer RMR", key="btn_rmr"):
            st.success(f"Score RMR : {7 if u > 100 else 4 + 20 if r > 75 else 13}")
    elif domaine == "Sols":
        p = st.number_input("Poids (g) :", key="sol_p")
        v = st.number_input("Volume (cm³) :", key="sol_v")
        if st.button("Calculer Densité", key="btn_sol"): st.success(f"Densité : {p/v:.2f} g/cm³")
    elif domaine == "Contrainte":
        f = st.number_input("Force (N) :", key="con_f")
        a = st.number_input("Aire (m²) :", key="con_a")
        if st.button("Calculer Contrainte", key="btn_con"): st.success(f"Contrainte : {f/a:.2f} Pa")

with tab3:
    st.header("Physique")
    f = st.number_input("Force (N) :", key="phys_f")
    s = st.number_input("Surface (m²) :", key="phys_s")
    if st.button("Calculer Pression", key="btn_press"):
        st.success(f"Pression = {f/s:.2f} Pa")
