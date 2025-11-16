import random
from datetime import datetime
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
    bg = "#050509"
    card_bg = "rgba(10,10,18,0.96)"
    text_color = "#ffffff"
    border_color = "rgba(255,255,255,0.16)"
    accent_glow = "rgba(176,124,255,0.35)"
else:
    bg = "#f0f0f5"
    card_bg = "rgba(255,255,255,0.99)"
    text_color = "#111111"
    border_color = "rgba(0,0,0,0.12)"
    accent_glow = "rgba(120,120,255,0.25)"

# =========================
#   CSS GLOBAL (deck look)
# =========================

st.markdown(
    f"""
<style>
body {{
    background-color: {bg} !important;
    color: {text_color};
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}}

main.block-container {{
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}}

.flip-card {{
    background-color: transparent;
    width: 100%;
    max-width: 320px;
    perspective: 1200px;
    margin-bottom: 1.4rem;
    margin-left: auto;
    margin-right: auto;
    transition: transform 0.2s ease-out, box-shadow 0.2s ease-out;
}}

.flip-card:hover {{
    transform: translateY(-4px);
}}

.flip-card-inner {{
    position: relative;
    width: 100%;
    min-height: 190px;
    text-align: left;
    transition: transform 0.6s;
    transform-style: preserve-3d;
    border-radius: 22px;
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
    border-radius: 22px;
    border: 1px solid {border_color};
    box-shadow:
        0 18px 40px rgba(0, 0, 0, 0.45),
        0 0 0 1px rgba(0, 0, 0, 0.15);
    padding: 1.1rem 1.2rem;
    box-sizing: border-box;
    background-color: {card_bg};
    color: {text_color};
    background-image:
        radial-gradient(circle at 15% 0%, rgba(255,255,255,0.12), transparent 55%),
        radial-gradient(circle at 85% 120%, {accent_glow}, transparent 60%);
}}

.flip-card-front h3, .flip-card-back h3 {{
    margin-top: 0;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
}}

.flip-card-front p, .flip-card-back p {{
    margin: 0.1rem 0;
    font-size: 0.94rem;
}}

.flip-card-back {{
    transform: rotateY(180deg);
}}

.oracle-pos {{
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    opacity: 0.75;
    margin-bottom: 0.25rem;
}}

.flip-hint {{
    font-size: 0.78rem;
    opacity: 0.6;
    margin-top: 0.4rem;
}}

textarea[aria-label="Texte à copier"] {{
    font-family: "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
    font-size: 0.9rem;
}}
</style>
    """,
    unsafe_allow_html=True,
)

# =========================
#       TITRE
# =========================

st.title("🔮 Oracle de 48 cartes")
st.write("Passe la souris ou touche les cartes pour les retourner comme un véritable jeu de tarot.")

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
#   TIRAGES AVANCÉS (PACKS)
# =========================

