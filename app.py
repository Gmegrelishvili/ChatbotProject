from extensions import app
from routes import home, chat, faq, registration, profile, login, logout

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)