import streamlit as st
import sympy as sp
import math
import pandas as pd

# Configuration
st.set_page_config(page_title="MathGeo Pro", page_icon="🌍", layout="wide")
st.title("🌍 MathGeo Pro - Suite Ingénierie Complète")

def export_csv(data_dict):
    df = pd.DataFrame([data_dict])
    return df.to_csv(index=False).encode('utf-8')

tab1, tab2, tab3 = st.tabs(["Mathématiques", "Géosciences", "Physique"])

# --- TAB 1 : MATHS ---
with tab1:
    st.header("Analyse Mathématique")
    choix = st.selectbox("Opération :", ["Dérivée", "Intégrale", "Équation 2nd degré"])
    x = sp.symbols('x')
   
    if choix == "Dérivée":
        expr = st.text_input("Fonction f(x) :", "2*x**2 + 3*x")
        if st.button("Calculer"):
            f = sp.sympify(expr)
            res = sp.diff(f, x)
            st.latex(r"\frac{d}{dx}(" + sp.latex(f) + ") = " + sp.latex(res))
            st.download_button("📥 CSV", export_csv({"Op": "Derivee", "Res": str(res)}), "derivee.csv")

    elif choix == "Intégrale":
        expr = st.text_input("Fonction f(x) :", "2*x")
        if st.button("Calculer"):
            f = sp.sympify(expr)
            res = sp.integrate(f, x)
            st.latex(r"\int (" + sp.latex(f) + ") dx = " + sp.latex(res) + " + C")
            st.download_button("📥 CSV", export_csv({"Op": "Integrale", "Res": str(res)}), "integrale.csv")

    elif choix == "Équation 2nd degré":
        a, b, c = st.number_input("a"), st.number_input("b"), st.number_input("c")
        if st.button("Résoudre"):
            delta = b**2 - 4*a*c
            st.latex(fr"\Delta = {b}^2 - 4({a})({c}) = {delta}")
            if delta >= 0:
                x1, x2 = (-b - math.sqrt(delta))/(2*a), (-b + math.sqrt(delta))/(2*a)
                st.success(f"x1={x1:.2f}, x2={x2:.2f}")

# --- TAB 2 : GÉOSCIENCES ---
with tab2:
    st.header("Géosciences")
    domaine = st.radio("Domaine :", ["Géotechnique (RMR)", "Géochimie", "Géophysique"])
   
    if domaine == "Géotechnique (RMR)":
        with st.expander("📝 Procédure RMR"):
            st.write("Le RMR (Bieniawski) évalue la qualité des roches. On additionne les notes de résistance, RQD, espacement, état des joints et eaux souterraines.")
        u = st.number_input("Résistance (MPa) :")
        r = st.number_input("RQD (%) :")
        if st.button("Calculer RMR"):
            res = (7 if u > 100 else 4) + (20 if r > 75 else 13)
            st.success(f"Score RMR : {res}")

    elif domaine == "Géochimie":
        with st.expander("📝 Procédure Concentration"):
            st.write("La concentration massique se calcule par le rapport entre la masse du soluté et le volume de la solution.")
            st.latex(r"C = \frac{m}{V}")
        m = st.number_input("Masse (g) :")
        v = st.number_input("Volume (L) :")
        if st.button("Calculer Concentration"):
            st.success(f"C = {m/v:.2f} g/L")

    elif domaine == "Géophysique":
        with st.expander("📝 Procédure Résistivité"):
            st.write("La résistivité apparente dépend de la géométrie de l'électrode (K) et de la résistance mesurée.")
            st.latex(r"\rho = K \cdot R")
        k = st.number_input("Facteur K :")
        r = st.number_input("Résistance (Ohm) :")
        if st.button("Calculer Résistivité"):
            st.success(f"Rho = {k*r:.2f} Ohm.m")

# --- TAB 3 : PHYSIQUE ---
with tab3:
    st.header("Physique")
    sous_cat = st.selectbox("Module :", ["Mécanique Rationnelle", "Mécanique des Fluides"])
   
    if sous_cat == "Mécanique Rationnelle":
        with st.expander("📝 Principe Mécanique"):
            st.write("Calcul de la Force selon la 2ème loi de Newton : F = m * a")
        m = st.number_input("Masse (kg) :")
        a = st.number_input("Accélération (m/s²) :")
        if st.button("Calculer Force"):
            st.latex(r"F = m \cdot a = " + f"{m} \cdot {a} = {m*a} \, N")

    elif sous_cat == "Mécanique des Fluides":
        with st.expander("📝 Principe Fluides"):
            st.write("Pression hydrostatique : P = rho * g * h")
        rho = st.number_input("Densité (kg/m³) :", value=1000.0)
        h = st.number_input("Profondeur (m) :")
        if st.button("Calculer Pression"):
            p = rho * 9.81 * h
            st.latex(r"P = \rho \cdot g \cdot h = " + f"{p:.2f} \, \text{Pa}")
