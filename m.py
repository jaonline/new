import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
import time
import random
import base64
import json
from io import StringIO
# Decode your secret from a JSON file
import os
sender_password = os.getenv("sender_password")

import pandas as pd
import os
import base64
import pandas as pd
from io import StringIO

# Step 1: Retrieve the base64-encoded secret from the environment
base64_string = os.environ.get("gar1")

if not base64_string:
    print("Environment variable 'gar1' is not set or empty.")
    exit(1)

# Step 2: Decode the Base64 string
try:
    decoded_content = base64.b64decode(base64_string).decode("utf-8")
except Exception as e:
    print(f"Error decoding Base64 string: {e}")
    exit(1)

# Step 3: Convert the decoded string to a pandas DataFrame
try:
    csv_data = StringIO(decoded_content)  # Create a file-like object from the string
    df = pd.read_csv(csv_data)  # Read the CSV data into a DataFrame
except Exception as e:
    print(f"Error reading CSV data: {e}")
    exit(1)

# Step 4: Save the DataFrame as a CSV file (optional)


# Step 5: Print confirmation and preview the DataFrame


# Decode the password
#sender_password = base64.b64decode(data).decode("utf-8")

# Load the data from another JSON file or directly from CSV
# Read the base64 encoded content from the file


# Load the CSV content into a pandas DataFrame
#df = pd.read_csv(StringIO(csv_content))

# Convert the decoded CSV string to a Pandas DataFrame
from io import StringIO

# Skip rows if needed
df = df[1:]  # Start from the 14th row

# Email credentials
sender_email = "jamshaidarif63@gmail.com"

# Email content
subject = "Loved Your Airbnb Listing!"

# Function to send email
def send_email(row):
    # Extract the host's name
    host_name = row['Host'].replace('Hosted by ', '')  # Remove "Hosted by" prefix
    
    # Prepare email details
    receiver_email = row['Emails']
    rating = row['Room Rating']
    reviews = row['visibleReviewCount']
    location = row['Location']
    
    # HTML email body with proper spacing
   def send_email(row):
    # Extract the host's name
    host_name = row['Host'].replace('Hosted by ', '')  # Remove "Hosted by" prefix
    
    # Prepare email details
    receiver_email = row['Emails']
    title = row['Title']
    rating = row['Room Rating']
    reviews = row['visibleReviewCount']
    location = row['Location']
    
    # Define the new subject
    subject = "Loved Your Airbnb Listing – Here's How I Can Help You Boost It!"
    
    # HTML email body with more details and spacing
    body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
        <p>Hi <strong>{host_name}</strong>,</p>
        
        <p>I came across your Airbnb listing, "<strong>{host_name}</strong>" in <strong>{location}</strong>, and I must say it looks fantastic! Your <strong>{rating}</strong>-star rating from <strong>{reviews}</strong> reviews shows that you’re doing a great job providing an excellent experience for your guests. It’s clear that you’re dedicated to offering a top-notch stay!</p>
        
        <p>As an Airbnb host, staying ahead of the competition is key. That’s why I’ve developed a tool that can help you take your listing to the next level:</p>
        <ul>
            <li><strong>Analyze competitor prices</strong> – Stay competitive by monitoring how your rates compare to similar listings and adjust accordingly.</li>
            <li><strong>Extract SEO keywords</strong> – Our tool extracts SEO-friendly keywords that can help improve your listing's visibility in search results, driving more views and potential bookings.</li>
        </ul>
        
        <p>In today’s competitive market, it’s important to not only stand out but also be strategic with your pricing and visibility. With these features, I believe you could see a significant improvement in your rankings and bookings!</p>
        
        <p>Would you be open to learning more about how this tool works and how it can help your listing get even better results? It’s simple to use and could make a big difference in your bookings.</p>
        
        <p>Looking forward to hearing from you!</p>
        
        <p>Best regards,<br>Jamshaid</p>
    </body>
    </html>
    """

  

   



    # Create the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))
    # Send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print(f"Email sent successfully !")
    except Exception as e:
        print(f"Error sending email to : {e}")

# Iterate through the DataFrame and send emails with a random delay
for index, row in df.iterrows():
    send_email(row)
    delay = random.randint(70, 80)  # Random delay between 10 and 30 seconds
    print(f"Waiting for {delay} seconds before sending the next email...")
    time.sleep(delay)
