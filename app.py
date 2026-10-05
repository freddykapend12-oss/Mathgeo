import streamlit as st
import sympy as sp
import math
import numpy as np
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="MathGeo Pro", page_icon="🌍", layout="wide")
st.title("🌍 MathGeo Pro - Suite Ingénierie Complète")

# --- BARRE LATÉRALE (LOGO ET CONTACT) ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/geography.png", width=70)
    st.title("MathGeo Pro")
    st.markdown("---")
    st.markdown("### 👨‍💻 À propos")
    st.write("Outils de calculs avancés pour géologues et ingénieurs.")
    st.markdown("---")
    st.markdown("### 📬 Contact")
    st.write("📍 Kolwezi, RDC")
    st.markdown("[🔗 GitHub](https://github.com/freddykapend12-oss)")

def export_csv(data_dict):
    df = pd.DataFrame([data_dict])
    return df.to_csv(index=False).encode('utf-8')

# Définition des onglets principaux
tab1, tab2, tab3 = st.tabs(["Mathématiques", "Géosciences", "Physique"])

# --- TAB 1 : MATHÉMATIQUES ---
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
    elif choix == "Intégrale":
        expr = st.text_input("Fonction f(x) :", "2*x")
        if st.button("Calculer"):
            f = sp.sympify(expr)
            res = sp.integrate(f, x)
            st.latex(r"\int (" + sp.latex(f) + ") dx = " + sp.latex(res) + " + C")
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
    sous_domaine = st.selectbox(
        "Module :", 
        [
            "RMR (Évaluation rapide)", 
            "RQD (Géotechnique)", 
            "Cote Piezométrique (Hydrogéologie)", 
            "Géochimie (Seuils d'Anomalie)", 
            "Géochimie (Ratio)", 
            "Géophysique (K & Rho)"
        ]
    )
   
    if sous_domaine == "RMR (Évaluation rapide)":
        u = st.number_input("Résistance (MPa) :")
        r = st.number_input("RQD (%) :")
        if st.button("Calculer RMR"):
            score = (7 if u > 100 else 4) + (20 if r > 75 else 13)
            st.success(f"Score RMR estimé : {score}")

    elif sous_domaine == "RQD (Géotechnique)":
        with st.expander("📝 Procédure RQD"):
            st.latex(r"RQD = \frac{\sum L_{>10cm}}{L_{totale}} \times 100")
        l_sum = st.number_input("Somme longueurs > 10cm (cm) :")
        l_tot = st.number_input("Longueur totale passe (cm) :")
        if st.button("Calculer RQD") and l_tot > 0:
            st.success(f"RQD = {(l_sum/l_tot)*100:.2f} %")

    elif sous_domaine == "Cote Piezométrique (Hydrogéologie)":
        st.subheader("Calcul de la cote piézométrique absolue")
        alt_margelle = st.number_input("Altitude du point de mesure / Margelle (m)", value=1250.0)
        prof_eau = st.number_input("Profondeur de l'eau mesurée par rapport au sol (m)", value=12.4)
        cote_piezo = alt_margelle - prof_eau
        st.metric(label="Cote piézométrique (Niveau d'eau /mer)", value=f"{cote_piezo:.2f} m")
        st.info("💡 Cette valeur est prête pour la cartographie piézométrique.")

    elif sous_domaine == "Géochimie (Seuils d'Anomalie)":
        st.subheader("Traitement statistique pour l'exploration minière")
        donnees_input = st.text_area(
            "Entrer les teneurs des échantillons (séparées par des virgules)", 
            "12.5, 14.1, 13.8, 45.2, 11.2, 15.0, 12.9, 88.5, 13.4"
        )
        if donnees_input:
            try:
                valeurs = [float(x.strip()) for x in donnees_input.split(",")]
                arr = np.array(valeurs)
                moyenne = np.mean(arr)
                ecart_type = np.std(arr)
                seuil_anomalie = moyenne + (2 * ecart_type)
                
                st.write(f"**Nombre d'échantillons :** {len(arr)}")
                st.write(f"**Moyenne :** {moyenne:.2f}")
                st.write(f"**Écart-type :** {ecart_type:.2f}")
                st.error(f"**Seuil d'anomalie recommandé ($\mu + 2\sigma$) :** {seuil_anomalie:.2f}")
                
                # Tableau complet avec tous les détails pour le téléchargement
                df_resultats = pd.DataFrame({
                    "Teneur": arr,
                    "Moyenne_Globale": round(moyenne, 4),
                    "Ecart_Type": round(ecart_type, 4),
                    "Seuil_Anomalie": round(seuil_anomalie, 4),
                    "Statut": ["Anomalie" if x > seuil_anomalie else "Fond" for x in arr]
                })
                
                st.dataframe(df_resultats, use_container_width=True)
                
                csv = df_resultats.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Télécharger le rapport complet (CSV)",
                    data=csv,
                    file_name='rapport_geochimie_complet.csv',
                    mime='text/csv',
                )
            except Exception:
                st.warning("⚠️ Veuillez entrer uniquement des nombres valides séparés par des virgules.")

    elif sous_domaine == "Géochimie (Ratio)":
        with st.expander("📝 Procédure Ratio"):
            st.write("Utile pour comparer les anomalies (ex: Cu/Mo)")
        el1 = st.number_input("Valeur Élément 1 :")
        el2 = st.number_input("Valeur Élément 2 :")
        if st.button("Calculer Ratio") and el2 != 0:
            st.latex(r"Ratio = \frac{" + str(el1) + "}{" + str(el2) + "} = " + f"{el1/el2:.4f}")

    elif sous_domaine == "Géophysique (K & Rho)":
        mode = st.radio("Calculer :", ["Facteur K (Wenner)", "Résistivité"])
        if mode == "Facteur K (Wenner)":
            a = st.number_input("Distance électrodes a (m) :")
            if st.button("Calculer K"):
                st.latex(r"K = 2 \cdot \pi \cdot a = " + f"{2 * math.pi * a:.2f}")
        else:
            k = st.number_input("Facteur K :")
            r = st.number_input("Résistance (Ohm) :")
            if st.button("Calculer Rho"):
                st.latex(r"\rho = K \cdot R = " + f"{k*r:.2f} \, \Omega \cdot m")

# --- TAB 3 : PHYSIQUE ---
with tab3:
    st.header("Physique")
    sous_cat = st.selectbox("Module :", ["Mécanique Rationnelle", "Mécanique des Fluides"])
    if sous_cat == "Mécanique Rationnelle":
        m = st.number_input("Masse (kg) :")
        a = st.number_input("Accélération (m/s²) :")
        if st.button("Calculer Force"):
            st.latex(r"F = m \cdot a = " + f"{m*a} \, N")
    elif sous_cat == "Mécanique des Fluides":
        rho = st.number_input("Densité (kg/m³) :", value=1000.0)
        h = st.number_input("Profondeur (m) :")
        if st.button("Calculer Pression"):
            st.latex(r"P = \rho \cdot g \cdot h = " + f"{rho * 9.81 * h:.2f} \, \text{Pa}")