SPREADS = [
    # Tirages courts
    {
        "id": "yin_yang",
        "nom": "Yin / Yang",
        "pack": "Tirages courts",
        "nb": 2,
        "positions": [
            "Yin (réceptivité / introspection)",
            "Yang (action / expression)",
        ],
    },
    {
        "id": "passe_present_futur",
        "nom": "Passé / Présent / Futur",
        "pack": "Tirages courts",
        "nb": 3,
        "positions": [
            "Passé / Héritage",
            "Présent",
            "Futur probable",
        ],
    },

    # Relationnels
    {
        "id": "relation_miroir",
        "nom": "Relation à deux – miroir",
        "pack": "Relationnel",
        "nb": 6,
        "positions": [
            "Toi",
            "L’autre",
            "Dynamique du lien",
            "Ce qui bloque",
            "Ce qui libère",
            "Potentiel de la relation",
        ],
    },
    {
        "id": "toi_ombre",
        "nom": "Toi & ton ombre",
        "pack": "Relationnel",
        "nb": 3,
        "positions": [
            "Toi (conscient)",
            "Ombre active",
            "Message d’intégration",
        ],
    },
    {
        "id": "relation_karmique",
        "nom": "Relation karmique",
        "pack": "Relationnel",
        "nb": 5,
        "positions": [
            "Origine karmique",
            "Leçon actuelle",
            "Blocage",
            "Intégration",
            "Évolution possible",
        ],
    },

    # Spirituels
    {
        "id": "guides",
        "nom": "Tirage des guides",
        "pack": "Spirituel",
        "nb": 3,
        "positions": [
            "Message principal",
            "Alerte / attention",
            "Conseil spirituel",
        ],
    },
    {
        "id": "ame",
        "nom": "Tirage de l’âme",
        "pack": "Spirituel",
        "nb": 3,
        "positions": [
            "Ce que ton âme sait",
            "Ce qu’elle t’invite à libérer",
            "Ce qu’elle veut te voir incarner",
        ],
    },
    {
        "id": "porte_cle_passage",
        "nom": "Porte / Clé / Passage",
        "pack": "Spirituel",
        "nb": 3,
        "positions": [
            "La Porte — ce qui s’ouvre",
            "La Clé — ce qui permet",
            "Le Passage — la transformation",
        ],
    },

    # Décisionnels
    {
        "id": "choix_ab",
        "nom": "Choix A / Choix B",
        "pack": "Décisionnel",
        "nb": 5,
        "positions": [
            "Énergie du choix A",
            "Énergie du choix B",
            "Ce qui t’aligne (axe de vérité)",
            "Issue si tu choisis A",
            "Issue si tu choisis B",
        ],
    },
    {
        "id": "chemin_actuel_potentiel",
        "nom": "Chemin actuel / chemin potentiel",
        "pack": "Décisionnel",
        "nb": 3,
        "positions": [
            "Où mène ton chemin actuel",
            "Où mènerait un nouveau chemin",
            "Signal à écouter",
        ],
    },

    # Évolution personnelle
    {
        "id": "evolution_personnelle",
        "nom": "Évolution personnelle (7 cartes)",
        "pack": "Évolution",
        "nb": 7,
        "positions": [
            "Toi actuellement",
            "Blocage",
            "Blessure active",
            "Ressource intérieure",
            "Aide extérieure",
            "Leçon",
            "Transformation",
        ],
    },

    # Horoscope énergétique
    {
        "id": "horoscope_energetique",
        "nom": "Horoscope énergétique (12 cartes)",
        "pack": "Horoscope énergétique",
        "nb": 12,
        "positions": [
            "Vitalité / énergie de base",
            "Sécurité / corps / maison intérieure",
            "Communication / idées",
            "Racines / passé",
            "Expression / créativité",
            "Santé / ajustements",
            "Relations / liens proches",
            "Transformation / alchimie",
            "Vision / expansion",
            "Mission / contribution",
            "Guidance / intuition",
            "Clôture & intégration",
        ],
    },

    # Intention & éléments
    {
        "id": "reve_ancrage_action",
        "nom": "Rêve / Ancrage / Action",
        "pack": "Intention",
        "nb": 3,
        "positions": [
            "Rêve / inspiration",
            "Ancrage / limite",
            "Action / prochaine étape",
        ],
    },
    {
        "id": "quatre_elements",
        "nom": "4 éléments",
        "pack": "Intention",
        "nb": 4,
        "positions": [
            "Feu — mouvement, moteur",
            "Eau — émotions",
            "Air — pensées",
            "Terre — concret / matière",
        ],
    },
]

PACKS = sorted(sorted({s["pack"] for s in SPREADS}))

# =========================
#   PARAMÈTRES & ÉTAT
# =========================

st.sidebar.header("⚙️ Type de tirage")
tirage_mode_type = st.sidebar.radio(
    "Choisir le type",
    ["Standard (libre / croix / jour)", "Tirages avancés (packs)"],
)

question = st.text_input("📝 Question / intention (facultatif)", "")

