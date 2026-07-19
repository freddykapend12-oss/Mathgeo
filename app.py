import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.title("Mon Outil Mathématiques & Physique")

# Menu de navigation à gauche
menu = st.sidebar.radio("Navigation", ["Maths Avancées", "Physique/Géotechnique", "Visualisation"])

# --- OPTION 1 : MATHS ---
if menu == "Maths Avancées":
    st.header("Calcul Mathématique")
    x = sp.symbols('x')
    func = st.text_input("Entrez une fonction (ex: x**2)", "x**2")
    if st.button("Calculer la dérivée"):
        st.write("Dérivée :", sp.diff(func, x))

# --- OPTION 2 : PHYSIQUE / GÉOTECHNIQUE ---
elif menu == "Physique/Géotechnique":
    st.header("Géotechnique")
    st.write("Module en construction pour calcul de contraintes.")
    poids = st.number_input("Poids spécifique (kN/m3)", value=20.0)
    profondeur = st.number_input("Profondeur (m)", value=5.0)
    if st.button("Calculer Contrainte"):
        sigma = poids * profondeur
        st.success(f"Contrainte verticale : {sigma} kPa")

# --- OPTION 3 : VISUALISATION ---
elif menu == "Visualisation":
    st.header("Visualisation de données")
    x_val = np.linspace(-10, 10, 100)
    y_val = x_val**2  # Exemple de fonction
    fig, ax = plt.subplots()
    ax.plot(x_val, y_val)
    st.pyplot(fig)