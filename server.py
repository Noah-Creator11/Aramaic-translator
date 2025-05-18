
from flask import Flask, request, jsonify
import openai

openai.api_key = "DEIN_API_KEY"  # <-- Hier deinen API-Schlüssel einfügen

app = Flask(__name__)

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text")
    target = data.get("target", "Aramäisch")

    prompt = f"Übersetze folgenden Text ins {target}:

\"{text}\""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        translated_text = response.choices[0].message["content"]
        return jsonify({"translation": translated_text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