# Historique dans la session
if "history" not in st.session_state:
    st.session_state["history"] = []

st.sidebar.header("📚 Historique")
show_history = st.sidebar.checkbox("Afficher l’historique des tirages", value=True)
if st.sidebar.button("Effacer l’historique 🗑️"):
    st.session_state["history"] = []

# ----- PARAMÈTRES STANDARD -----

daily_mode = False
mode_radio = None
nb_cartes_standard = None

if tirage_mode_type == "Standard (libre / croix / jour)":
    st.sidebar.markdown("### Paramètres standard")
    daily_mode = st.sidebar.checkbox("Mode tirage du jour (1 carte)", value=False)

    mode_radio = st.sidebar.radio(
        "Mode de tirage standard",
        ["Tirage libre (1–5 cartes)", "Tirage en croix (5 cartes)"],
    )

    if daily_mode:
        effective_mode_standard = "Tirage libre (1–5 cartes)"
        nb_cartes_standard = 1
    else:
        effective_mode_standard = mode_radio
        if effective_mode_standard == "Tirage libre (1–5 cartes)":
            nb_cartes_standard = st.sidebar.slider("Nombre de cartes (libre) :", 1, 5, 1)
        else:
            nb_cartes_standard = 5

# ----- PARAMÈTRES TIRAGES AVANCÉS -----

selected_spread = None

if tirage_mode_type == "Tirages avancés (packs)":
    st.sidebar.markdown("### Tirages avancés")
    pack_choice = st.sidebar.selectbox("Pack", PACKS)
    spreads_in_pack = [s for s in SPREADS if s["pack"] == pack_choice]
    spread_names = [s["nom"] for s in spreads_in_pack]
    spread_name_choice = st.sidebar.selectbox("Tirage", spread_names)
    selected_spread = next(s for s in spreads_in_pack if s["nom"] == spread_name_choice)

# =========================
#   AFFICHAGE CARTE
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
#   TEXTE PRÊT À COPIER
# =========================

def build_summary(tirage, mode_label, question, timestamp, daily, positions=None):
    lines = []
    titre = "Tirage du jour" if daily else "Tirage de l’oracle"
    lines.append(f"{titre} — {timestamp}")
    if question and question.strip():
        lines.append(f"Question : {question.strip()}")
    lines.append(f"Mode : {mode_label}")
    lines.append("")

    if positions is not None:
        # Tirages avancés ou croix avec positions explicites
        for i, (c, pos) in enumerate(zip(tirage, positions), start=1):
            lines.append(
                f"Carte {i} — {c['nom']} [{pos}]\n"
                f"  Message : {c['message']}\n"
                f"  Axe : {c['axe']}"
            )
    else:
        # Tirages standard sans positions
        if mode_label.startswith("Tirage en croix"):
            pos_labels = [
                "Situation actuelle",
                "Défi / obstacle",
                "Ressource / atout",
                "Conseil / chemin",
                "Issue potentielle (si tu suis ce chemin)",
            ]
            for i, (c, pos) in enumerate(zip(tirage, pos_labels), start=1):
                lines.append(
                    f"Carte {i} — {c['nom']} [{pos}]\n"
                    f"  Message : {c['message']}\n"
                    f"  Axe : {c['axe']}"
                )
        else:
            for i, c in enumerate(tirage, start=1):
                lines.append(
                    f"Carte {i} — {c['nom']} "
                    f"(famille : {c['famille']})\n"
                    f"  Message : {c['message']}\n"
                    f"  Axe : {c['axe']}"
                )

    return "\n".join(lines)

# =========================
#   ONGLET PRINCIPAL
# =========================

tab_tirage, tab_methode, tab_cartes, tab_apropos = st.tabs(
    ["🔮 Tirage", "📜 Méthode", "🃏 Toutes les cartes", "ℹ️ À propos"]
)

