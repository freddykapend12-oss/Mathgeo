

import streamlit as st
import sympy as sp
import math

st.set_page_config(page_title="MathGeo Pro", page_icon="🌍")
st.title("🌍 Mon Outil Mathématiques & Physique")

tab1, tab2, tab3 = st.tabs(["Mathématiques", "Géotechnique", "Physique"])

# --- ONGLET 1 : MATHÉMATIQUES ---
with tab1:
    st.header("Calculs Mathématiques")
    choix_math = st.radio("Choisissez l'outil :", ["Dérivée", "Géométrie", "Trigonométrie"])
   
    if choix_math == "Dérivée":
        func_str = st.text_input("Fonction (ex: 2*x**2)")
        if st.button("Calculer"):
            x = sp.symbols('x')
            st.write(f"Dérivée : {sp.diff(sp.sympify(func_str), x)}")

    elif choix_math == "Géométrie":
        forme = st.selectbox("Forme :", ["Cercle", "Rectangle"])
        if forme == "Cercle":
            r = st.number_input("Rayon :")
            if st.button("Aire"): st.write(f"Aire = {math.pi * r**2:.2f}")
        else:
            l = st.number_input("Longueur :")
            w = st.number_input("Largeur :")
            if st.button("Aire"): st.write(f"Aire = {l * w}")

    elif choix_math == "Trigonométrie":
        angle = st.number_input("Angle en degrés :")
        if st.button("Calculer"):
            rad = math.radians(angle)
            st.write(f"Sinus : {math.sin(rad):.2f} | Cosinus : {math.cos(rad):.2f}")

# --- ONGLET 2 : GÉOTECHNIQUE ---
with tab2:
    st.header("Boîte à outils Géotechnique")
    domaine = st.radio("Domaine :", ["RMR", "Sols", "Contrainte", "Géochimie", "Géophysique"])
    # ... (Garde ton code précédent ici, ou ajoute les autres domaines) ...
    st.info("Utilise ton menu précédent pour les calculs géotechniques.")

# --- ONGLET 3 : PHYSIQUE ---
with tab3:
    st.header("Physique")
    choix_phys = st.radio("Domaine :", ["Pression", "Mécanique", "Fluides"])
   
    if choix_phys == "Mécanique":
        m = st.number_input("Masse (kg) :")
        a = st.number_input("Accélération (m/s²) :")
        if st.button("Calculer Force (F=ma)"):
            st.success(f"Force = {m * a} Newtons")
           
    elif choix_phys == "Fluides":
        rho = st.number_input("Densité du fluide (kg/m³) :")
        h = st.number_input("Hauteur (m) :")
        g = 9.81
        if st.button("Calculer Pression Hydrostatique"):
            st.success(f"Pression = {rho * g * h:.2f} Pascals")
           
    elif choix_phys == "Pression":
        force = st.number_input("Force (N) :")
        surf = st.number_input("Surface (m²) :")
        if st.button("Calculer"): st.write(f"Pression = {force/surf:.2f} Pa")

