from flask import Blueprint, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText
import logging
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/services')
def services():
    return render_template('services.html')

@main.route('/pricing')
def pricing():
    return render_template('pricing.html')

@main.route('/solutions')
def solutions():
    return render_template('solutions.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy.html')

@main.route('/terms-of-service')
def terms_of_service():
    return render_template('termsofservice.html')

@main.route('/careers')
def careers():
    return render_template('careers.html')

def send_email(subject, body, recipient):
    """Sends email, returns True on success, False on failure."""
    try:
        # Load SMTP settings from environment variables
        smtp_server = os.getenv('SMTP_SERVER')
        smtp_port = int(os.getenv('SMTP_PORT'))
        smtp_user = os.getenv('SMTP_USER')
        smtp_password = os.getenv('SMTP_PASSWORD')
        sender_email = smtp_user  # Use the authenticated user as the sender

        # Debugging: Print SMTP settings
        logger.debug(f"SMTP Server: {smtp_server}, Port: {smtp_port}, User: {smtp_user}")

        # Connect to SMTP server
        server = smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=10)
        server.set_debuglevel(False)  # Keep debug level at False for production
        server.login(smtp_user, smtp_password)

        # Create email message
        msg = MIMEText(body, "plain", "utf-8")
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient

        # Send email
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()

        logger.info(f"Email sent to: {recipient}")
        return True
    except Exception as e:
        logger.error(f"Failed to send email to {recipient}: {e}")
        return False

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Debugging: Print form data
        logger.debug(f"Form Data - Name: {name}, Email: {email}, Message: {message}")

        if not name or not email or not message:
            logger.error("Missing form data")
            flash('Please fill out all fields.', 'error')
            return redirect(url_for('main.contact'))

        # Prepare email content
        subject = f"New Contact Form Submission from {name}"
        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        # Send email
        if send_email(subject, body, "hello@ciphervance.com"):
            flash('Your message has been sent! We will get back to you soon.', 'success')
        else:
            flash('An error occurred while sending your message. Please try again later.', 'error')

        return redirect(url_for('main.contact'))

    return render_template('contact.html')