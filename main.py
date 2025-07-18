from flask import Flask, render_template

app = Flask(__name__)

# Список демонів
demons = [
    {"name": "Tartarus", "creator": "Dolphy", "difficulty": "Extreme Demon", "id": 65340217},
    {"name": "Acheron", "creator": "GrenadeOfTacos", "difficulty": "Extreme Demon", "id": 88245923},
    {"name": "Slaughterhouse", "creator": "Icedcave", "difficulty": "Extreme Demon", "id": 77317401}
]

@app.route("/")
def index():
    return render_template("index.html", demons=demons)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
