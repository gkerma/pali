import random
from datetime import datetime
import streamlit as st

st.set_page_config(page_title="Oracle multi-jeux", page_icon="🔮", layout="centered")

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

.totem-border {
    border: 2px solid rgba(255, 190, 120, 0.55) !important;
    box-shadow: 0 0 14px rgba(255, 170, 60, 0.4);
}

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

st.title("🔮 Oracle multi-jeux")
st.write("Oracle 48 cartes, Pāli, runes et I Ching (64 hexagrammes) dans une seule interface.")

# =========================
#       JEUX / DECKS
# =========================

# Oracle 48 cartes (ton jeu principal)
ORACLE48_CARDS = [
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

# Oracle Pāli (mini deck – extensible)
PALI_CARDS = [
    {"nom": "Mettā", "famille": "Pāli", "message": "Bienveillance illimitée envers tous les êtres.", "axe": "Amour inconditionnel"},
    {"nom": "Karunā", "famille": "Pāli", "message": "Compassion face à la souffrance.", "axe": "Cœur ouvert"},
    {"nom": "Mudita", "famille": "Pāli", "message": "Joie empathique pour le bonheur d’autrui.", "axe": "Gratitude partagée"},
    {"nom": "Upekkhā", "famille": "Pāli", "message": "Équanimité, centre stable.", "axe": "Neutralité bienveillante"},
    {"nom": "Sati", "famille": "Pāli", "message": "Attention juste, présence consciente.", "axe": "Pleine conscience"},
    {"nom": "Samādhi", "famille": "Pāli", "message": "Recueillement, unification de l’esprit.", "axe": "Concentration"},
    {"nom": "Paññā", "famille": "Pāli", "message": "Vision claire de la réalité.", "axe": "Sagesse"},
    {"nom": "Karuṇā-bhāvanā", "famille": "Pāli", "message": "Cultiver la compassion.", "axe": "Pratique du cœur"},
    {"nom": "Anicca", "famille": "Pāli", "message": "Tout est impermanent.", "axe": "Lâcher-prise"},
    {"nom": "Dukkha", "famille": "Pāli", "message": "Reconnaître l’insatisfaction pour la dépasser.", "axe": "Lucidité"},
    {"nom": "Anattā", "famille": "Pāli", "message": "Rien n’est un “moi” séparé.", "axe": "Détachement de l’ego"},
    {"nom": "Bhavana", "famille": "Pāli", "message": "Cultiver, développer le mental.", "axe": "Pratique intérieure"},
]

# Runes (Elder Futhark – version résumée)
RUNES_CARDS = [
    {"nom": "Fehu", "famille": "Rune", "message": "Flux, ressources, énergie vitale.", "axe": "Abondance en mouvement"},
    {"nom": "Uruz", "famille": "Rune", "message": "Force brute, santé, puissance.", "axe": "Puissance sauvage"},
    {"nom": "Thurisaz", "famille": "Rune", "message": "Portail, épreuve, protection.", "axe": "Franchir un seuil"},
    {"nom": "Ansuz", "famille": "Rune", "message": "Parole, inspiration, message.", "axe": "Communication inspirée"},
    {"nom": "Raidho", "famille": "Rune", "message": "Voyage, direction, chemin.", "axe": "Alignement du mouvement"},
    {"nom": "Kenaz", "famille": "Rune", "message": "Torche, clarté, artisanat.", "axe": "Révélation"},
    {"nom": "Gebo", "famille": "Rune", "message": "Don, échange, alliance.", "axe": "Partage juste"},
    {"nom": "Wunjo", "famille": "Rune", "message": "Joie, harmonie, accomplissement.", "axe": "Contentement"},
    {"nom": "Hagalaz", "famille": "Rune", "message": "Rupture, tempête, chaos fécond.", "axe": "Réinitialisation"},
    {"nom": "Nauthiz", "famille": "Rune", "message": "Nécessité, tension, frein.", "axe": "Apprendre de la contrainte"},
    {"nom": "Isa", "famille": "Rune", "message": "Glace, pause, stagnation.", "axe": "Immobilité consciente"},
    {"nom": "Jera", "famille": "Rune", "message": "Récolte, cycle, résultat.", "axe": "Patience récompensée"},
    {"nom": "Eihwaz", "famille": "Rune", "message": "Axe, endurance, protection profonde.", "axe": "Résilience"},
    {"nom": "Perthro", "famille": "Rune", "message": "Mystère, destin, hasard.", "axe": "Lâcher prise sur le contrôle"},
    {"nom": "Algiz", "famille": "Rune", "message": "Protection, intuition, lien spirituel.", "axe": "Ancrage sacré"},
    {"nom": "Sowilo", "famille": "Rune", "message": "Soleil, réussite, vitalité.", "axe": "Rayonnement"},
    {"nom": "Tiwaz", "famille": "Rune", "message": "Justice, sacrifice, honneur.", "axe": "Alignement éthique"},
    {"nom": "Berkano", "famille": "Rune", "message": "Naissance, croissance, soin.", "axe": "Nourrir le vivant"},
    {"nom": "Ehwaz", "famille": "Rune", "message": "Coopération, progrès, confiance.", "axe": "Alliances fécondes"},
    {"nom": "Mannaz", "famille": "Rune", "message": "Humain, communauté, identité.", "axe": "Relation à soi et aux autres"},
    {"nom": "Laguz", "famille": "Rune", "message": "Eau, intuition, flux émotionnel.", "axe": "Suivre le courant profond"},
    {"nom": "Inguz", "famille": "Rune", "message": "Germination, potentiel, clôture.", "axe": "Achever pour renaître"},
    {"nom": "Dagaz", "famille": "Rune", "message": "Aube, bascule, illumination.", "axe": "Passage lumière"},
    {"nom": "Othala", "famille": "Rune", "message": "Héritage, foyer, ancêtres.", "axe": "Transmission"},
]

# I Ching – 64 hexagrammes complets (King Wen)
ICHING_CARDS = [
    {"nom": "1. Le Créatif (Qián)", "famille": "I Ching", "message": "Élan créateur, initiative, puissance du ciel.", "axe": "Agir avec force et rectitude"},
    {"nom": "2. Le Réceptif (Kūn)", "famille": "I Ching", "message": "Réceptivité, accueil, puissance de la terre.", "axe": "Coopérer humblement avec ce qui vient"},
    {"nom": "3. La Difficulté initiale", "famille": "I Ching", "message": "Démarrage chaotique, naissance dans la confusion.", "axe": "Organiser le chaos pas à pas"},
    {"nom": "4. La Folie juvénile", "famille": "I Ching", "message": "Immaturité, ignorance, apprentissage nécessaire.", "axe": "Accepter d’apprendre et demander conseil"},
    {"nom": "5. L’Attente", "famille": "I Ching", "message": "Temps de maturation, patience active.", "axe": "Faire confiance au bon moment"},
    {"nom": "6. Le Conflit", "famille": "I Ching", "message": "Tension, opposition, friction verbale ou mentale.", "axe": "Clarifier, éviter l’escalade inutile"},
    {"nom": "7. L’Armée", "famille": "I Ching", "message": "Organisation, discipline, but commun.", "axe": "Mettre de l’ordre et suivre une direction claire"},
    {"nom": "8. La Solidarité", "famille": "I Ching", "message": "Union, rassemblement, cohésion.", "axe": "Choisir consciemment avec qui tu t’associes"},
    {"nom": "9. La Petite Emprise", "famille": "I Ching", "message": "Progression douce, influence limitée.", "axe": "Travailler sur les détails sans forcer"},
    {"nom": "10. La Marche", "famille": "I Ching", "message": "Avancer prudemment, position délicate.", "axe": "Marcher avec respect, sans arrogance"},
    {"nom": "11. La Paix", "famille": "I Ching", "message": "Harmonie, échange fluide, prospérité.", "axe": "Entretenir activement l’équilibre"},
    {"nom": "12. La Stagnation", "famille": "I Ching", "message": "Blocage, fermeture, séparation.", "axe": "Ne pas forcer, purifier et attendre le renouveau"},
    {"nom": "13. Communauté avec les hommes", "famille": "I Ching", "message": "Relations collectives, groupe, partage.", "axe": "Trouver ta juste place dans le collectif"},
    {"nom": "14. Le Grand Avoir", "famille": "I Ching", "message": "Grande richesse, abondance de moyens.", "axe": "Utiliser tes ressources avec noblesse"},
    {"nom": "15. La Modestie", "famille": "I Ching", "message": "Simplicité, humilité, juste mesure.", "axe": "Réduire l’ego pour laisser passer le juste"},
    {"nom": "16. L’Empressement (L’Enthousiasme)", "famille": "I Ching", "message": "Élan, inspiration, enthousiasme contagieux.", "axe": "Canaliser ton élan pour ne pas te disperser"},
    {"nom": "17. La Suivante", "famille": "I Ching", "message": "Suivre ce qui est juste, adhérer à une voie.", "axe": "Choisir consciemment ce que tu suis"},
    {"nom": "18. Travail sur ce qui est corrompu", "famille": "I Ching", "message": "Réparer l’ancien, corriger les erreurs.", "axe": "Regarder les dysfonctionnements sans fuir"},
    {"nom": "19. L’Approche", "famille": "I Ching", "message": "Proximité, rapprochement, arrivée d’une influence.", "axe": "Accueillir ce qui vient avec clarté"},
    {"nom": "20. La Contemplation", "famille": "I Ching", "message": "Regard global, observation, recul.", "axe": "Observer avant d’agir, clarifier ta vision"},
    {"nom": "21. Mordre au travers", "famille": "I Ching", "message": "Déblocage par un acte ferme.", "axe": "Trancher ce qui entrave la vérité"},
    {"nom": "22. La Grâce", "famille": "I Ching", "message": "Beauté, forme, ornement.", "axe": "Soigner la forme sans perdre le fond"},
    {"nom": "23. L’Éclatement", "famille": "I Ching", "message": "Démantèlement, effondrement d’une structure.", "axe": "Laisser tomber ce qui ne tient plus"},
    {"nom": "24. Le Retour", "famille": "I Ching", "message": "Cycle, renaissance, retour à soi.", "axe": "Revenir à la source, recommencer simplement"},
    {"nom": "25. L’Innocence", "famille": "I Ching", "message": "Spontanéité, sincérité, agir sans calcul.", "axe": "Rester droit sans manipuler"},
    {"nom": "26. Force apprivoisée du Grand", "famille": "I Ching", "message": "Maîtrise de grandes forces, retenue.", "axe": "Canaliser ta puissance au lieu de la déchaîner"},
    {"nom": "27. Les Nourritures", "famille": "I Ching", "message": "Ce qui nourrit le corps, le cœur et l’esprit.", "axe": "Veiller à ce que tu donnes et reçois"},
    {"nom": "28. Prépondérance du Grand", "famille": "I Ching", "message": "Charge excessive, tension extrême.", "axe": "Soutenir momentanément, mais alléger à terme"},
    {"nom": "29. L’Abîme (l’Eau)", "famille": "I Ching", "message": "Danger répété, épreuve profonde.", "axe": "Rester sincère et centré au cœur du danger"},
    {"nom": "30. L’Adhérent (le Feu)", "famille": "I Ching", "message": "Clarté, illumination, adhérence.", "axe": "Éclairer sans brûler, voir sans s’attacher"},
    {"nom": "31. L’Influence", "famille": "I Ching", "message": "Attraction mutuelle, résonance.", "axe": "Agir par la douceur, pas par la force"},
    {"nom": "32. La Durée", "famille": "I Ching", "message": "Stabilité dans le temps, constance.", "axe": "Persévérer dans ce qui est juste"},
    {"nom": "33. La Retraite", "famille": "I Ching", "message": "Se retirer à temps, protection.", "axe": "Savoir reculer pour rester intègre"},
    {"nom": "34. La Puissance du Grand", "famille": "I Ching", "message": "Force disponible, affirmation.", "axe": "User de ta puissance avec droiture"},
    {"nom": "35. Le Progrès", "famille": "I Ching", "message": "Avancée rapide, visibilité.", "axe": "Progresser sans arrogance"},
    {"nom": "36. Obscurcissement de la Lumière", "famille": "I Ching", "message": "Lumière blessée, nécessité de se protéger.", "axe": "Préserver ta flamme à l’abri des attaques"},
    {"nom": "37. La Famille", "famille": "I Ching", "message": "Cercle intime, rôles, foyer.", "axe": "Clarifier responsabilités et communication"},
    {"nom": "38. L’Opposition", "famille": "I Ching", "message": "Différences, divergences, polarité.", "axe": "Accepter la différence sans rompre le lien"},
    {"nom": "39. L’Entrave", "famille": "I Ching", "message": "Obstacle, contretemps, difficulté.", "axe": "Changer de perspective plutôt que de forcer"},
    {"nom": "40. La Délivrance", "famille": "I Ching", "message": "Libération après tension, résolution.", "axe": "Relâcher la pression, simplifier"},
    {"nom": "41. La Diminution", "famille": "I Ching", "message": "Réduction, simplification.", "axe": "Alléger, renoncer à l’excès"},
    {"nom": "42. L’Accroissement", "famille": "I Ching", "message": "Croissance, gain, soutien.", "axe": "Offrir et recevoir dans un juste échange"},
    {"nom": "43. La Percée", "famille": "I Ching", "message": "Décision, proclamation, rupture nette.", "axe": "Dire clairement non à ce qui n’est plus acceptable"},
    {"nom": "44. Venir à la rencontre", "famille": "I Ching", "message": "Rencontre puissante, influence soudaine.", "axe": "Rester vigilant face aux forces séduisantes"},
    {"nom": "45. Le Rassemblement", "famille": "I Ching", "message": "Réunion, rassemblement autour d’un centre.", "axe": "Fédérer sans manipuler"},
    {"nom": "46. L’Ascension", "famille": "I Ching", "message": "Progression pas à pas, montée patiente.", "axe": "Gravir les marches avec constance"},
    {"nom": "47. L’Épuisement", "famille": "I Ching", "message": "Contrainte, fatigue, manque de ressources.", "axe": "Ne pas confondre limitation et échec"},
    {"nom": "48. Le Puits", "famille": "I Ching", "message": "Source profonde, ressource commune.", "axe": "Revenir à la source pour se régénérer"},
    {"nom": "49. La Révolution", "famille": "I Ching", "message": "Changement radical, mue nécessaire.", "axe": "Changer de peau avec clarté et timing juste"},
    {"nom": "50. Le Chaudron", "famille": "I Ching", "message": "Transformation alchimique, nourriture spirituelle.", "axe": "Transformer la matière brute en sagesse"},
    {"nom": "51. L’Éveilleur (le Tonnerre)", "famille": "I Ching", "message": "Choc, réveil, secousse.", "axe": "Te laisser réveiller sans paniquer"},
    {"nom": "52. L’Immobilisation (la Montagne)", "famille": "I Ching", "message": "Arrêt, stabilité, silence.", "axe": "Apprendre à rester immobile en conscience"},
    {"nom": "53. Le Développement", "famille": "I Ching", "message": "Croissance lente, maturation progressive.", "axe": "Respecter le rythme naturel des choses"},
    {"nom": "54. La Jeune Mariée", "famille": "I Ching", "message": "Situation secondaire, compromis, lien déséquilibré.", "axe": "Ne pas te sacrifier pour être accepté"},
    {"nom": "55. L’Abondance", "famille": "I Ching", "message": "Plein épanouissement, apogée.", "axe": "Profiter et préparer déjà la suite"},
    {"nom": "56. Le Voyageur", "famille": "I Ching", "message": "Exil, déplacement, passage.", "axe": "Rester léger et correct en terrain étranger"},
    {"nom": "57. Le Doux (le Vent)", "famille": "I Ching", "message": "Influence subtile, persévérance douce.", "axe": "Agir par petites touches répétées"},
    {"nom": "58. Le Joyeux (le Lac)", "famille": "I Ching", "message": "Joie, échange, ouverture.", "axe": "Créer de la joie partagée sans excès"},
    {"nom": "59. La Dispersion", "famille": "I Ching", "message": "Dissoudre les blocages, fluidifier.", "axe": "Faire circuler ce qui était figé"},
    {"nom": "60. La Limite", "famille": "I Ching", "message": "Cadre, mesure, frontière.", "axe": "Poser des limites claires et bienveillantes"},
    {"nom": "61. La Vérité intérieure", "famille": "I Ching", "message": "Sincérité, authenticité, cœur transparent.", "axe": "Aligner parole, acte et cœur"},
    {"nom": "62. Prépondérance du Petit", "famille": "I Ching", "message": "Importance des détails, petites choses décisives.", "axe": "Soigner les petites actions plutôt que les grands gestes"},
    {"nom": "63. Après l’Accomplissement", "famille": "I Ching", "message": "Cycle accompli, ordre établi.", "axe": "Rester vigilant même quand tout semble en place"},
    {"nom": "64. Avant l’Accomplissement", "famille": "I Ching", "message": "Processus inachevé, tension finale.", "axe": "Ne pas relâcher juste avant le passage"},
]

TOTEMS_AMS_CARDS = [
    # Forêt amazonienne
    {
        "nom": "Jaguar",
        "famille": "Totem – Forêt",
        "message": "Puissance silencieuse, instinct affûté.",
        "axe": "Reprendre possession de ta force intérieure",
    },
    {
        "nom": "Anaconda",
        "famille": "Totem – Forêt",
        "message": "Énergie qui entoure, enserre et transforme.",
        "axe": "Laisser mourir une ancienne peau",
    },
    {
        "nom": "Dauphin rose",
        "famille": "Totem – Fleuve",
        "message": "Joie mystérieuse, intelligence ludique.",
        "axe": "Guérir par le jeu et la douceur",
    },
    {
        "nom": "Toucan",
        "famille": "Totem – Forêt",
        "message": "Parole colorée, expression visible.",
        "axe": "Oser dire ta vérité avec couleurs",
    },
    {
        "nom": "Ara bleu",
        "famille": "Totem – Forêt",
        "message": "Communication, liens sociaux, mémoire.",
        "axe": "Soigner la qualité de tes échanges",
    },
    {
        "nom": "Paresseux",
        "famille": "Totem – Forêt",
        "message": "Lenteur sacrée, économie d’énergie.",
        "axe": "Arrêter d’en faire trop, choisir l’essentiel",
    },
    {
        "nom": "Singe capucin",
        "famille": "Totem – Forêt",
        "message": "Curiosité, ruse, improvisation.",
        "axe": "Retrouver le jeu dans la résolution des problèmes",
    },
    {
        "nom": "Fourmilier géant",
        "famille": "Totem – Forêt",
        "message": "Patience, minutie, travail discret.",
        "axe": "Avancer par petites actions répétées",
    },

    # Andes & hauts plateaux
    {
        "nom": "Condor",
        "famille": "Totem – Andes",
        "message": "Vision d’en haut, perspective spirituelle.",
        "axe": "Prendre de la hauteur sur ta situation",
    },
    {
        "nom": "Puma",
        "famille": "Totem – Andes",
        "message": "Force agile, courage en mouvement.",
        "axe": "Passer de l’intention à l’action",
    },
    {
        "nom": "Lama",
        "famille": "Totem – Andes",
        "message": "Porter des charges avec dignité.",
        "axe": "Alléger ce que tu portes pour continuer sereinement",
    },
    {
        "nom": "Alpaga",
        "famille": "Totem – Andes",
        "message": "Douceur, chaleur, ressource partagée.",
        "axe": "Créer du confort pour toi et les autres",
    },
    {
        "nom": "Renard des Andes",
        "famille": "Totem – Andes",
        "message": "Adaptation, discrétion, stratégie.",
        "axe": "Ne pas tout montrer, choisir tes confidences",
    },

    # Rivages, marais, frontières
    {
        "nom": "Caïman",
        "famille": "Totem – Eaux profondes",
        "message": "Présence immobile, attaque fulgurante.",
        "axe": "Attendre le bon moment avant d’agir",
    },
    {
        "nom": "Tortue d’eau douce",
        "famille": "Totem – Eaux lentes",
        "message": "Ancienneté, sagesse lente, protection.",
        "axe": "Bâtir sur le long terme sans précipitation",
    },
    {
        "nom": "Capybara",
        "famille": "Totem – Rive",
        "message": "Vie communautaire, calme social.",
        "axe": "Chercher des environnements où tu peux te détendre",
    },
    {
        "nom": "Grenouille poison",
        "famille": "Totem – Forêt humide",
        "message": "Beauté intense, toxicité potentielle.",
        "axe": "Voir où tu brilles et où tu te fais du mal",
    },

    # Nuit, mystère, médecine
    {
        "nom": "Chauve-souris",
        "famille": "Totem – Nuit",
        "message": "Navigation dans l’obscur, sens subtils.",
        "axe": "Faire confiance à ce que tu ne vois pas clairement",
    },
    {
        "nom": "Tatou",
        "famille": "Totem – Terre",
        "message": "Armure, limites, territoire.",
        "axe": "Clarifier ce qui est à toi et ce qui ne l’est pas",
    },
    {
        "nom": "Ocelot",
        "famille": "Totem – Nuit",
        "message": "Beauté féline, chasse intuitive.",
        "axe": "Suivre tes ressentis plutôt que la logique brute",
    },
    {
        "nom": "Serpent corail",
        "famille": "Totem – Médecine",
        "message": "Danger coloré, pouvoir du venin.",
        "axe": "Respecter tes pouvoirs pour ne pas blesser",
    },
    {
        "nom": "Araçari",
        "famille": "Totem – Forêt",
        "message": "Pont entre branches, transitions souples.",
        "axe": "Te déplacer entre différents mondes sociaux",
    },
    {
        "nom": "Manakin",
        "famille": "Totem – Danse",
        "message": "Parade, séduction, rythme.",
        "axe": "Réintroduire le jeu et la danse dans ta présence",
    },
    {
        "nom": "Seriema",
        "famille": "Totem – Savane",
        "message": "Veille, vigilance, cri d’alerte.",
        "axe": "Ne pas ignorer les signaux précoces",
    },
]

TOTEMS_AMN_CARDS = [
    # Grandes plaines & forêts
    {
        "nom": "Bison",
        "famille": "Totem – Plaines",
        "message": "Puissance collective, abondance partagée.",
        "axe": "Te relier à la force du groupe sans t’oublier",
    },
    {
        "nom": "Loup",
        "famille": "Totem – Meute",
        "message": "Instinct, loyauté, enseignement.",
        "axe": "Honorer tes instincts et ta tribu",
    },
    {
        "nom": "Ours",
        "famille": "Totem – Forêt",
        "message": "Retrait, hibernation, introspection profonde.",
        "axe": "T’autoriser des temps de retrait pour te régénérer",
    },
    {
        "nom": "Aigle",
        "famille": "Totem – Ciel",
        "message": "Vision haute, courage spirituel.",
        "axe": "Regarder plus loin que tes peurs immédiates",
    },
    {
        "nom": "Corbeau",
        "famille": "Totem – Mystère",
        "message": "Magie, transformation, messages de l’invisible.",
        "axe": "Reconnaître les signes que tu reçois déjà",
    },
    {
        "nom": "Coyote",
        "famille": "Totem – Trickster",
        "message": "Humour, paradoxe, leçon déguisée.",
        "axe": "Accepter que l’Univers t’enseigne aussi par la farce",
    },
    {
        "nom": "Lynx",
        "famille": "Totem – Secrets",
        "message": "Discrétion, regard pénétrant.",
        "axe": "Voir sans tout dire, garder le silence juste",
    },
    {
        "nom": "Castor",
        "famille": "Totem – Bâtisseur",
        "message": "Construction, persévérance, habitat.",
        "axe": "Structurer ton quotidien pour servir ton âme",
    },
    {
        "nom": "Cheval mustang",
        "famille": "Totem – Liberté",
        "message": "Élan sauvage, esprit indompté.",
        "axe": "Retrouver une liberté de mouvement intérieure",
    },
    {
        "nom": "Caribou",
        "famille": "Totem – Migration",
        "message": "Endurance, cycles de déplacement.",
        "axe": "Accepter que ta route passe par plusieurs territoires",
    },
    {
        "nom": "Hibou",
        "famille": "Totem – Nuit",
        "message": "Voir dans l’obscurité, sagesse silencieuse.",
        "axe": "Écouter ta connaissance intuitive même la nuit",
    },
    {
        "nom": "Baleine",
        "famille": "Totem – Océan",
        "message": "Mémoire ancienne, chant, profondeur émotionnelle.",
        "axe": "Honorer les mémoires profondes qui remontent",
    },
    {
        "nom": "Orque",
        "famille": "Totem – Clan",
        "message": "Famille d’âme, coordination, puissance.",
        "axe": "Trouver et nourrir ta véritable famille d’âme",
    },
    {
        "nom": "Raton laveur",
        "famille": "Totem – Masques",
        "message": "Adaptation, rôle, débrouillardise.",
        "axe": "Voir quels masques tu portes encore par sécurité",
    },
]

TOTEMS_ASIA_CARDS = [
    # Forêt & montagne
    {
        "nom": "Tigre",
        "famille": "Totem – Forêt",
        "message": "Puissance féline, détermination, instinct.",
        "axe": "Oser défendre ton territoire énergétique",
    },
    {
        "nom": "Panda",
        "famille": "Totem – Douce force",
        "message": "Force tranquille, douceur, équilibre yin.",
        "axe": "T’autoriser à être fort et tendre en même temps",
    },
    {
        "nom": "Grue",
        "famille": "Totem – Ciel / Terre",
        "message": "Grâce, longévité, pas mesuré.",
        "axe": "Alléger tes mouvements et respecter ton rythme",
    },
    {
        "nom": "Dragon",
        "famille": "Totem – Esprit",
        "message": "Puissance spirituelle, feu intérieur.",
        "axe": "Reconnaître ton pouvoir créateur sans l’abuser",
    },
    {
        "nom": "Tortue dragon (tortue sacrée)",
        "famille": "Totem – Gardien",
        "message": "Protection, sagesse lente, stabilité.",
        "axe": "Construire sur du long terme, calmement",
    },
    {
        "nom": "Serpent",
        "famille": "Totem – Transformation",
        "message": "Mue, guérison, énergie vitale.",
        "axe": "Accepter de laisser tomber une ancienne identité",
    },
    {
        "nom": "Macaque",
        "famille": "Totem – Esprit joueur",
        "message": "Intelligence vive, imitation, troupe.",
        "axe": "Observer ce que tu reproduis sans t’en rendre compte",
    },
    {
        "nom": "Yak",
        "famille": "Totem – Haute montagne",
        "message": "Endurance, support, service.",
        "axe": "Soutenir sans te sacrifier entièrement",
    },
    {
        "nom": "Éléphant d’Asie",
        "famille": "Totem – Mémoire",
        "message": "Stabilité, mémoire, loyauté.",
        "axe": "Honorer ton histoire sans y rester coincé",
    },
    {
        "nom": "Phénix",
        "famille": "Totem – Renaissance",
        "message": "Mort et renaissance, transmutation par le feu.",
        "axe": "Accepter les cycles de destruction créatrice",
    },
    {
        "nom": "Carpe koï",
        "famille": "Totem – Eau",
        "message": "Persévérance, sens du courant, ascension.",
        "axe": "Continuer à avancer malgré les contre-courants",
    },
    {
        "nom": "Loutre",
        "famille": "Totem – Joie",
        "message": "Jeu, complicité, plaisir simple.",
        "axe": "Ramener du jeu dans tes relations",
    },
    {
        "nom": "Cigale",
        "famille": "Totem – Cycle",
        "message": "Longue maturation, expression sonore.",
        "axe": "Respecter les longs temps de préparation avant l’émergence",
    },
    {
        "nom": "Griffon (totem hybride)",
        "famille": "Totem – Gardien des seuils",
        "message": "Protection de trésors intérieurs.",
        "axe": "Protéger ce qui est sacré en toi",
    },
]

DECKS = {
    "Oracle 48 cartes": ORACLE48_CARDS,
    "Oracle Pāli": PALI_CARDS,
    "Runes (Elder Futhark)": RUNES_CARDS,
    "I Ching (64 hexagrammes)": ICHING_CARDS,
    "Totems animaux — Amérique du Sud": TOTEMS_AMS_CARDS,
    "Totems animaux — Amérique du Nord": TOTEMS_AMN_CARDS,
    "Totems animaux — Asie": TOTEMS_ASIA_CARDS,
}

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
    {
        "id": "chakana_andine",
        "nom": "Chakana andine (7 cartes)",
        "pack": "Spirituel",
        "nb": 7,
        "positions": [
            "Centre — Cœur de ta situation",
            "Nord — Sagesse / Ancêtres / Esprit",
            "Sud — Enfant intérieur / Joie / Guérison",
            "Est — Nouveau départ / Vision / Idée",
            "Ouest — Transformation / Mort symbolique",
            "Haut — Guidance supérieure",
            "Bas — Ancrage / Corps / Racines",
        ],
    },
    {
        "id": "voyage_chamanique",
        "nom": "Voyage chamanique",
        "pack": "Spirituel",
        "nb": 6,
        "positions": [
            "Entrée du voyage — Seuil, intention, porte d’accès",
            "Guide — Présence qui t’accompagne ou t’ouvre le chemin",
            "Tunnel / Passage — Ce que tu traverses actuellement",
            "Animal totem — Force ou allié qui se présente",
            "Message — Enseignement principal de ce voyage",
            "Retour / Intégration — Comment revenir et intégrer dans ta vie",
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

    {
        "Totems – Médecine animale": {
            "Allié du moment (1 carte)": [
                ("Animal allié", "La présence animale qui t’accompagne maintenant.")
            ],
            "Médecine du jour (3 cartes)": [
                ("Totem", "L’énergie animale qui se présente."),
                ("Défi", "Ce qu’elle veut t’aider à dépasser."),
                ("Médecine", "L’enseignement qu’elle t’invite à intégrer."),
            ],
            "Totem d’ombre (3 cartes)": [
                ("Ombre animale", "La part instinctive refoulée."),
                ("Risque", "Le danger si tu résistes."),
                ("Intégration", "Comment domestiquer cette énergie."),
            ],
            "Totem de pouvoir (4 cartes)": [
                ("Animal principal", "Force en action."),
                ("Voie haute", "Ton potentiel lumineux."),
                ("Voie basse", "Quand la puissance déborde."),
                ("Conseil", "Comment canaliser cette énergie."),
            ],
            "Roue chamanique (4 directions)": [
                ("Nord", "Sagesse / Ancêtres / Vision supérieure."),
                ("Sud", "Enfance / Joie / Guérison émotionnelle."),
                ("Est", "Nouveau départ / Pensée / Inspiration."),
                ("Ouest", "Transformation / Mort symbolique / Initiation."),
            ],
            "Chemin de médecine (5 cartes)": [
                ("Passé animal", "L’énergie animale qui t’a construit(e)."),
                ("Présent", "Ton énergie totem actuelle."),
                ("Défi", "Le blocage que l’animal pointe."),
                ("Allié caché", "Ce qui t’aide sans que tu le voies."),
                ("Médecine finale", "L’enseignement global du totem pour cette période."),
            ],
        },
    }
]

PACKS = sorted(sorted({s["pack"] for s in SPREADS}))

# =========================
#   PARAMÈTRES & ÉTAT
# =========================

st.sidebar.header("🔁 Jeu / système")
system_name = st.sidebar.selectbox("Choisir le jeu", list(DECKS.keys()))
CARDS = DECKS[system_name]

st.sidebar.header("⚙️ Type de tirage")

type_options = [
    "Standard (libre / croix / jour)",
    "Tirages avancés (packs)",
]

# Mode I Ching classique seulement pour le deck I Ching
if system_name.startswith("I Ching"):
    type_options.append("Tirage I Ching classique (6 traits)")

tirage_mode_type = st.sidebar.radio("Choisir le type", type_options)

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

    # On force le mode libre pour les autres jeux que l’oracle 48
    if system_name != "Oracle 48 cartes":
        mode_radio = "Tirage libre (1–5 cartes)"

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

    # style spécial totems
    is_totem = system_name.startswith("Totems animaux")

    html = (
        '<div class="flip-card">'
        '<div class="flip-card-inner">'
        f'<div class="flip-card-front{" totem-border" if is_totem else ""}">'
        f'{pos_html}'
        f'<h3>{front_title} — {carte["nom"]}</h3>'
        f'<p><b>Famille :</b> {carte["famille"]}</p>'
        '<p class="flip-hint">Retourne la carte (survol / toucher) pour voir le message.</p>'
        '</div>'
        f'<div class="flip-card-back{" totem-border" if is_totem else ""}">'
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

def build_summary(tirage, mode_label, question, timestamp, daily, positions=None, system=None):
    lines = []
    titre = "Tirage du jour" if daily else "Tirage de l’oracle"
    lines.append(f"{titre} — {timestamp}")
    if system:
        lines.append(f"Jeu : {system}")
    if question and question.strip():
        lines.append(f"Question : {question.strip()}")
    lines.append(f"Mode : {mode_label}")
    lines.append("")

    if positions is not None:
        for i, (c, pos) in enumerate(zip(tirage, positions), start=1):
            lines.append(
                f"Carte {i} — {c['nom']} [{pos}]\n"
                f"  Message : {c['message']}\n"
                f"  Axe : {c['axe']}"
            )
    else:
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
#   HELPERS I CHING CLASSIQUE
# =========================

def iching_line_symbol(line_type: str) -> str:
    """Petit dessin ASCII du trait."""
    if line_type == "yang":
        return "━━━━━━━"          # trait plein
    if line_type == "yin":
        return "━━   ━━"          # trait brisé
    if line_type == "old_yang":
        return "━━━━━━━  o"       # yang mutant
    if line_type == "old_yin":
        return "━━   ━━  x"       # yin mutant
    return "?"

def iching_line_label(line_type: str) -> str:
    mapping = {
        "yang": "Yang stable",
        "yin": "Yin stable",
        "old_yang": "Yang mutant (tend vers Yin)",
        "old_yin": "Yin mutant (tend vers Yang)",
    }
    return mapping.get(line_type, line_type)

def iching_nuclear_bits(bits_main):
    """
    bits_main : 6 bits (bas → haut).
    Nucléaire (hu gua) classique :
    - trigramme bas : lignes 2,3,4
    - trigramme haut : lignes 3,4,5
    => [l2, l3, l4, l3, l4, l5]
    """
    return [
        bits_main[1],
        bits_main[2],
        bits_main[3],
        bits_main[2],
        bits_main[3],
        bits_main[4],
    ]

def iching_complementary_bits(bits_main):
    """
    Complémentaire : inversion de toutes les lignes (yin ↔ yang).
    """
    return [1 - b for b in bits_main]

# Trigrammes selon binaire (bas → haut)
# 111 ☰ Ciel, 110 ☱ Lac, 101 ☲ Feu, 100 ☳ Tonnerre,
# 011 ☴ Vent, 010 ☵ Eau, 001 ☶ Montagne, 000 ☷ Terre
TRIGRAM_BITS_TO_INDEX = {
    (1, 1, 1): 0,  # ☰
    (1, 1, 0): 1,  # ☱
    (1, 0, 1): 2,  # ☲
    (1, 0, 0): 3,  # ☳
    (0, 1, 1): 4,  # ☴
    (0, 1, 0): 5,  # ☵
    (0, 0, 1): 6,  # ☶
    (0, 0, 0): 7,  # ☷
}

# Tableau King Wen : [lower trigram index][upper trigram index] → numéro d’hexagramme
HEX_KINGWEN_FROM_TRIGRAMS = [
    # upper:  ☰   ☱   ☲   ☳   ☴   ☵   ☶   ☷
    [1,   43, 14, 34, 9,   5,  26, 11],  # lower ☰
    [10,  58, 38, 54, 61, 60, 41, 19],  # lower ☱
    [13,  49, 30, 55, 37, 63, 22, 36],  # lower ☲
    [25,  17, 21, 51, 42, 3,  27, 24],  # lower ☳
    [44,  28, 50, 32, 57, 48, 18, 46],  # lower ☴
    [6,   47, 64, 40, 59, 29, 4,  7],   # lower ☵
    [33,  31, 56, 62, 53, 39, 52, 15],  # lower ☶
    [12,  45, 35, 16, 20, 8,  23, 2],   # lower ☷
]

def hex_number_from_bits(bits6):
    """bits6 : liste de 6 bits (bas → haut), retourne le numéro d’hexagramme King Wen."""
    lower_bits = tuple(bits6[0:3])
    upper_bits = tuple(bits6[3:6])
    lower_idx = TRIGRAM_BITS_TO_INDEX[lower_bits]
    upper_idx = TRIGRAM_BITS_TO_INDEX[upper_bits]
    return HEX_KINGWEN_FROM_TRIGRAMS[lower_idx][upper_idx]

def iching_main_and_changed(traits):
    """
    traits: liste de 6 valeurs parmi ["yin","yang","old_yin","old_yang"] (bas → haut)
    retourne (num_main, num_changed, bits_main, bits_changed)
    """
    bits_main = [1 if t in ("yang", "old_yang") else 0 for t in traits]
    bits_changed = []
    for t, b in zip(traits, bits_main):
        if t == "old_yang":
            bits_changed.append(0)  # yang mutant → yin
        elif t == "old_yin":
            bits_changed.append(1)  # yin mutant → yang
        else:
            bits_changed.append(b)

    num_main = hex_number_from_bits(bits_main)
    num_changed = hex_number_from_bits(bits_changed)
    return num_main, num_changed, bits_main, bits_changed

def build_iching_classic_summary(
    main_card,
    changed_card,
    nuclear_card,
    complementary_card,
    num_main,
    num_changed,
    num_nuclear,
    num_complementary,
    traits,
    question,
    timestamp,
    system,
):
    lines = []
    lines.append(f"Tirage I Ching classique (6 traits) — {timestamp}")
    if system:
        lines.append(f"Jeu : {system}")
    if question and question.strip():
        lines.append(f"Question : {question.strip()}")
    lines.append("")
    lines.append("Traits (du bas vers le haut) :")
    for i, t in enumerate(traits, start=1):
        symbol = iching_line_symbol(t)
        label = iching_line_label(t)
        lines.append(f"  Ligne {i} : {symbol} — {label}")
    lines.append("")
    # Hexagramme principal
    lines.append(f"Hexagramme principal : #{num_main} — {main_card['nom']}")
    lines.append(f"  Message : {main_card['message']}")
    lines.append(f"  Axe : {main_card['axe']}")
    # Mutation
    if num_changed is not None and changed_card is not None and num_changed != num_main:
        lines.append("")
        lines.append(f"Hexagramme de mutation : #{num_changed} — {changed_card['nom']}")
        lines.append(f"  Message : {changed_card['message']}")
        lines.append(f"  Axe : {changed_card['axe']}")
    # Nucléaire
    if num_nuclear is not None and nuclear_card is not None:
        lines.append("")
        lines.append(f"Hexagramme nucléaire : #{num_nuclear} — {nuclear_card['nom']}")
        lines.append(f"  Message : {nuclear_card['message']}")
        lines.append(f"  Axe : {nuclear_card['axe']}")
    # Complémentaire
    if num_complementary is not None and complementary_card is not None:
        lines.append("")
        lines.append(f"Hexagramme complémentaire : #{num_complementary} — {complementary_card['nom']}")
        lines.append(f"  Message : {complementary_card['message']}")
        lines.append(f"  Axe : {complementary_card['axe']}")
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

    # ---------- STANDARD ----------
    if tirage_mode_type == "Standard (libre / croix / jour)":
        btn_label = "Tirer la carte du jour ✨" if daily_mode else "Tirer les cartes ✨"

        if st.button(btn_label):
            if system_name == "Oracle 48 cartes" and mode_radio == "Tirage en croix (5 cartes)" and not daily_mode:
                tirage = random.sample(CARDS, 5)
                mode_label = "Tirage en croix (5 cartes)"
            else:
                tirage = random.sample(CARDS, nb_cartes_standard)
                mode_label = "Tirage libre (1–5 cartes)"

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            st.session_state["history"].append(
                {
                    "datetime": timestamp,
                    "system": system_name,
                    "mode_type": "standard",
                    "mode_label": mode_label,
                    "daily": daily_mode,
                    "question": question.strip(),
                    "cards": tirage,
                    "positions": None,
                }
            )

            st.subheader(f"🔮 Résultat du tirage ({system_name})")

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

            summary_text = build_summary(tirage, mode_label, question, timestamp, daily_mode, system=system_name)
            st.markdown("#### 📝 Texte prêt à copier")
            st.text_area("Texte à copier", summary_text, height=220)

    # ---------- TIRAGES AVANCÉS ----------
    elif tirage_mode_type == "Tirages avancés (packs)":
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
                    "system": system_name,
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

            st.subheader(f"🔮 Résultat — {selected_spread['nom']} ({system_name})")
            st.markdown(f"_Pack : **{selected_spread['pack']}**_")
            if question.strip():
                st.markdown(f"**Intention :** _{question}_")
                st.write("---")

            for i, (c, pos) in enumerate(zip(tirage, positions), start=1):
                afficher_carte(c, f"Carte {i}", pos)

            summary_text = build_summary(
                tirage,
                mode_label,
                question,
                timestamp,
                False,
                positions=positions,
                system=system_name,
            )
            st.markdown("#### 📝 Texte prêt à copier")
            st.text_area("Texte à copier", summary_text, height=220)

    # ---------- TIRAGE I CHING CLASSIQUE HARDCORE ----------
    elif tirage_mode_type.startswith("Tirage I Ching classique"):
        if not system_name.startswith("I Ching"):
            st.warning("Le tirage I Ching classique est réservé au jeu I Ching.")
        else:
            if st.button("Lancer le tirage I Ching classique ✨"):
                # 6 traits, bas → haut
                traits = [random.choice(["yin", "yang", "old_yin", "old_yang"]) for _ in range(6)]
                num_main, num_changed, bits_main, bits_changed = iching_main_and_changed(traits)

                # Hexagramme principal
                main_hex = ICHING_CARDS[num_main - 1]

                # Hexagramme de mutation (si différent)
                changed_hex = ICHING_CARDS[num_changed - 1] if num_changed != num_main else None

                # Hexagramme nucléaire
                bits_nuclear = iching_nuclear_bits(bits_main)
                num_nuclear = hex_number_from_bits(bits_nuclear)
                nuclear_hex = ICHING_CARDS[num_nuclear - 1]

                # Hexagramme complémentaire
                bits_complementary = iching_complementary_bits(bits_main)
                num_complementary = hex_number_from_bits(bits_complementary)
                complementary_hex = ICHING_CARDS[num_complementary - 1]

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                st.session_state["history"].append(
                    {
                        "datetime": timestamp,
                        "system": system_name,
                        "mode_type": "iching_classic",
                        "mode_label": "Tirage I Ching classique (6 traits)",
                        "daily": False,
                        "question": question.strip(),
                        # on stocke juste références numériques, les cartes seront recalculées
                        "traits": traits,
                        "hex_num_main": num_main,
                        "hex_num_changed": num_changed,
                        "hex_num_nuclear": num_nuclear,
                        "hex_num_complementary": num_complementary,
                    }
                )

                st.subheader("🔮 Tirage I Ching classique (6 traits)")

                if question.strip():
                    st.markdown(f"**Intention :** _{question}_")
                    st.write("---")

                st.markdown("#### Traits (du bas vers le haut)")
                for i, t in enumerate(traits, start=1):
                    symbol = iching_line_symbol(t)
                    label = iching_line_label(t)
                    st.markdown(f"- Ligne {i} : `{symbol}` — {label}")

                st.write("---")
                st.markdown(f"### Hexagramme principal — #{num_main}")
                afficher_carte(main_hex, "Hexagramme principal")

                if changed_hex is not None and num_changed != num_main:
                    st.markdown(f"### Hexagramme de mutation — #{num_changed}")
                    afficher_carte(changed_hex, "Hexagramme de mutation")

                st.markdown(f"### Hexagramme nucléaire — #{num_nuclear}")
                afficher_carte(nuclear_hex, "Hexagramme nucléaire")

                st.markdown(f"### Hexagramme complémentaire — #{num_complementary}")
                afficher_carte(complementary_hex, "Hexagramme complémentaire")

                summary_text = build_iching_classic_summary(
                    main_hex,
                    changed_hex,
                    nuclear_hex,
                    complementary_hex,
                    num_main,
                    num_changed,
                    num_nuclear,
                    num_complementary,
                    traits,
                    question,
                    timestamp,
                    system_name,
                )
                st.markdown("#### 📝 Texte prêt à copier")
                st.text_area("Texte à copier", summary_text, height=320)

    # ----- Historique -----
    if show_history and st.session_state["history"]:
        st.write("---")
        st.subheader("📚 Historique des tirages (session)")

        for idx, entry in enumerate(reversed(st.session_state["history"]), start=1):
            titre_hist = f"{idx}. {entry['datetime']} — {entry['mode_label']} — [{entry.get('system','')}]"
            if entry.get("daily"):
                titre_hist += " (tirage du jour)"
            if entry.get("mode_type") == "advanced":
                titre_hist += f" — pack {entry.get('pack','')}"

            with st.expander(titre_hist, expanded=False):
                if entry["question"]:
                    st.markdown(f"**Intention :** _{entry['question']}_")
                st.write("")

                mode_type = entry.get("mode_type", "standard")
                positions = entry.get("positions")

                # HISTORIQUE : I CHING CLASSIQUE
                if mode_type == "iching_classic":
                    traits = entry.get("traits", [])
                    num_main = entry.get("hex_num_main")
                    num_changed = entry.get("hex_num_changed")
                    num_nuclear = entry.get("hex_num_nuclear")
                    num_complementary = entry.get("hex_num_complementary")

                    if traits:
                        st.markdown("**Traits (du bas vers le haut) :**")
                        for i, t in enumerate(traits, start=1):
                            symbol = iching_line_symbol(t)
                            label = iching_line_label(t)
                            st.markdown(f"- Ligne {i} : `{symbol}` — {label}")
                        st.write("")

                    main_hex = ICHING_CARDS[num_main - 1] if num_main else None
                    changed_hex = ICHING_CARDS[num_changed - 1] if num_changed and num_changed != num_main else None
                    nuclear_hex = ICHING_CARDS[num_nuclear - 1] if num_nuclear else None
                    complementary_hex = ICHING_CARDS[num_complementary - 1] if num_complementary else None

                    if main_hex is not None:
                        st.markdown(f"**Hexagramme principal — #{num_main}**")
                        afficher_carte(main_hex, "Hexagramme principal")

                    if changed_hex is not None:
                        st.markdown(f"**Hexagramme de mutation — #{num_changed}**")
                        afficher_carte(changed_hex, "Hexagramme de mutation")

                    if nuclear_hex is not None:
                        st.markdown(f"**Hexagramme nucléaire — #{num_nuclear}**")
                        afficher_carte(nuclear_hex, "Hexagramme nucléaire")

                    if complementary_hex is not None:
                        st.markdown(f"**Hexagramme complémentaire — #{num_complementary}**")
                        afficher_carte(complementary_hex, "Hexagramme complémentaire")

                    txt = build_iching_classic_summary(
                        main_hex,
                        changed_hex,
                        nuclear_hex,
                        complementary_hex,
                        num_main,
                        num_changed,
                        num_nuclear,
                        num_complementary,
                        traits,
                        entry["question"],
                        entry["datetime"],
                        entry.get("system"),
                    )
                    st.markdown("**Texte prêt à copier :**")
                    st.text_area("Texte à copier", txt, height=320, key=f"hist_{idx}")

                # HISTORIQUE : AUTRES MODES
                else:
                    if positions:
                        for i, (c, pos) in enumerate(zip(entry["cards"], positions), start=1):
                            afficher_carte(c, f"Carte {i}", pos)
                    else:
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
                        system=entry.get("system"),
                    )
                    st.markdown("**Texte prêt à copier :**")
                    st.text_area("Texte à copier", txt, height=200, key=f"hist_{idx}")
    elif show_history:
        st.info("Aucun tirage enregistré pour cette session.")

# ----- ONGLET METHODE -----
with tab_methode:
    st.subheader("Comment utiliser cet oracle multi-jeux")
    st.markdown(
        """
### 1. Choisir le jeu
Dans la barre latérale :

- **Oracle 48 cartes** : ton oracle principal, structuré en 4 familles.
- **Oracle Pāli** : mots-clés de la tradition pālie, orientés sur la pratique intérieure.
- **Runes (Elder Futhark)** : archétypes nordiques, force, cycles, épreuves, protection.
- **I Ching (64 hexagrammes)** : lecture des processus, mutations, cycles.

### 2. Type de tirage
- **Standard** : tirage libre (tous les jeux) + tirage en croix (oracle 48).
- **Packs avancés** : tirages structurés (relationnels, décisionnels, spirituels, etc.).
- **Tirage I Ching classique (6 traits)** :
  - 6 traits tirés du bas vers le haut.
  - Hexagramme principal calculé par trigrammes.
  - Hexagramme de mutation en fonction des lignes changeantes.

### 3. Intégrer le message
- Lis chaque carte / hexagramme comme un **miroir symbolique**.
- Le **texte prêt à copier** permet de garder trace dans un journal ou une consultation.
- Tu peux comparer le même tirage (packs) avec différents jeux.
        """
    )

# ----- ONGLET TOUTES LES CARTES -----
with tab_cartes:
    st.subheader(f"Cartes du jeu actuel : {system_name}")

    familles = sorted(sorted({c["famille"] for c in CARDS}))
    for fam in familles:
        cartes_famille = [c for c in CARDS if c["famille"] == fam]
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
    st.subheader("À propos de cet oracle multi-jeux")
    st.markdown(
        """
Cet outil rassemble plusieurs **systèmes symboliques** dans la même interface :

- un **oracle de 48 cartes** original,
- un mini-oracle **Pāli**,
- les **runes nordiques** (Elder Futhark),
- les **64 hexagrammes du I Ching** en ordre King Wen,
- un **mode I Ching classique** avec 6 traits, hexagramme principal et hexagramme de mutation.

L’objectif n’est pas de prédire l’avenir, mais d’ouvrir des
**espaces de lecture et d’écoute** de ce que tu vis.

Tu peux :
- explorer une question avec plusieurs systèmes,
- garder trace via le texte prêt à copier,
- étendre les decks en ajoutant tes propres cartes dans le code.

> La technique est précise, mais l’interprétation reste vivante :  
> c’est toi le véritable oracle.
        """
    )

st.caption("Oracle multi-jeux — Oracle 48 cartes • Pāli • Runes • I Ching (64) • Tirages standard & avancés • Tirage I Ching classique • Historique • Texte prêt à copier.")
