import streamlit as st
import sympy as sp
import math
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="MathGeo Pro", page_icon="🌍", layout="wide")
st.title("🌍 MathGeo Pro - Version Pro")

tab1, tab2, tab3 = st.tabs(["Mathématiques", "Géosciences", "Physique"])

# --- TAB 1 : MATHS (Avec étapes) ---
with tab1:
    st.header("Analyse Mathématique")
    choix = st.selectbox("Sélectionner l'opération :", ["Dérivée", "Intégrale", "Équation 2nd degré"], key="math_sel")
    x = sp.symbols('x')
   
    if choix == "Dérivée":
        expr = st.text_input("Fonction f(x) :", "2*x**2 + 3*x", key="deriv_input")
        if st.button("Calculer avec étapes"):
            f = sp.sympify(expr)
            res = sp.diff(f, x)
            st.write("### Étapes :")
            st.latex(r"\frac{d}{dx}(" + sp.latex(f) + ")")
            st.success(f"Résultat : {res}")

    elif choix == "Intégrale":
        expr = st.text_input("Fonction f(x) :", "2*x", key="int_input")
        if st.button("Calculer avec étapes"):
            f = sp.sympify(expr)
            res = sp.integrate(f, x)
            st.write("### Étapes :")
            st.latex(r"\int (" + sp.latex(f) + ") \, dx")
            st.success(f"Résultat : {res} + C")

    elif choix == "Équation 2nd degré":
        st.write("### Résolution de ax² + bx + c = 0")
        a = st.number_input("a :", value=1.0)
        b = st.number_input("b :", value=0.0)
        c = st.number_input("c :", value=0.0)
       
        if st.button("Résoudre avec étapes"):
            delta = b**2 - 4*a*c
            st.write("---")
            st.write("### Étape 1 : Calcul du discriminant (Δ)")
            st.latex(fr"\Delta = b^2 - 4ac = {b}^2 - 4({a})({c}) = {delta}")
           
            if delta >= 0:
                x1 = (-b - math.sqrt(delta)) / (2*a)
                x2 = (-b + math.sqrt(delta)) / (2*a)
                st.write("### Étape 2 : Solutions")
                st.latex(r"x = \frac{-b \pm \sqrt{\Delta}}{2a}")
                st.success(f"x1 = {x1:.2f} | x2 = {x2:.2f}")
            else:
                st.error("Δ < 0 : Pas de solution réelle.")

# --- TAB 2 : GÉOSCIENCES ---
with tab2:
    st.header("Géosciences")
    domaine = st.radio("Domaine :", ["RMR", "Géophysique"], key="geo_all")
   
    if domaine == "RMR":
        u = st.number_input("Résistance (MPa) :", min_value=0.0)
        r = st.number_input("RQD (%) :", min_value=0.0, max_value=100.0)
        if st.button("Calculer RMR"):
            res = (7 if u > 100 else 4) + (20 if r > 75 else 13)
            st.success(f"Score RMR : {res}")

# --- TAB 3 : PHYSIQUE ---
with tab3:
    st.header("Physique")
    rho = st.number_input("Densité (kg/m³) :", value=1000.0)
    h = st.number_input("Profondeur (m) :", value=10.0)
    if st.button("Calculer Pression"):
        p = rho * 9.81 * h
        st.latex(r"P = \rho \cdot g \cdot h = " + f"{rho} \cdot 9.81 \cdot {h} = {p:.2f} \, \text{Pa}")
