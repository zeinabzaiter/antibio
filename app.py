import streamlit as st
import pandas as pd
import plotly.express as px

# Charger les données
file_path = 'antibiotics_exceeding_alert_thresholds_2024.xlsx'  # Ton fichier de données
df = pd.read_excel(file_path)

# Titre de l'application
st.title("Dashboard des alertes par antibiotique")

# Sélecteur d'antibiotique
antibiotic = st.selectbox("Choisissez un antibiotique", df['Antibiotique'].unique())

# Filtrer les données en fonction de l'antibiotique sélectionné
filtered_df = df[df['Antibiotique'] == antibiotic]

# Graphique des alertes par semaine
fig = px.bar(filtered_df, x='Semaine', y='Alert Count',
             title=f'Alerte de {antibiotic} par Semaine',
             labels={'Semaine': 'Semaine', 'Alert Count': 'Nombre d\'alertes'})

# Afficher le graphique
st.plotly_chart(fig)

# Afficher les données sous forme de tableau
st.subheader("Données de alertes par semaine")
st.write(filtered_df)

# Afficher des statistiques (optionnel)
st.subheader("Statistiques des alertes")
st.write(filtered_df.describe())
