# How to Run the WhatsApp Product Review Collector

## Prerequisites ✅
- ✅ Python 3.10.11 installed
- ✅ Node.js v24.1.0 installed
- ✅ PostgreSQL database configured
- ✅ All dependencies installed

## 3 Commands to Run the Project

### Command 1: Start the Backend Server

**Option A: Using the batch file (Recommended)**
```cmd
start-backend.bat
```

**Option B: Manual commands**
```cmd
cd backend
venv\Scripts\activate
python main.py
```

**Expected Output:**
- Backend will start at: http://localhost:8000
- API docs available at: http://localhost:8000/docs

---

### Command 2: Start the Frontend Application

**Option A: Using the batch file (Recommended)**
```cmd
start-frontend.bat
```

**Option B: Manual commands**
```cmd
cd frontend
npm start
```

**Expected Output:**
- Frontend will open automatically in browser at: http://localhost:3000
- You'll see the Product Reviews interface

---

### Command 3: (Optional) Expose Backend via ngrok

For WhatsApp webhook integration with Twilio:

```cmd
ngrok http 8000
```

**Expected Output:**
- You'll get a public HTTPS URL (e.g., https://abc123.ngrok.io)
- Copy this URL and configure it in Twilio WhatsApp Sandbox settings
- Set webhook URL to: https://YOUR-NGROK-URL/webhook/whatsapp

---

## Running the Complete Project

### Step 1: Open Command Prompt #1
```cmd
cd C:\Users\cheta\Desktop\Assignment
start-backend.bat
```
Keep this window open!

### Step 2: Open Command Prompt #2
```cmd
cd C:\Users\cheta\Desktop\Assignment
start-frontend.bat
```
Keep this window open!

### Step 3 (Optional): Open Command Prompt #3
```cmd
ngrok http 8000
```
For WhatsApp functionality only.

---

## Quick Test

1. After starting both servers, open: http://localhost:3000
2. You should see the reviews interface
3. Backend API is running at: http://localhost:8000
4. Check backend health: http://localhost:8000 (should show welcome message)

---

## Troubleshooting

**If backend fails to start:**
- Ensure PostgreSQL is running
- Check that database 'whatsapp_reviews' exists
- Verify .env file has correct database password

**If frontend fails to start:**
- Port 3000 might be in use
- Try closing other React apps

**If "port already in use" error:**
- Kill the process using that port or restart your computer

---

## Current Configuration

- Database: `postgresql://postgres:chetan@localhost:5432/whatsapp_reviews`
- Backend Port: 8000
- Frontend Port: 3000
- Twilio Account SID: Configured
- Twilio Auth Token: Configured

