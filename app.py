import streamlit as st
import sympy as sp
import math

st.set_page_config(page_title="MathGeo Pro", page_icon="🌍")
st.title("🌍 Mon Outil Mathématiques & Physique")

tab1, tab2, tab3 = st.tabs(["Mathématiques", "Géosciences", "Physique"])

# --- TAB 1 : MATHS ---
with tab1:
    st.header("Calculs Mathématiques")
    choix = st.radio("Outil :", ["Dérivée", "Géométrie", "Trigonométrie"], key="math_r")
    if choix == "Dérivée":
        f = st.text_input("Fonction (ex: 2*x**2)", key="f_deriv")
        if st.button("Calculer", key="btn_deriv"):
            st.success(f"Résultat : {sp.diff(sp.sympify(f), sp.symbols('x'))}")
    elif choix == "Géométrie":
        l = st.number_input("Longueur :", key="rect_l")
        w = st.number_input("Largeur :", key="rect_w")
        if st.button("Calculer Aire", key="btn_rect"): st.success(f"Aire = {l * w}")
    elif choix == "Trigonométrie":
        angle = st.number_input("Angle en degrés :", key="trig_a")
        if st.button("Calculer Sin/Cos", key="btn_trig"):
            rad = math.radians(angle)
            st.success(f"Sinus : {math.sin(rad):.2f} | Cosinus : {math.cos(rad):.2f}")

# --- TAB 2 : GÉOSCIENCES ---
with tab2:
    st.header("Boîte à outils Géosciences")
    domaine = st.radio("Domaine :", ["RMR", "Sols", "Géochimie", "Géophysique"], key="geo_all")
   
    if domaine == "RMR":
        u = st.number_input("Résistance (MPa) :", key="rmr_u")
        r = st.number_input("RQD (%) :", key="rmr_r")
        if st.button("Calculer RMR", key="btn_rmr"): st.success(f"RMR : { (7 if u > 100 else 4) + (20 if r > 75 else 13) }")
       
    elif domaine == "Sols":
        m = st.number_input("Poids (g) :", key="sol_m")
        v = st.number_input("Volume (cm³) :", key="sol_v")
        if st.button("Calculer Densité", key="btn_sol"): st.success(f"Densité = {m/v:.2f} g/cm³")
       
    elif domaine == "Géochimie":
        m = st.number_input("Masse (g) :", key="gc_m")
        v = st.number_input("Volume (L) :", key="gc_v")
        if st.button("Calculer Concentration", key="btn_gc"): st.success(f"Concentration = {m/v:.2f} g/L")
       
    elif domaine == "Géophysique":
        k = st.number_input("Facteur géométrique K :", key="gp_k")
        r = st.number_input("Résistance (Ohm) :", key="gp_r")
        if st.button("Calculer Résistivité", key="btn_gp"): st.success(f"Rho = {k * r:.2f} Ohm.m")

# --- TAB 3 : PHYSIQUE ---
with tab3:
    st.header("Physique")
    choix_ph = st.radio("Domaine :", ["Mécanique Rationnelle", "Mécanique des Fluides"], key="ph_r")
   
    if choix_ph == "Mécanique Rationnelle":
        m = st.number_input("Masse (kg) :", key="mech_m")
        a = st.number_input("Accélération (m/s²) :", key="mech_a")
        if st.button("Calculer Force", key="btn_mech"): st.success(f"Force = {m * a} Newtons")
       
    elif choix_ph == "Mécanique des Fluides":
        rho = st.number_input("Densité fluide (kg/m³) :", key="flu_rho")
        h = st.number_input("Profondeur (m) :", key="flu_h")
        if st.button("Calculer Pression", key="btn_flu"): st.success(f"Pression = {rho * 9.81 * h:.2f} Pa")
