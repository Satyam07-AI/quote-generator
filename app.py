import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Your custom quotes
quotes = [
    "Made by SAT 💙 Keep going!",
    "Winners are just ex-losers who never gave up.",
    "Don’t wait for people to believe in you. Make them watch. Make them regret ever doubting you.",
    "Don’t waste energy on proving a point emotionally. Prove it by performance.",
    "Outperform. Outdeliver. Outgrind. Outshine.",
    "Be honest with yourself even if it hurts. Truth burns, but it also purifies. Denial delays success. That’s how you take souls in real life.",
    "Stop blaming others — it's YOUR life. Victim mode is broken.",
    "Quit everything that distracts. No more half-focus.",
    "Track progress daily, even if it’s 1%. Small wins compound.",
    "Be okay staying alone if you're becoming better. Legends are built in isolation, not in party invites.",
    "Don’t impress. Build the real you. You’re not here to look cool. You’re here to be undeniable."
]



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quote')
def get_quote():
    quote = random.choice(quotes)
    return jsonify({'quote': quote})





