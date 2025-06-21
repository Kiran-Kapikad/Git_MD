from flask import Flask
import random

app = Flask(__name__)

# A few cool facts
facts = [
    "Honey never spoils.",
    "Bananas are berries, but strawberries aren’t!",
    "Octopuses have three hearts.",
    "There are more stars in the universe than grains of sand on Earth.",
    "A day on Venus is longer than its year."
]

@app.route("/")
def fun_fact():
    # Return a random fact
    return f"🤔 Fun Fact: {random.choice(facts)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

