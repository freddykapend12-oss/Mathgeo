import streamlit as st
import sympy as sp
import math

st.set_page_config(page_title="MathGeo Pro", page_icon="🌍")
st.title("🌍 Mon Outil Mathématiques & Physique")

tab1, tab2, tab3 = st.tabs(["Mathématiques", "Géotechnique", "Physique"])

# --- ONGLET 1 : MATHÉMATIQUES ---
with tab1:
    st.header("Calculs Mathématiques")
    choix_math = st.radio("Choisissez l'outil :", ["Dérivée", "Géométrie", "Trigonométrie"], key="math_radio")
   
    if choix_math == "Dérivée":
        func_str = st.text_input("Fonction (ex: 2*x**2)", key="math_func")
        if st.button("Calculer la dérivée", key="btn_deriv"):
            x = sp.symbols('x')
            st.success(f"Dérivée : {sp.diff(sp.sympify(func_str), x)}")

    elif choix_math == "Géométrie":
        forme = st.selectbox("Forme :", ["Cercle", "Rectangle"], key="geo_forme")
        if forme == "Cercle":
            r = st.number_input("Rayon :", key="geo_r")
            if st.button("Calculer Aire Cercle", key="btn_cercle"): st.success(f"Aire = {math.pi * r**2:.2f}")
        else:
            l = st.number_input("Longueur :", key="geo_l")
            w = st.number_input("Largeur :", key="geo_w")
            if st.button("Calculer Aire Rectangle", key="btn_rect"): st.success(f"Aire = {l * w}")

    elif choix_math == "Trigonométrie":
        angle = st.number_input("Angle en degrés :", key="trig_angle")
        if st.button("Calculer Trigonométrie", key="btn_trig"):
            rad = math.radians(angle)
            st.success(f"Sinus : {math.sin(rad):.2f} | Cosinus : {math.cos(rad):.2f}")

# --- ONGLET 2 : GÉOTECHNIQUE ---
with tab2:
    st.header("Boîte à outils Géotechnique")
    domaine = st.radio("Domaine :", ["RMR", "Sols", "Contrainte", "Géochimie", "Géophysique"], key="geo_radio")

    if domaine == "RMR":
        ucs = st.number_input("Résistance (MPa) :", min_value=0.0, key="rmr_ucs")
        rqd = st.number_input("RQD (%) :", min_value=0.0, max_value=100.0, key="rmr_rqd")
        if st.button("Calculer RMR", key="btn_rmr"):
            st.success(f"Score RMR : {7 if ucs > 100 else 4 + 20 if rqd > 75 else 13}")

    elif domaine == "Sols":
        poids = st.number_input("Poids (g) :", min_value=0.0, key="sol_poids")
        vol = st.number_input("Volume (cm³) :", min_value=0.1, key="sol_vol")
        if st.button("Calculer Densité", key="btn_sol"): st.success(f"Densité : {poids / vol:.2f}")

    elif domaine == "Contrainte":
        f = st.number_input("Force (N) :", min_value=0.0, key="con_f")
        a = st.number_input("Aire (m²) :", min_value=0.0001, key="con_a")
        if st.button("Calculer Contrainte", key="btn_con"): st.success(f"Sigma = {f/a:.2f} Pa")

# --- ONGLET 3 : PHYSIQUE ---
with tab3:
    st.header("Physique")
    choix_phys = st.radio("Domaine :", ["Pression", "Mécanique", "Fluides"], key="phys_radio")
   
    if choix_phys == "Mécanique":
        m = st.number_input("Masse (kg) :", key="phys_m")
        a = st.number_input("Accélération (m/s²) :", key="phys_a")
        if st.button("Calculer Force", key="btn_force"): st.success(f"F = {m * a} N")
           
    elif choix_phys == "Fluides":
        rho = st.number_input("Densité (kg/m³) :", key="phys_rho")
        h = st.number_input("Hauteur (m) :", key="phys_h")
        if st.button("Calculer Pression Fluide", key="btn_fluid"): st.success(f"P = {rho * 9.81 * h:.2f} Pa")
           
    elif choix_phys == "Pression":
        f = st.number_input("Force (N) :", key="phys_f2")
        s = st.number_input("Surface (m²) :", key="phys_s2")
        if st.button("Calculer Pression", key="btn_press"): st.success(f"P = {f/s:.2f} Pa"
