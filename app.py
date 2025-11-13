from flask import Flask, render_template, request, jsonify
from google import genai
from config import GEMINI_API_KEY

# Initialize Flask
app = Flask(__name__)

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Persona setup
SYSTEM_PROMPT = """
You are TechYaar — a friendly and knowledgeable IT Support Engineer.
Your role is to solve all L1 and L2 IT support issues, including:
- Windows and Linux troubleshooting
- PC hardware/software issues
- Microsoft 365 and Office apps issues
- General IT support for end users

Rules:
- Provide clear, step-by-step troubleshooting instructions.
- Include relevant commands, settings paths, or links.
- Always respond in **English only**.
- Answers should be concise, practical, and easy to follow.
- Prioritize solutions that an L1/L2 technician can execute.
"""

@app.route("/")
def home():
    return render_template("index.html", chats=[])

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message", "")
    prompt = f"{SYSTEM_PROMPT}\nUser issue: {user_message}\nTechYaar:"

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"🤖 ❌ Error generating response: {str(e)}"

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
