Asynchronous HTTP Requests
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.sentiment_access import load_notebook_from_pkl
from models.issue_escalation import should_escalate
from models.response_automation import preprocess_text, get_product_subject, get_product_body
import httpx

# Initialize the FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ZAPIER_WEBHOOK_URL = "https://zapier.com/editor/276111231/published"

class Ticket(BaseModel):
    subject: str
    body: str
    customer_email: str

@app.post("/process-ticket/")
async def process_ticket(ticket: Ticket):
    try:
        logger.info(f"Processing ticket for {ticket.customer_email}")
        # Preprocess ticket data
        processed_subject = preprocess_text(ticket.subject)
        processed_body = preprocess_text(ticket.body)

        # Sentiment analysis
        sentiment_result = load_notebook_from_pkl(processed_body)
        if not isinstance(sentiment_result, dict) or "sentiment" not in sentiment_result:
            logger.error("Invalid response from sentiment analysis model")
            raise ValueError("Invalid response from sentiment analysis model")

        # Issue escalation
        priority = should_escalate(processed_body)
        if not isinstance(priority, str):
            logger.error("Invalid priority calculated by issue escalation model")
            raise ValueError("Invalid priority calculated by issue escalation model")

        escalation_required = load_notebook_from_pkl(priority)
        if not isinstance(escalation_required, bool):
            logger.error("Invalid response for escalation requirement")
            raise ValueError("Invalid response for escalation requirement")

        # Extract product information
        product_subject = get_product_subject(processed_subject)
        product_body = get_product_body(processed_body)

        # Generate response
        response = {
            "customer_email": ticket.customer_email,
            "sentiment": sentiment_result["sentiment"],
            "escalation_required": escalation_required,
            "priority": priority,
            "product_details": {
                "from_subject": product_subject,
                "from_body": product_body
            }
        }

        # Construct payload for Zapier webhook
        zapier_payload = {
            "To": ticket.customer_email,
            "Cc": "",
            "Subject": f"Issue Report: {product_subject}",
            "Body type": "plain",
            "Body": (
                f"Hello,\n\n"
                f"We've received your ticket regarding: {product_subject}.\n\n"
                f"Here are the details:\n\n"
                f"Sentiment: {sentiment_result['sentiment']}\
::contentReference[oaicite:0]{index=0}
 
