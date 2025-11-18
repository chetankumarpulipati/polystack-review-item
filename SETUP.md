# Setup Instructions for WhatsApp Product Review Collector

## Quick Start Guide

Follow these steps to get the application running:

### Step 1: Install Prerequisites

1. **Install Python 3.8+**
   - Download from: https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"
   - Verify: Open cmd and run `python --version`

2. **Install Node.js 14+**
   - Download from: https://nodejs.org/
   - Install with default settings
   - Verify: Open cmd and run `node --version`

3. **Install PostgreSQL**
   - Download from: https://www.postgresql.org/download/windows/
   - During installation, set a password (remember it!)
   - Default port: 5432
   - Verify: PostgreSQL should be running as a service

4. **Create Database**
   - Open pgAdmin (comes with PostgreSQL)
   - Right-click "Databases" → Create → Database
   - Name it: `whatsapp_reviews`
   - Click Save

### Step 2: Setup Backend

1. **Configure Environment Variables**
   - Navigate to `backend/` folder
   - Copy `.env.example` to `.env`
   - Edit `.env` and update:
     ```
     DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/whatsapp_reviews
     ```
     Replace `YOUR_PASSWORD` with your PostgreSQL password

2. **Run Backend**
   - Double-click `start-backend.bat` in the Assignment folder
   - OR manually:
     ```cmd
     cd backend
     python -m venv venv
     venv\Scripts\activate
     pip install -r requirements.txt
     python main.py
     ```
   - Backend will start at http://localhost:8000
   - Keep this window open!

### Step 3: Setup Frontend

1. **Run Frontend**
   - Double-click `start-frontend.bat` in the Assignment folder
   - OR manually:
     ```cmd
     cd frontend
     npm install
     npm start
     ```
   - Frontend will open in browser at http://localhost:3000
   - Keep this window open!

### Step 4: Setup Twilio WhatsApp

1. **Create Twilio Account**
   - Go to: https://www.twilio.com/try-twilio
   - Sign up for free account
   - Verify your email and phone number

2. **Setup WhatsApp Sandbox**
   - In Twilio Console, go to: Messaging > Try it out > Send a WhatsApp message
   - You'll see a WhatsApp number (e.g., +1 415 523 8886)
   - Follow the instructions to join the sandbox:
     - Send a WhatsApp message with the code shown (e.g., "join <code>")
     - You'll get a confirmation message

3. **Get Twilio Credentials**
   - In Twilio Console, go to Account Dashboard
   - Copy your "Account SID" and "Auth Token"
   - Update `backend/.env` file:
     ```
     TWILIO_ACCOUNT_SID=your_account_sid_here
     TWILIO_AUTH_TOKEN=your_auth_token_here
     ```

4. **Setup ngrok (to receive WhatsApp messages)**
   - Download ngrok: https://ngrok.com/download
   - Extract ngrok.exe to a folder
   - Open cmd in that folder and run:
     ```cmd
     ngrok http 8000
     ```
   - Copy the HTTPS URL shown (e.g., https://abc123.ngrok.io)
   - In Twilio Console:
     - Go to: Messaging > Settings > WhatsApp Sandbox Settings
     - Set "WHEN A MESSAGE COMES IN" to:
       ```
       https://your-ngrok-url.ngrok.io/webhook/whatsapp
       ```
     - Set method to: HTTP POST
     - Click Save

### Step 5: Test the Application

1. **Test Backend API**
   - Open browser: http://localhost:8000/docs
   - You should see API documentation
   - Try GET /api/reviews endpoint

2. **Test WhatsApp Flow**
   - Send any message to your Twilio WhatsApp number
   - Follow the conversation:
     ```
     You: Hi
     Bot: Which product is this review for?
     You: iPhone 15
     Bot: What's your name?
     You: John
     Bot: Please send your review for iPhone 15.
     You: Great phone, loving it!
     Bot: Thanks John -- your review for iPhone 15 has been recorded.
     ```

3. **View Reviews**
   - Open frontend: http://localhost:3000
   - Your review should appear automatically
   - Click refresh button to update manually

## Troubleshooting

### Backend won't start
- Check PostgreSQL is running (Services → PostgreSQL)
- Verify DATABASE_URL in .env file
- Check if port 8000 is already in use

### Frontend won't start
- Run `npm install` in frontend folder
- Check if port 3000 is already in use
- Try: `npm cache clean --force` then `npm install`

### WhatsApp messages not working
- Ensure ngrok is running
- Check webhook URL in Twilio Console
- Verify backend is running and accessible
- Check backend logs for errors

### Database connection error
- Ensure PostgreSQL service is running
- Verify password in DATABASE_URL
- Check database exists: `whatsapp_reviews`

## What's Included

✅ **Backend (FastAPI + PostgreSQL)**
   - WhatsApp webhook endpoint
   - Conversation state management
   - RESTful API for reviews
   - Database models and schemas

✅ **Frontend (React)**
   - Modern, responsive UI
   - Real-time review display
   - Auto-refresh every 10 seconds
   - Error handling

✅ **Documentation**
   - Complete README files
   - Setup instructions
   - API documentation
   - Troubleshooting guide

✅ **Helper Scripts**
   - start-backend.bat
   - start-frontend.bat

## Demo Video Recording

To record your screencast:
1. Use OBS Studio (free) or Windows Game Bar (Win+G)
2. Show the complete flow:
   - Start backend and frontend
   - Send WhatsApp messages
   - Show conversation flow
   - Display reviews on frontend
   - Test refresh functionality

## Next Steps

1. Test the entire flow
2. Record your screencast demo
3. Push to GitHub (see GitHub instructions below)
4. Submit your assignment

## GitHub Repository

To create a GitHub repo:

```cmd
cd C:\Users\cheta\Desktop\Assignment
git init
git add .
git commit -m "Initial commit: WhatsApp Product Review Collector"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/whatsapp-review-collector.git
git push -u origin main
```

That's it! You now have a complete full-stack WhatsApp review collection system.

