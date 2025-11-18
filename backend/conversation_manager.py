from typing import Dict, Optional
from datetime import datetime, timedelta

class ConversationState:
    INITIAL = "initial"
    AWAITING_PRODUCT = "awaiting_product"
    AWAITING_NAME = "awaiting_name"
    AWAITING_REVIEW = "awaiting_review"
    COMPLETED = "completed"

class ConversationManager:
    def __init__(self):
        # In production, use Redis or database for persistence
        self.conversations: Dict[str, dict] = {}
        self.timeout_minutes = 30

    def get_conversation(self, contact_number: str) -> dict:
        """Get or create a conversation state for a contact"""
        if contact_number not in self.conversations:
            self.conversations[contact_number] = {
                "state": ConversationState.INITIAL,
                "product_name": None,
                "user_name": None,
                "product_review": None,
                "last_updated": datetime.utcnow()
            }
        else:
            # Check for timeout
            last_updated = self.conversations[contact_number]["last_updated"]
            if datetime.utcnow() - last_updated > timedelta(minutes=self.timeout_minutes):
                # Reset conversation
                self.conversations[contact_number] = {
                    "state": ConversationState.INITIAL,
                    "product_name": None,
                    "user_name": None,
                    "product_review": None,
                    "last_updated": datetime.utcnow()
                }

        return self.conversations[contact_number]

    def update_conversation(self, contact_number: str, **kwargs):
        """Update conversation data"""
        if contact_number in self.conversations:
            self.conversations[contact_number].update(kwargs)
            self.conversations[contact_number]["last_updated"] = datetime.utcnow()

    def reset_conversation(self, contact_number: str):
        """Reset conversation to initial state"""
        if contact_number in self.conversations:
            del self.conversations[contact_number]

    def process_message(self, contact_number: str, message: str) -> tuple[str, bool]:
        """
        Process incoming message and return response
        Returns: (response_message, is_complete)
        """
        conversation = self.get_conversation(contact_number)
        state = conversation["state"]
        is_complete = False
        
        if state == ConversationState.INITIAL:
            # First message - ask for product
            self.update_conversation(contact_number, state=ConversationState.AWAITING_PRODUCT)
            response = "Which product is this review for?"
            
        elif state == ConversationState.AWAITING_PRODUCT:
            # Received product name
            self.update_conversation(
                contact_number,
                product_name=message.strip(),
                state=ConversationState.AWAITING_NAME
            )
            response = "What's your name?"
            
        elif state == ConversationState.AWAITING_NAME:
            # Received user name
            product_name = conversation["product_name"]
            self.update_conversation(
                contact_number,
                user_name=message.strip(),
                state=ConversationState.AWAITING_REVIEW
            )
            response = f"Please send your review for {product_name}."
            
        elif state == ConversationState.AWAITING_REVIEW:
            # Received review
            user_name = conversation["user_name"]
            product_name = conversation["product_name"]
            self.update_conversation(
                contact_number,
                product_review=message.strip(),
                state=ConversationState.COMPLETED
            )
            response = (
                f"✅ Thank you, {user_name}! Your review for {product_name} has been successfully recorded.\n\n"
                f"📝 Your review: \"{message.strip()}\"\n\n"
                f"Want to submit another review? Just send any message to start over!"
            )
            is_complete = True
            
        elif state == ConversationState.COMPLETED:
            # User wants to submit another review
            self.reset_conversation(contact_number)
            self.update_conversation(contact_number, state=ConversationState.AWAITING_PRODUCT)
            response = "Great! Let's collect another review. Which product is this review for?"

        else:
            # Shouldn't reach here, but handle gracefully
            response = "Something went wrong. Let's start over. Which product is this review for?"
            self.update_conversation(contact_number, state=ConversationState.AWAITING_PRODUCT)
        
        return response, is_complete
    
    def get_complete_data(self, contact_number: str) -> Optional[dict]:
        """Get complete conversation data if ready to save"""
        conversation = self.get_conversation(contact_number)
        if conversation["state"] == ConversationState.COMPLETED:
            return {
                "contact_number": contact_number,
                "product_name": conversation["product_name"],
                "user_name": conversation["user_name"],
                "product_review": conversation["product_review"]
            }
        return None

# Global instance
conversation_manager = ConversationManager()
