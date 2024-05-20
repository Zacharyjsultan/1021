from flask import Flask, render_template, request
from chatterbot import ChatBot

# Create a chatbot instance
chatbot = ChatBot('MyChatBot')

# Flask app
app = Flask(__name__)

# Define routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    # Get user input from the 'msg' parameter in the request
    user_text = request.args.get('msg')
    
    # Get the chatbot response
    bot_response = str(chatbot.get_response(user_text))
    
    # Return the bot response as a string
    return bot_response

# Run the Flask app
if __name__ == "__main__":
    app.run()
