import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
import time
import random
import base64
import json

# Decode your secret from a JSON file
with open("file.json", "r") as f:
    data = json.load(f)
    encoded_secret = data["password"]

# Decode the password
sender_password = base64.b64decode(encoded_secret).decode("utf-8")

# Load the data from another JSON file or directly from CSV
with open("file1.json", "r") as f:
    df_encoded = json.load(f)
    decoded_csv = base64.b64decode(df_encoded["data"]).decode("utf-8")

# Convert the decoded CSV string to a Pandas DataFrame
from io import StringIO
df = pd.read_csv(StringIO(decoded_csv))

# Skip rows if needed
df = df[13:]  # Start from the 14th row

# Email credentials
sender_email = "jamshaidarif63@gmail.com"

# Email content
subject = "Loved Your Airbnb Listing!"

# Function to send email
def send_email(row):
    receiver_email = row['Emails']
    body = f"""Hi {row['Title']},

I came across your Airbnb listing, {row['Title']}, and it looks fantastic! You’ve done an incredible job maintaining a {row['Rating']} star rating from {row['Reviews']} reviews.

The reason I'm emailing you is that I can help improve your Airbnb ranking and manage your pricing effectively.
I have a tool that can extract SEO keywords to boost your ranking. It also scrapes competitor prices, enabling you to adjust your pricing strategically and stay ahead in the market.

Would you like me to show you how it works?

Looking forward to hearing from you!

Best regards,  
Jamshaid
"""

    # Create the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print(f"Email sent successfully to {receiver_email}!")
    except Exception as e:
        print(f"Error sending email to {receiver_email}: {e}")

# Iterate through the DataFrame and send emails with a random delay
for index, row in df.iterrows():
    send_email(row)
    delay = random.randint(10, 30)  # Random delay between 10 and 30 seconds
    print(f"Waiting for {delay} seconds before sending the next email...")
    time.sleep(delay)
