import os
import openai
from dotenv import load_dotenv
from utilities import *
from flask import Flask, request, jsonify,render_template

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")
messages =  []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/message", methods=["POST"])
def message():
    user_input = request.form["message"]
    gpt_response = chat_gpt(user_input,messages)
    is_code, language = extract_language(gpt_response)
    return jsonify({"message": gpt_response, "language": language, "is_code":is_code})

if __name__ == '__main__':
    app.run(debug=True)
