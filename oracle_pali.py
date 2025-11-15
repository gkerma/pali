import random
from datetime import datetime
import textwrap
import streamlit as st

st.set_page_config(page_title="Oracle 48 cartes", page_icon="🔮", layout="centered")

# =========================
#   THEME CLAIR / SOMBRE
# =========================

st.sidebar.header("🎨 Thème")
theme = st.sidebar.radio(
    "Choisir un thème",
    ["Sombre", "Clair"],
    index=0
)

if theme == "Sombre":
    bg = "#111111"
    card_bg = "rgba(17,17,17,0.9)"
    text_color = "#ffffff"
    border_color = "rgba(255,255,255,0.12)"
else:
    bg = "#f3f3f3"
    card_bg = "rgba(255,255,255,0.98)"
    text_color = "#000000"
    border_color = "rgba(0,0,0,0.15)"

# =========================
#   CSS GLOBAL
# =========================

st.markdown(
    f"""
<style>
body {{
    background-color: {bg} !important;
    color: {text_color};
}}

.flip-card {{
    background-color: transparent;
    width: 100%;
    perspective: 1000px;
    margin-bottom: 1rem;
}}

.flip-card-inner {{
    position: relative;
    width: 100%;
    min-height: 160px;
    text-align: left;
    transition: transform 0.6s;
    transform-style: preserve-3d;
}}

.flip-card:hover .flip-card-inner {{
    transform: rotateY(180deg);
}}

.flip-card:active .flip-card-inner {{
    transform: rotateY(180deg);
}}

.flip-card-front, .flip-card-back {{
    position: absolute;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    border-radius: 14px;
    border: 1px solid {border_color};
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.28);
    padding: 0.9rem 1.1rem;
    box-sizing: border-box;
    background-color: {card_bg};
    color: {text_color};
}}

.flip-card-front h3, .flip-card-back h3 {{
    margin-top: 0;
    margin-bottom: 0.4rem;
    font-size: 1.05rem;
}}

.flip-card-front p, .flip-card-back p {{
    margin: 0.1rem 0;
    font-size: 0.94rem;
}}

.flip-card-back {{
    transform: rotateY(180deg);
}}

.oracle-pos {{
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    opacity: 0.7;
    margin-bottom: 0.2rem;
}}

.flip-hint {{
    font-size: 0.75rem;
    opacity: 0.6;
    margin-top: 0.3rem;
}}
</style>
    """,
    unsafe_allow_html=True,
)

# =========================
#       TITRE
# =========================

st.title("🔮 Oracle de 48 cartes")
st.write("Passe la souris ou touche les cartes pour les retourner façon tarot (recto / verso).")

# =========================
#       JEU DE CARTES
# =========================

CARDS = [
    # I. Voie intérieure
    {"nom": "Éveil", "famille": "Voie intérieure", "message": "Quelque chose s’ouvre en toi.", "axe": "Clarté intérieure"},
    {"nom": "
