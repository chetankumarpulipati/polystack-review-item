# WhatsApp Product Review Collector

A full-stack application that collects product reviews via WhatsApp conversations and displays them in a modern web interface.

## Overview

This application enables users to submit product reviews through WhatsApp. The backend manages a conversational flow to collect product name, user name, and review text, then stores everything in a PostgreSQL database. The React frontend displays all reviews in real-time.

## Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Relational database
- **SQLAlchemy** - ORM for database operations
- **Twilio** - WhatsApp integration
- **Python 3.8+**

### Frontend
- **React** - UI library
- **Axios** - HTTP client
- **CSS3** - Modern styling

## Features

✅ WhatsApp conversation flow for review collection  
✅ Automatic message handling via Twilio webhooks  
✅ PostgreSQL database for persistent storage  
✅ RESTful API endpoints  
✅ Real-time review display  
✅ Auto-refresh functionality  
✅ Responsive design  
✅ Error handling and validation  

## Project Structure

```
Assignment/
├── backend/
│   ├── main.py                  # FastAPI app and routes
│   ├── models.py                # Database models
│   ├── schemas.py               # Pydantic schemas
│   ├── database.py              # Database configuration
│   ├── conversation_manager.py  # WhatsApp conversation logic
│   ├── requirements.txt         # Python dependencies
│   ├── .env.example            # Environment template
│   └── README.md               # Backend documentation
├── frontend/
│   ├── src/
│   │   ├── App.js              # Main React component
│   │   ├── App.css             # Styling
│   │   ├── index.js            # Entry point
│   │   └── index.css           # Global styles
│   ├── public/
│   │   └── index.html          # HTML template
│   ├── package.json            # Dependencies
│   └── README.md               # Frontend documentation
└── README.md                   # This file
```

## Quick Start

### Prerequisites

1. **Python 3.8+** installed
2. **Node.js 14+** and npm installed
3. **PostgreSQL** installed and running
4. **Twilio account** with WhatsApp Sandbox configured
5. **ngrok** (for exposing local server to Twilio)

### Backend Setup

1. Navigate to backend folder:
```bash
cd backend
```

2. Create virtual environment and install dependencies:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

3. Create PostgreSQL database:
```sql
CREATE DATABASE whatsapp_reviews;
```

4. Create `.env` file (copy from `.env.example`):
```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/whatsapp_reviews
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
```

5. Run the server:
```bash
python main.py
```

Server will start at `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend folder:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm start
```

App will open at `http://localhost:3000`

### Twilio Setup

1. Sign up at [Twilio](https://www.twilio.com/)
2. Go to Messaging > Try it out > Send a WhatsApp message
3. Follow instructions to activate your sandbox
4. Install and run ngrok:
```bash
ngrok http 8000
```
5. Copy the ngrok HTTPS URL
6. In Twilio Console, set webhook to: `https://your-ngrok-url.ngrok.io/webhook/whatsapp`

## Conversation Flow

```
User: Hi
Bot:  Which product is this review for?

User: iPhone 15
Bot:  What's your name?

User: Aditi
Bot:  Please send your review for iPhone 15.

User: Amazing battery life, very satisfied.
Bot:  Thanks Aditi -- your review for iPhone 15 has been recorded.
```

## API Endpoints

### GET /api/reviews
Returns all reviews in JSON format.

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

### GET /api/reviews/{id}
Returns a specific review by ID.

### POST /webhook/whatsapp
Twilio webhook endpoint (configured in Twilio Console).

## Database Schema

**Table: reviews**

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key (auto-increment) |
| contact_number | String | WhatsApp number (format: whatsapp:+1234567890) |
| user_name | String | Name of the reviewer |
| product_name | String | Product being reviewed |
| product_review | Text | The review text |
| created_at | Timestamp | When review was created (UTC) |

## Testing

1. **Test Backend API:**
   - Visit `http://localhost:8000/docs` for Swagger UI
   - Or use curl: `curl http://localhost:8000/api/reviews`

2. **Test WhatsApp Flow:**
   - Send a message to your Twilio WhatsApp number
   - Follow the conversation prompts
   - Check frontend to see your review appear

3. **Test Frontend:**
   - Open `http://localhost:3000`
   - Click refresh button
   - Reviews should load automatically
   
### Expected Flow:
1. User sends message to WhatsApp
2. Bot guides conversation to collect: product name → user name → review
3. Review saves to database
4. Frontend displays review in real-time

## Troubleshooting

### Backend Issues

**Database Connection Error:**
- Check PostgreSQL is running
- Verify DATABASE_URL in .env
- Ensure database exists

**Twilio Webhook Not Working:**
- Verify ngrok is running
- Check webhook URL in Twilio Console
- Look at server logs for errors

### Frontend Issues

**Can't Fetch Reviews:**
- Ensure backend is running on port 8000
- Check CORS is enabled in backend
- Verify API_URL in App.js

## Production Deployment

### Backend
- Deploy to: AWS EC2, Heroku, Google Cloud Run, DigitalOcean
- Use production database (RDS, ElephantSQL, etc.)
- Set up proper environment variables
- Use Redis for conversation state (instead of in-memory)
- Add authentication and rate limiting

### Frontend
- Deploy to: Vercel, Netlify, AWS S3 + CloudFront
- Update API_URL to production backend
- Run `npm run build` before deployment

## Future Enhancements

- [ ] User authentication
- [ ] Review moderation/admin panel
- [ ] Rating system (1-5 stars)
- [ ] Image upload support
- [ ] Search and filter reviews
- [ ] Export reviews to CSV
- [ ] Email notifications
- [ ] Analytics dashboard
- [ ] Multi-language support

## License

This project is open source and available for educational purposes.

## Author

Created as an assignment submission for WhatsApp Product Review Collector.

## Support

For issues or questions:
1. Check the README files in backend/ and frontend/ folders
2. Review Twilio documentation
3. Check server logs for error messages

---
