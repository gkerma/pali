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
    {"nom": "Intuition", "famille": "Voie intérieure", "message": "Écoute la petite voix.", "axe": "Guidance subtile"},
    {"nom": "Silence", "famille": "Voie intérieure", "message": "Le vrai message se trouve dans le calme.", "axe": "Repos mental"},
    {"nom": "Présence", "famille": "Voie intérieure", "message": "Reviens ici et maintenant.", "axe": "Ancrage"},
    {"nom": "Authenticité", "famille": "Voie intérieure", "message": "Sois vrai avec toi-même.", "axe": "Alignement intérieur"},
    {"nom": "Âme", "famille": "Voie intérieure", "message": "Une mémoire profonde se réveille.", "axe": "Contact intérieur"},
    {"nom": "Ombre", "famille": "Voie intérieure", "message": "Regarde ce que tu évitais.", "axe": "Introspection"},
    {"nom": "Guérison", "famille": "Voie intérieure", "message": "Tu te répares doucement.", "axe": "Libération émotionnelle"},
    {"nom": "Vision", "famille": "Voie intérieure", "message": "Tu perçois au-delà de l’évidence.", "axe": "Perspectives nouvelles"},
    {"nom": "Cœur", "famille": "Voie intérieure", "message": "Ouvre-toi avec sincérité.", "axe": "Sensibilité"},
    {"nom": "Émotion", "famille": "Voie intérieure", "message": "Accueille ce que tu ressens.", "axe": "Acceptation"},
    {"nom": "Conscience", "famille": "Voie intérieure", "message": "Tu prends de la hauteur.", "axe": "Sagesse intérieure"},

    # II. Croissance et transformation
    {"nom": "Mutation", "famille": "Croissance", "message": "Tu changes de peau.", "axe": "Transformation profonde"},
    {"nom": "Renouveau", "famille": "Croissance", "message": "Une phase se termine, une autre s’ouvre.", "axe": "Nouvelle énergie"},
    {"nom": "Renaissance", "famille": "Croissance", "message": "Tu retrouves ton souffle.", "axe": "Régénération"},
    {"nom": "Libération", "famille": "Croissance", "message": "Un poids tombe.", "axe": "Soulagement"},
    {"nom": "Passage", "famille": "Croissance", "message": "Une porte s’ouvre devant toi.", "axe": "Transition"},
    {"nom": "Clarté", "famille": "Croissance", "message": "La confusion se dissipe.", "axe": "Vision nette"},
    {"nom": "Dépassement", "famille": "Croissance", "message": "Tu franchis un seuil intérieur.", "axe": "Courage"},
    {"nom": "Flux", "famille": "Croissance", "message": "Laisse venir, laisse aller.", "axe": "Mouvement naturel"},
    {"nom": "Patience", "famille": "Croissance", "message": "Le temps agit pour toi.", "axe": "Maturation"},
    {"nom": "Éclosion", "famille": "Croissance", "message": "Ton potentiel se déploie.", "axe": "Manifestation"},
    {"nom": "Transformation", "famille": "Croissance", "message": "Tout se réorganise.", "axe": "Métamorphose"},
    {"nom": "Ascension", "famille": "Croissance", "message": "Tu montes d’un niveau.", "axe": "Élévation"},

    # III. Relations, émotions et cœur
    {"nom": "Miroir", "famille": "Relations", "message": "L’autre reflète une part de toi.", "axe": "Compréhension"},
    {"nom": "Rencontre", "famille": "Relations", "message": "Une présence arrive dans ta vie.", "axe": "Ouverture sociale"},
    {"nom": "Partage", "famille": "Relations", "message": "Tu n’es pas seul(e).", "axe": "Connexion"},
    {"nom": "Compassion", "famille": "Relations", "message": "Adoucis ton regard.", "axe": "Empathie"},
    {"nom": "Mettā", "famille": "Relations", "message": "Rayonne sans attendre.", "axe": "Amour universel"},
    {"nom": "Joie", "famille": "Relations", "message": "La lumière revient.", "axe": "Enthousiasme"},
    {"nom": "Union", "famille": "Relations", "message": "Deux chemins se rejoignent.", "axe": "Harmonisation"},
    {"nom": "Loyauté", "famille": "Relations", "message": "Reste fidèle à l’essentiel.", "axe": "Solidité du lien"},
    {"nom": "Tension", "famille": "Relations", "message": "Une friction demande douceur.", "axe": "Ajustement"},
    {"nom": "Pardon", "famille": "Relations", "message": "Libère-toi du passé.", "axe": "Guérison de la relation"},
    {"nom": "Distance", "famille": "Relations", "message": "Un espace est nécessaire.", "axe": "Protection"},
    {"nom": "Réconciliation", "famille": "Relations", "message": "Une harmonie revient.", "axe": "Paix retrouvée"},

    # IV. Destin, guidance et potentiel
    {"nom": "Destinée", "famille": "Guidance", "message": "Tu es à l’endroit juste.", "axe": "Alignement cosmique"},
    {"nom": "Protection", "famille": "Guidance", "message": "Tu es entouré(e).", "axe": "Force invisible"},
    {"nom": "Synchronie", "famille": "Guidance", "message": "Ce signe n’est pas un hasard.", "axe": "Messages subtils"},
    {"nom": "Portail", "famille": "Guidance", "message": "Un grand changement approche.", "axe": "Opportunité essentielle"},
    {"nom": "Épreuve", "famille": "Guidance", "message": "Un défi te renforce.", "axe": "Croissance"},
    {"nom": "Courage", "famille": "Guidance", "message": "Affronte ce qui t’appelle.", "axe": "Force intérieure"},
    {"nom": "Vérité", "famille": "Guidance", "message": "Ne fuis pas ce qui est.", "axe": "Lucidité"},
    {"nom": "Abondance", "famille": "Guidance", "message": "Le flux arrive vers toi.", "axe": "Expansion"},
    {"nom": "Choix", "famille": "Guidance", "message": "La décision t’appartient.", "axe": "Responsabilité"},
    {"nom": "Voyage", "famille": "Guidance", "message": "Va voir plus loin.", "axe": "Exploration"},
    {"nom": "Manifestation", "famille": "Guidance", "message": "Ce que tu portes prend forme.", "axe": "Concrétisation"},
    {"nom": "Unité", "famille": "Guidance", "message": "Tout est relié.", "axe": "Sagesse universelle"},
]

