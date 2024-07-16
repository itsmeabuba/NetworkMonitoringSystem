import csv
import datetime
import smtplib
from email.mime.text import MIMEText

# Configuration
ALERT_THRESHOLD = 10000  # Number of packets per minute that triggers an alert, change this to your desired maximum threshold based on your normal activity
EMAIL_ADDRESS = 'sending@gmail.com'  # Change to your email address
EMAIL_PASSWORD = 'aaaa aaaa aaaa aaaa'  # Change to your email app password
ALERT_RECIPIENT = 'recieving@example.com'  # Change to the recipient's email address

# CSV file path
csv_file_path = 'network_traffic.csv'  # Path to the CSV file

def send_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'Network Traffic Alert'
    msg['From'] = EMAIL_ADDRESS  # Sender's email address
    msg['To'] = ALERT_RECIPIENT  # Recipient's email address

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:  # Using Gmail SMTP server
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login to the email account
        server.send_message(msg)  # Send the alert email

# Check for high traffic
now = datetime.datetime.now()
one_minute_ago = now - datetime.timedelta(minutes=1)  # Calculate the timestamp for one minute ago

count = 0
with open(csv_file_path, mode='r', newline='') as file:  # Open the CSV file in read mode
    reader = csv.DictReader(file)
    headers = reader.fieldnames  # Get the headers from the CSV file
    if 'date' not in headers or 'time' not in headers:
        raise KeyError("CSV file is missing 'date' or 'time' header.")
    
    for row in reader:
        try:
            date_str = row['date']  # Get the date string
            time_str = row['time']  # Get the time string
            timestamp = datetime.datetime.strptime(date_str + ' ' + time_str, '%Y-%m-%d %H:%M:%S.%f')  # Combine date and time
            if timestamp >= one_minute_ago:
                count += 1  # Count the number of packets in the last minute
        except KeyError as e:
            print(f"KeyError: {e} - row data: {row}")
        except ValueError as e:
            print(f"ValueError: {e} - row data: {row}")

if count > ALERT_THRESHOLD:  # Check if the packet count exceeds the threshold
    send_alert(f'High network traffic detected: {count} packets in the last minute.')  # Send an alert email
