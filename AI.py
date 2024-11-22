import os
from flask import Flask, render_template, request
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

app = Flask(__name__)

# Initialize the ChatCompletionsClient
client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(os.environ.get("GITHUB_TOKEN")),
)

available_models = ["gpt-4o-mini", "gpt-4o", "o1-mini", "o1-preview"]

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_input = request.form["message"]
        selected_model = request.form["model"]
        if user_input.lower() in ['quit', 'q']:
            return render_template("index.html", response="Goodbye!", models=available_models)
        if user_input:
            try:
                messages = [UserMessage(content=user_input)]
                response = client.complete(
                    messages=messages,
                    model=selected_model
                )
                bot_response = response.choices[0].message.content
            except Exception as e:
                bot_response = f"Error: {str(e)}"
            return render_template("index.html", response=bot_response, models=available_models)
    return render_template("index.html", models=available_models)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)