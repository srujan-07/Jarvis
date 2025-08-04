import pyttsx3
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.setProperty("rate",185)

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

#^ Function to send an email.
def send_email(sender_email, sender_password, recipient_email, subject, content):
    from email.message import EmailMessage
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.set_content(content)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

    print("Email sent successfully.")
    Speak("Email sent successfully.")

# ~Using Dictionary to map recipient names and their email ids.

recipient_mapping = {
    "friend": "friend@example.com",
    "family": "family@example.com",
    "boss": "boss@company.com",
    # Add more recipient mappings as needed.
    # Format: "name_you_say": "actual_email@domain.com"
}

# & Fetch sender's email and password 
# & Here you will add your email id and password which you want to use to send email to other recipients.
# & You make sure that you can't use your original password for privacy concerns.
# & You can use Google 'App Passwords' feature for Gmail (2-factor authentication required).
# & Go to: Google Account Settings -> Security -> App passwords

sender_email = "srujansamala92@gmail.com"  # Gmail address
sender_password = "mxj6142f"  # Gmail App Password