# ----- ONGLET TIRAGE -----
with tab_tirage:
    summary_text = ""

    if tirage_mode_type == "Standard (libre / croix / jour)":
        btn_label = "Tirer la carte du jour ✨" if daily_mode else "Tirer les cartes ✨"

        if st.button(btn_label):
            # Standard : libre ou croix
            if mode_radio == "Tirage en croix (5 cartes)" and not daily_mode:
                tirage = random.sample(CARDS, 5)
                mode_label = "Tirage en croix (5 cartes)"
            else:
                tirage = random.sample(CARDS, nb_cartes_standard)
                mode_label = "Tirage libre (1–5 cartes)"

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            st.session_state["history"].append(
                {
                    "datetime": timestamp,
                    "mode_type": "standard",
                    "mode_label": mode_label,
                    "daily": daily_mode,
                    "question": question.strip(),
                    "cards": tirage,
                    "positions": None,
                }
            )

            st.subheader("🔮 Résultat du tirage")

            if question.strip():
                st.markdown(f"**Intention :** _{question}_")
                st.write("---")

            if mode_label.startswith("Tirage libre"):
                st.markdown("### 🔹 Tirage libre")
                for i, c in enumerate(tirage, start=1):
                    afficher_carte(c, f"Carte {i}")
            else:
                st.markdown("### ✖ Tirage en croix")

                if len(tirage) != 5:
                    st.error("Erreur interne : le tirage en croix doit contenir 5 cartes.")
                else:
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

            summary_text = build_summary(tirage, mode_label, question, timestamp, daily_mode)
            st.markdown("#### 📝 Texte prêt à copier")
            st.text_area("Texte à copier", summary_text, height=220)

    else:
        # Tirages avancés (packs)
        btn_label = "Lancer ce tirage avancé ✨"
        if st.button(btn_label) and selected_spread is not None:
            nb = selected_spread["nb"]
            positions = selected_spread["positions"]
            tirage = random.sample(CARDS, nb)
            mode_label = f"Tirage avancé — {selected_spread['nom']}"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            st.session_state["history"].append(
                {
                    "datetime": timestamp,
                    "mode_type": "advanced",
                    "mode_label": mode_label,
                    "daily": False,
                    "question": question.strip(),
                    "cards": tirage,
                    "positions": positions,
                    "pack": selected_spread["pack"],
                    "spread_id": selected_spread["id"],
                }
            )

            st.subheader(f"🔮 Résultat — {selected_spread['nom']}")
            st.markdown(f"_Pack : **{selected_spread['pack']}**_")
            if question.strip():
                st.markdown(f"**Intention :** _{question}_")
                st.write("---")

            for i, (c, pos) in enumerate(zip(tirage, positions), start=1):
                afficher_carte(c, f"Carte {i}", pos)

            summary_text = build_summary(tirage, mode_label, question, timestamp, False, positions=positions)
            st.markdown("#### 📝 Texte prêt à copier")
            st.text_area("Texte à copier", summary_text, height=220)

    # ----- Historique -----
    if show_history and st.session_state["history"]:
        st.write("---")
        st.subheader("📚 Historique des tirages (session)")

        for idx, entry in enumerate(reversed(st.session_state["history"]), start=1):
            titre_hist = f"{idx}. {entry['datetime']} — {entry['mode_label']}"
            if entry.get("daily"):
                titre_hist += " (tirage du jour)"
            if entry.get("mode_type") == "advanced":
                titre_hist += f" — pack {entry.get('pack','')}"

            with st.expander(titre_hist, expanded=False):
                if entry["question"]:
                    st.markdown(f"**Intention :** _{entry['question']}_")
                st.write("")
                positions = entry.get("positions")
                if positions:
                    for i, (c, pos) in enumerate(zip(entry["cards"], positions), start=1):
                        afficher_carte(c, f"Carte {i}", pos)
                else:
                    # standard
                    if entry["mode_label"].startswith("Tirage en croix"):
                        pos_labels = [
                            "Situation actuelle",
                            "Défi / obstacle",
                            "Ressource / atout",
                            "Conseil / chemin",
                            "Issue potentielle (si tu suis ce chemin)",
                        ]
                        for i, (c, pos) in enumerate(zip(entry["cards"], pos_labels), start=1):
                            afficher_carte(c, f"Carte {i}", pos)
                    else:
                        for i, c in enumerate(entry["cards"], start=1):
                            afficher_carte(c, f"Carte {i}")

                txt = build_summary(
                    entry["cards"],
                    entry["mode_label"],
                    entry["question"],
                    entry["datetime"],
                    entry.get("daily", False),
                    positions=entry.get("positions"),
                )
                st.markdown("**Texte prêt à copier :**")
                st.text_area("Texte à copier", txt, height=200, key=f"hist_{idx}")
    elif show_history:
        st.info("Aucun tirage enregistré pour cette session.")

