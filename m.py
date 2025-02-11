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
 # Start from the 14th row

# Email credentials
sender_email = "james@datavyn.com"
df=df[300:]
# Email content
subject = "Loved Your Airbnb Listing!"
df["Host"]= df["Host"].str.replace("Hosted by ", "", regex=False)
# Function to send email

    
    # HTML email body with proper spacing
def send_email(row):
    # Extract the host's name
    # Remove "Hosted by" prefix
    
       # Prepare email details
    receiver_email = row['Emails']
    host_name = row["Host"]
    location = row['Location']
    rating = row['Room Rating']
    reviews = row['visibleReviewCount']
    
    # Define the subject
    subject = f"{host_name}, Loved Your Airbnb Listing!"
    
    # Plain text email body
    body = f"""Hi {host_name},

    I hope you’re well! I came across your Airbnb listing and was truly impressed—you’ve done an incredible job maintaining a {rating}-star rating from {reviews} reviews.
    
    I’m following up because I believe my tool can help your listing shine even brighter. It extracts top SEO keywords to boost your ranking and scrapes competitor prices, so you can set the perfect rate to attract more guests.
    
    Would you like a quick demo to see how it works?
    
    Looking forward to hearing from you!
    
    Warm regards,
    Jamshaid
    """
    
    # Create the email
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    
    # Output the email message


    # Send the email
    try:
        with smtplib.SMTP("smtp.hostinger.com", 587) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print(f"Email sent successfully !")
    except Exception as e:
        print(f"Error sending email to : {e}")

# Iterate through the DataFrame and send emails with a random delay
for index, row in df.iterrows():
    send_email(row)
    delay = random.randint(30, 45)  # Random delay between 10 and 30 seconds
    print(f"Waiting for {delay} seconds before sending the next email...")
    time.sleep(delay)
