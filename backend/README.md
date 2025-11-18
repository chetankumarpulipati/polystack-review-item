# WhatsApp Product Review Collector - Backend

This is the backend service for the WhatsApp Product Review Collector application. It receives WhatsApp messages via Twilio webhook, manages conversation flow, stores reviews in PostgreSQL, and provides REST APIs.

## Tech Stack

- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Database for storing reviews
- **SQLAlchemy** - ORM for database operations
- **Twilio** - WhatsApp integration
- **Uvicorn** - ASGI server

## Prerequisites

1. **Python 3.8+** installed
2. **PostgreSQL** installed and running
3. **Twilio Account** with WhatsApp Sandbox configured

## Setup Instructions

### 1. Install PostgreSQL

If you don't have PostgreSQL installed:
- Download from: https://www.postgresql.org/download/
- Install and remember your password
- Default port: 5432

### 2. Create Database

Open PostgreSQL command line (psql) or pgAdmin and create a database:

```sql
CREATE DATABASE whatsapp_reviews;
```

### 3. Install Python Dependencies

Navigate to the backend folder and create a virtual environment:

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the backend folder:

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/whatsapp_reviews
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
```

Replace:
- `your_password` with your PostgreSQL password
- `your_account_sid` with your Twilio Account SID
- `your_auth_token` with your Twilio Auth Token

### 5. Setup Twilio WhatsApp Sandbox

1. Go to https://console.twilio.com/
2. Navigate to Messaging > Try it out > Send a WhatsApp message
3. Follow instructions to activate your sandbox (send a code to the Twilio WhatsApp number)
4. Configure the webhook URL:
   - You'll need to expose your local server using ngrok (see below)
   - Set webhook URL to: `https://your-ngrok-url.ngrok.io/webhook/whatsapp`

### 6. Expose Local Server with ngrok

Since Twilio needs to reach your local server:

1. Download ngrok: https://ngrok.com/download
2. Run ngrok:
   ```bash
   ngrok http 8000
   ```
3. Copy the HTTPS URL (e.g., `https://abc123.ngrok.io`)
4. In Twilio Console, set this as your webhook URL: `https://abc123.ngrok.io/webhook/whatsapp`

### 7. Run the Server

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The server will start at `http://localhost:8000`

## API Endpoints

### GET /api/reviews
Returns all stored reviews in JSON format.

**Response:**
```json
[
  {
    "id": 1,
    "contact_number": "whatsapp:+1415XXXXXXX",
    "user_name": "Aditi",
    "product_name": "iPhone 15",
    "product_review": "Amazing battery life, very satisfied.",
    "created_at": "2025-11-17T12:34:56Z"
  }
]
```

### GET /api/reviews/{review_id}
Get a specific review by ID.

### POST /webhook/whatsapp
Twilio webhook endpoint (configured in Twilio Console).

## Conversation Flow

1. User sends: "Hi"
2. Bot: "Which product is this review for?"
3. User: "iPhone 15"
4. Bot: "What's your name?"
5. User: "Aditi"
6. Bot: "Please send your review for iPhone 15."
7. User: "Amazing battery life, very satisfied."
8. Bot: "Thanks Aditi -- your review for iPhone 15 has been recorded."

## Database Schema

**Table: reviews**

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| contact_number | String | WhatsApp number (format: whatsapp:+1234567890) |
| user_name | String | Name of the reviewer |
| product_name | String | Product being reviewed |
| product_review | Text | The review text |
| created_at | Timestamp | When the review was created |

## Testing

You can test the API endpoints using:
- Browser: http://localhost:8000/docs (Swagger UI)
- Postman or curl
- The React frontend

Example curl command:
```bash
curl http://localhost:8000/api/reviews
```

## Troubleshooting

### Database Connection Error
- Check PostgreSQL is running
- Verify DATABASE_URL in .env file
- Ensure database exists

### Twilio Webhook Not Receiving Messages
- Check ngrok is running
- Verify webhook URL in Twilio Console
- Check server logs for errors

### Conversation Not Working
- Check server logs
- Verify message format from Twilio
- Test API endpoints directly

## Development

The conversation state is stored in memory. For production:
- Use Redis for conversation state
- Add authentication
- Add rate limiting
- Use proper logging
- Deploy to cloud (AWS, Heroku, etc.)

## Project Structure

```
backend/
├── main.py                  # FastAPI application and routes
├── models.py                # SQLAlchemy database models
├── schemas.py               # Pydantic schemas for validation
├── database.py              # Database configuration
├── conversation_manager.py  # WhatsApp conversation logic
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── .env                    # Your environment variables (git-ignored)
└── README.md               # This file
```

