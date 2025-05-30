import streamlit as st
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from dotenv import load_dotenv
import os

# Custom CSS for styling
st.markdown("""
  <style>
    .stApp {
        background-color:rgb(216, 217, 219);
        color : rgb(11,55,99);
    }
    .stForm {
        background-color: rgb(190, 245, 103);
        color: rgb(245, 12, 24);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(243, 14, 14, 0.1);
    }
    .stButton>button {
        background-color:rgb(44, 86, 223);
        color: rgba(125, 79, 250, 0.88);
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    h1 {
        color:rgb(235, 235, 235);
    }
    .stTextInput>div>div>input {
        color: rgb(56, 23, 240);
    }
    .stTextArea>div>div>textarea {
        color: rgb(240, 23, 113);
    }
    </style>
     """, unsafe_allow_html=True)

# Page configuration
# st.set_page_config(
#     page_title="Email Sender",
#     page_icon="✉️",
#     layout="centered"
# )

# Load environment variables
load_dotenv()
sender_email = os.getenv("sender_email")
password = os.getenv("password")

# Title and description
st.title("📧 Email Sender")
st.markdown("Send emails easily using this interface!")

# Create a form for email input
with st.form("email_form"):
    # Email input fields
    receiver_email = st.text_input("Recipient Email Address")
    subject = st.text_input("Subject", "Automated Email Subject")
    message = st.text_area("Message", height=200)
    
    # Send button
    submit_button = st.form_submit_button("Send Email")

    if submit_button:
        if not receiver_email or not message:
            st.error("Please fill in all required fields!")
        else:
            try:
                # Create message
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(message, 'plain'))

                # Send email
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                server.quit()

                st.success("✅ Email sent successfully!")
            except Exception as e:
                st.error(f"❌ Failed to send email: {str(e)}")

# Add some helpful information
st.markdown("---")
st.markdown("""
### How to use:
1. Enter the recipient's email address
2. Add a subject (optional)
3. Write your message
4. Click 'Send Email' to send
""")