# ----- ONGLET METHODE -----
with tab_methode:
    st.subheader("Comment utiliser cet oracle")
    st.markdown(
        """
### 1. Préparer le tirage
- Pose une **intention claire** ou une question ouverte.
- Respire quelques instants, centre-toi sur ta sensation du moment.
- Quand tu te sens prêt·e, lance le tirage.

### 2. Tirages standard
- **Tirage libre (1 à 5 cartes)** : vue simple, adaptable à ton usage.
- **Tirage en croix (5 cartes)** : lecture globale d’une situation.
- **Tirage du jour** : une seule carte, énergie du moment.

### 3. Tirages avancés par packs
Dans la barre latérale, choisis **“Tirages avancés (packs)”**, puis :

- Un **pack** (relationnel, spirituel, décisionnel, etc.)
- Un **tirage précis** dans ce pack

Chaque tirage avancé :
- possède un **nombre de cartes fixe**,
- une **légende de position** pour chaque carte,
- un **texte prêt à copier** pour ton journal ou tes consultations.

Tu peux t’en servir pour :
- explorer une relation,
- éclairer un choix,
- suivre ton évolution intérieure,
- ou lire ton **“horoscope énergétique”** à 12 cartes.

> Rappelle-toi : l’oracle ne t’enferme pas, il ouvre des pistes de lecture.
        """
    )

# ----- ONGLET TOUTES LES CARTES -----
with tab_cartes:
    st.subheader("Liste complète des cartes & légendes")

    familles_ordre = ["Voie intérieure", "Croissance", "Relations", "Guidance"]

    for fam in familles_ordre:
        cartes_famille = [c for c in CARDS if c["famille"] == fam]
        if not cartes_famille:
            continue

        st.markdown(f"## {fam}")
        for c in cartes_famille:
            st.markdown(
                f"""
**{c['nom']}**

- *Message* : {c['message']}
- *Axe de guidance* : {c['axe']}

---
                """
            )

# ----- ONGLET A PROPOS -----
with tab_apropos:
    st.subheader("À propos de cet oracle")
    st.markdown(
        """
Cet oracle de 48 cartes est conçu comme un **outil de réflexion et d’introspection** :

- Il ne prédit pas l’avenir, il **met en lumière** des dynamiques déjà présentes.
- Chaque carte est une **porte symbolique** : ton ressenti au moment du tirage fait partie de la réponse.
- Les différents tirages (standard & packs) t’aident à regarder :
  - ton quotidien,
  - tes relations,
  - tes choix,
  - ton chemin intérieur,
  - et l’orientation plus globale de ton énergie.

Tu es toujours libre de :
- prendre ce qui résonne,
- laisser ce qui ne parle pas,
- compléter avec ton propre langage, tes pratiques, ta spiritualité.

> L’oracle ne sait rien à ta place.  
> Il t’aide à écouter ce que tu sais déjà, un peu plus profondément.
        """
    )

st.caption("Oracle de 48 cartes — Deck physique virtuel • Tirages standard & avancés par packs • Texte prêt à copier • Historique par session.")
