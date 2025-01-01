from flask import Flask, request, jsonify, render_template
from openai import OpenAI  # Import OpenAI class
from prompt_engineering import generate_prompt  # Import the generate_prompt function

# Initialize Flask app
app = Flask(__name__)

client = OpenAI(api_key='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')  # API key remains visible
GPT_MODEL = "gpt-4-1106-preview"  # Specify the model to use

def chat_gpt(goal, diet_goal, diet_type, include_cardio, gym_days, cardio_days, fitness_level, location):
    try:
        # Use the generate_prompt function from prompt_engineering.py
        prompt = generate_prompt(goal, diet_goal, diet_type, include_cardio, gym_days, cardio_days, fitness_level, location)
        
        # Call OpenAI API to get the response
        response = client.chat.completions.create(
            model=GPT_MODEL,
            messages=[
                {"role": "system", "content": "You are a fitness and diet assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error occurred: {str(e)}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    goal = data.get("goal")
    diet_goal = data.get("diet_goal")
    diet_type = data.get("diet_type")
    include_cardio = data.get("include_cardio")
    gym_days = data.get("gym_days")
    cardio_days = data.get("cardio_days")
    fitness_level = data.get("fitness_level")
    location = data.get("location")

    if not all([goal, diet_goal, diet_type, gym_days, cardio_days, fitness_level, location]):
        return jsonify({"error": "Missing required fields"}), 400

    answer = chat_gpt(goal, diet_goal, diet_type, include_cardio, gym_days, cardio_days, fitness_level, location)

    if answer:
        # Returning HTML content as part of the response
        return jsonify({"answer": answer})  # Send raw HTML content here
    else:
        return jsonify({"error": "Failed to get a response from OpenAI."}), 500


if __name__ == "__main__":
    app.run(debug=True)
