# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return "Bienvenue, prenez place..."


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------


@app.get("/presentation")
def presentation():
    return """
    <h1>David Kouakou</h1>
    <p>Je suis étudiant en <strong>deuxième année d'informatique</strong>.</p>
    <img src="https://i0.wp.com/longreads.com/wp-content/uploads/2024/03/Hacking-RL-final.jpg?fit=2400%2C1400&ssl=1" width="100">
    <h2>Ce que j'aime</h2>
    <ul>
        <li>Les jeux vidéo</li>
        <li>Le sport</li>
        <li>Le code (bientôt !)</li>
    </ul>
    """

@app.get("/loisirs")
def loisirs():
    return "Mes loisirs sont l'informatique, les jeux vidéos et le sport."

# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
