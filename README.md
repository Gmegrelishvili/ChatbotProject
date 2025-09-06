## Car Loan Chatbot

This project is a **Car Loan Chatbot** built with **Python**, **Flask**, **Rasa**, **SQLite**, and **Bootstrap**.  
It allows users to chat with an AI assistant about auto loan conditions from different partner companies, register and
log in, and store conversation history.

---

## Features

- 🔹 **User Authentication**
    - Registration and login with password hashing
    - Logout functionality
    - Loads previous conversations for each user

- 🔹 **Chatbot (Rasa-based)**
    - Answers questions about car loans from 5 partner companies
    - Provides conditions depending on **car year**
    - Provides conditions depending on **borrower's age**
    - Responds to direct queries about each company (Silk Bank, Central, Flex Capital, Mogo, Dizi)

- 🔹 **Database (SQLite)**
    - Stores registered users
    - Saves chat history (messages from user and chatbot)
    - Different colors for user and bot messages

- 🔹 **Frontend (Flask + Bootstrap)**
    - Clean, responsive UI
    - Works on both desktop and mobile devices

---

## Technologies Used

- **Python 3.10**
- **Flask** (for backend and frontend integration)
- **Rasa** (for natural language understanding and actions)
- **SQLite** (for data persistence)
- **Bootstrap** (for UI styling)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/car-loan-chatbot.git

    cd car-loan-chatbot

    python -m venv venv
    source venv/bin/activate # On Windows use: venv\Scripts\activate

    pip install -r requirements.txt

    rasa train
   
    rasa run actions &
    rasa run --enable-api --cors "*"

    python app.py
   
    Open in browser: http://127.0.0.1:5000
   

## Sample Conversation – Car Financing
**User:** I want to buy a car  
**Bot:** We partner with 5 companies: Silk Bank, Central, Flex Capital, MoGo and Dizi. Each has different terms and conditions. Send me your car details (manufacturer, model, and year of manufacture) and I will tell you which company will be able to finance it. 

**User:** BMW X5 2010  
**Bot:** Your car can be financed by any partner company. The best terms are with Silk Bank.

**User:** BMW 323 1996  
**Bot:** Your car can only be financed through MoGo and Flex Capital.


## Sample Conversation – Age Check
**User:** What are the loan terms based on age?  
**Bot:** How old are you?

**User:** My age is 25  
**Bot:** ✅ All companies will review your application.

**User:** My age is 21  
**Bot:** ⚠️ All companies are considering it, except Dizi.

**User:** My age is 19  
**Bot:** ⚠️ Only Flex Capital will review your application.

**User:** My age is 16  
**Bot:** ⚠️ Your application will not be considered because you are not of legal age.










