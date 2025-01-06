from flask import Flask, render_template, request, jsonify
import openai
from security.auth import authenticate_user
from database.nutrition import get_nutrition_info

app = Flask(__name__)

# OpenAI API key
openai.api_key = "your_openai_api_key_here"

# Welcome Page
@app.route("/")
def welcome():
    return render_template("index.html")

# Chat Page
@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_message = request.json.get("message")
        response = get_ai_response(user_message)
        return jsonify({"response": response})
    return render_template("chat.html")

# Account Page
@app.route("/account")
def account():
    return render_template("account.html")

# OpenAI Response Handler
def get_ai_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}],
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