# =========================
#   PARAMÈTRES & ÉTAT
# =========================

st.sidebar.header("⚙️ Paramètres du tirage")
mode = st.sidebar.radio(
    "Mode de tirage",
    ["Tirage libre (1–5 cartes)", "Tirage en croix (5 cartes)"],
)

if mode == "Tirage libre (1–5 cartes)":
    nb_cartes = st.sidebar.slider("Nombre de cartes :", 1, 5, 1)
else:
    nb_cartes = 5

question = st.text_input("📝 Question / intention (facultatif)", "")

# Historique dans la session
if "history" not in st.session_state:
    st.session_state["history"] = []

st.sidebar.header("📚 Historique")
show_history = st.sidebar.checkbox("Afficher l’historique des tirages", value=True)
if st.sidebar.button("Effacer l’historique 🗑️"):
    st.session_state["history"] = []

# =========================
#   FONCTION D'AFFICHAGE
# =========================
# =========================
#   FONCTION D'AFFICHAGE
# =========================

def afficher_carte(carte, titre=None, description_position=None, container=None):
    target = container or st

    pos_html = f'<div class="oracle-pos">{description_position}</div>' if description_position else ""
    front_title = titre if titre else "Carte"

    html = (
        '<div class="flip-card">'
        '<div class="flip-card-inner">'
        '<div class="flip-card-front">'
        f'{pos_html}'
        f'<h3>{front_title} — {carte["nom"]}</h3>'
        f'<p><b>Famille :</b> {carte["famille"]}</p>'
        '<p class="flip-hint">Retourne la carte (survol / toucher) pour voir le message.</p>'
        '</div>'
        '<div class="flip-card-back">'
        f'{pos_html}'
        f'<h3>{carte["nom"]}</h3>'
        f'<p><b>Message :</b> {carte["message"]}</p>'
        f'<p><i>Axe de guidance :</i> {carte["axe"]}</p>'
        '</div>'
        '</div>'
        '</div>'
    )

    target.markdown(html, unsafe_allow_html=True)

# =========================
#     TIRAGE ACTUEL
# =========================

if st.button("Tirer les cartes ✨"):
    tirage = random.sample(CARDS, nb_cartes)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    st.session_state["history"].append(
        {
            "datetime": timestamp,
            "mode": mode,
            "question": question.strip(),
            "cards": tirage,
        }
    )

    st.subheader("🔮 Résultat du tirage")

    if question.strip():
        st.markdown(f"**Intention :** _{question}_")
        st.write("---")

    if mode == "Tirage libre (1–5 cartes)":
        st.markdown("### 🔹 Tirage libre")
        for i, c in enumerate(tirage, start=1):
            afficher_carte(c, f"Carte {i}")
    else:
        st.markdown("### ✖ Tirage en croix")
        c1, c2, c3, c4, c5 = tirage

        top = st.columns(3)
        with top[1]:
            afficher_carte(c3, "Carte 3", "Ressource / Atout")

        mid = st.columns(3)
        with mid[0]:
            afficher_carte(c2, "Carte 2", "Défi / Obstacle")
        with mid[1]:
            afficher_carte(c1, "Carte 1", "Situation actuelle")
        with mid[2]:
            afficher_carte(c4, "Carte 4", "Conseil / Chemin")

        bottom = st.columns(3)
        with bottom[1]:
            afficher_carte(c5, "Carte 5", "Issue potentielle (si tu suis ce chemin)")

# =========================
#     HISTORIQUE
# =========================

if show_history and st.session_state["history"]:
    st.write("---")
    st.subheader("📚 Historique des tirages (session)")

    for idx, entry in enumerate(reversed(st.session_state["history"]), start=1):
        titre = f"{idx}. {entry['datetime']} — {entry['mode']}"
        with st.expander(titre, expanded=False):
            if entry["question"]:
                st.markdown(f"**Intention :** _{entry['question']}_")
            st.write("")
            for i, c in enumerate(entry["cards"], start=1):
                afficher_carte(c, f"Carte {i}")
elif show_history:
    st.info("Aucun tirage enregistré pour cette session.")

st.caption("Oracle de 48 cartes — Flip tarot 3D • Thème clair/sombre • Tirage libre & croix • Historique.")
