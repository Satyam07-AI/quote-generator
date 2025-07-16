from flask import Flask, render_template
import quote
import random

app = Flask(__name__)

topics = ["success", "life", "dream", "discipline", "motivation", "learning", "hustle"]

@app.route('/')
def home():
    try:
        topic = random.choice(topics)
        result = quote.quote(topic)

        # ✅ Always extract ONE quote only
        if isinstance(result, list) and len(result) > 0:
            chosen = result[0]
        elif isinstance(result, dict):
            chosen = result
        else:
            chosen = {'quote': "Keep going anyway.", 'author': "Unknown"}

        quote_text = chosen.get('quote', 'Keep going anyway.')
        author = chosen.get('author', 'Unknown')

    except Exception as e:
        print("Error:", e)
        quote_text = "Do your best anyway."
        author = "Mother Teresa"

    return render_template('index.html', quote=quote_text, author=author)

if __name__ == '__main__':
    app.run(debug=True)



