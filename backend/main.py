from fastapi import FastAPI, Depends, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from sqlalchemy.orm import Session
from typing import List
from twilio.twiml.messaging_response import MessagingResponse

import models
import schemas
from database import engine, get_db
from conversation_manager import conversation_manager

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="WhatsApp Product Review Collector")

# CORS middleware for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "WhatsApp Product Review Collector API"}

@app.post("/webhook/whatsapp")
async def whatsapp_webhook(
    request: Request,
    Body: str = Form(...),
    From: str = Form(...),
    db: Session = Depends(get_db)
):
    """
    Twilio webhook endpoint for WhatsApp messages
    """
    contact_number = From  # Format: whatsapp:+1234567890
    message_body = Body.strip()
    
    # Process the message through conversation manager
    response_text, is_complete = conversation_manager.process_message(
        contact_number, 
        message_body
    )
    
    # If conversation is complete, save to database
    if is_complete:
        review_data = conversation_manager.get_complete_data(contact_number)
        if review_data:
            db_review = models.Review(**review_data)
            db.add(db_review)
            db.commit()
            db.refresh(db_review)
            
            # Reset conversation for next review
            conversation_manager.reset_conversation(contact_number)
    
    # Create Twilio response with proper XML formatting
    resp = MessagingResponse()
    resp.message(response_text)
    
    # Return response with correct content type for Twilio
    return Response(content=str(resp), media_type="application/xml")

@app.get("/api/reviews", response_model=List[schemas.ReviewResponse])
def get_reviews(db: Session = Depends(get_db)):
    """
    Get all reviews from database
    """
    reviews = db.query(models.Review).order_by(models.Review.created_at.desc()).all()
    return reviews

@app.get("/api/reviews/{review_id}", response_model=schemas.ReviewResponse)
def get_review(review_id: int, db: Session = Depends(get_db)):
    """
    Get a specific review by ID
    """
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not review:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@app.delete("/api/reviews/{review_id}")
def delete_review(review_id: int, db: Session = Depends(get_db)):
    """
    Delete a review (optional feature)
    """
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not review:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Review not found")
    
    db.delete(review)
    db.commit()
    return {"message": "Review deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
