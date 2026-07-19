import streamlit as st
import sympy as sp
import math
import pandas as pd
import io

# Configuration de la page
st.set_page_config(page_title="MathGeo Pro", page_icon="🌍", layout="wide")
st.title("🌍 MathGeo Pro - Suite d'Ingénierie")

tab1, tab2, tab3 = st.tabs(["Mathématiques", "Géosciences", "Physique"])

# --- FONCTION D'EXPORT ---
def export_csv(data_dict):
    df = pd.DataFrame([data_dict])
    csv = df.to_csv(index=False).encode('utf-8')
    return csv

# --- TAB 1 : MATHS ---
with tab1:
    st.header("Analyse Mathématique")
    choix = st.selectbox("Sélectionner l'opération :", ["Dérivée", "Intégrale", "Équation 2nd degré", "Trigonométrie"], key="math_sel")
   
    x = sp.symbols('x')
   
    if choix == "Dérivée":
        expr = st.text_input("Fonction f(x) (ex: 2*x**3 + 4*x)", key="deriv_input")
        if st.button("Calculer Dérivée", key="btn_deriv"):
            try:
                res = sp.diff(sp.sympify(expr), x)
                st.success(f"f'(x) = {res}")
                st.download_button("📥 Export CSV", export_csv({"Opération": "Dérivée", "Entrée": expr, "Résultat": str(res)}), "resultat.csv")
            except: st.error("Erreur : Vérifiez votre saisie.")

    elif choix == "Intégrale":
        expr = st.text_input("Fonction f(x) à intégrer :", key="int_input")
        if st.button("Calculer Intégrale", key="btn_int"):
            try:
                res = sp.integrate(sp.sympify(expr), x)
                st.success(f"∫ f(x)dx = {res} + C")
                st.download_button("📥 Export CSV", export_csv({"Opération": "Intégrale", "Entrée": expr, "Résultat": str(res)}), "resultat.csv")
            except: st.error("Erreur de calcul.")

    elif choix == "Équation 2nd degré":
        st.write("Résoudre ax² + bx + c = 0")
        a = st.number_input("a :", value=1.0)
        b = st.number_input("b :", value=0.0)
        c = st.number_input("c :", value=0.0)
        if st.button("Résoudre", key="btn_quad"):
            delta = b**2 - 4*a*c
            if delta > 0:
                x1 = (-b - math.sqrt(delta)) / (2*a)
                x2 = (-b + math.sqrt(delta)) / (2*a)
                res = f"x1={x1:.2f}, x2={x2:.2f}"
            elif delta == 0:
                res = f"x0={-b/(2*a):.2f}"
            else:
                res = "Pas de solution réelle"
            st.success(f"Résultat : {res}")

# --- TAB 2 : GÉOSCIENCES ---
with tab2:
    st.header("Géosciences")
    domaine = st.radio("Domaine :", ["RMR", "Géochimie", "Géophysique"], key="geo_all")
   
    if domaine == "RMR":
        with st.expander("📚 Info Norme Bieniawski"):
            st.write("Calcul simplifié du RMR.")
        u = st.number_input("Résistance (MPa) :", key="rmr_u")
        r = st.number_input("RQD (%) :", key="rmr_r")
        if st.button("Calculer RMR", key="btn_rmr"):
            res = (7 if u > 100 else 4) + (20 if r > 75 else 13)
            st.success(f"RMR : {res}")
            st.download_button("📥 Export CSV", export_csv({"Type": "RMR", "Résultat": res}), "rmr.csv")

    elif domaine == "Géochimie":
        m = st.number_input("Masse (g) :", key="gc_m")
        v = st.number_input("Volume (L) :", key="gc_v")
        if st.button("Calculer Concentration", key="btn_gc"):
            res = m/v
            st.success(f"Concentration = {res:.2f} g/L")

    elif domaine == "Géophysique":
        k = st.number_input("Facteur K :", key="gp_k")
        r = st.number_input("Résistance (Ohm) :", key="gp_r")
        if st.button("Calculer Résistivité", key="btn_gp"):
            res = k * r
            st.success(f"Rho = {res:.2f} Ohm.m")

# --- TAB 3 : PHYSIQUE ---
with tab3:
    st.header("Mécanique & Fluides")
    cat = st.selectbox("Choisir :", ["Mécanique", "Fluides"], key="ph_cat")
    if cat == "Mécanique":
        m = st.number_input("Masse (kg) :", key="mech_m")
        a = st.number_input("Accélération (m/s²) :", key="mech_a")
        if st.button("Calculer Force", key="btn_mech"): st.success(f"F = {m*a} N")
    else:
        rho = st.number_input("Densité (kg/m³) :", key="flu_rho")
        h = st.number_input("Hauteur (m) :", key="flu_h")
        if st.button("Pression", key="btn_press"): st.success(f"P = {rho * 9.81 * h:.2f} Pa")
