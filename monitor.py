import requests
import smtplib
import schedule
import time
from datetime import datetime

# --- CONFIGURATION ---
SENDER_EMAIL = "your-email@gmail.com"        # Your Gmail
SENDER_PASSWORD = "xxxx xxxx xxxx xxxx"      # Your App Password (16 chars)
RECEIVER_EMAIL = "target-email@gmail.com"    # Who gets the alert?

# List of sites to monitor
SITES_TO_CHECK = [
    "https://google.com",
    "https://github.com",
    "https://httpstat.us/404", # Test URL (This will fail intentionally)
    "https://httpstat.us/500", # Test URL (Server Error)
]

def send_alert(site, status_code):
    """Sends an email alert when a site goes down."""
    subject = f"⚠️ ALERT: {site} is DOWN!"
    body = f"URGENT: Your monitor detected a failure.\n\nSite: {site}\nStatus Code: {status_code}\nTime: {datetime.now()}"
    
    # Format the email
    msg = f"Subject: {subject}\n\n{body}"
    
    try:
        # Connect to Gmail SMTP Server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls() # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg)
            
        print(f"📧 Alert email sent for {site}")
        
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

def check_sites():
    """Loops through URLs and checks their status."""
    print(f"\n🔎 Running check at {datetime.now().strftime('%H:%M:%S')}...")
    
    for site in SITES_TO_CHECK:
        try:
            # Send a GET request (Timeout after 5 seconds)
            response = requests.get(site, timeout=5)
            
            # Check if status code is 200 (OK)
            if response.status_code == 200:
                print(f"✅ {site} is ONLINE")
            else:
                print(f"❌ {site} returned {response.status_code}")
                send_alert(site, response.status_code)
                
        except requests.exceptions.ConnectionError:
            print(f"❌ {site} Connection FAILED")
            send_alert(site, "Connection Error")
            
        except requests.exceptions.Timeout:
            print(f"❌ {site} Timed Out")
            send_alert(site, "Timeout")

# --- SCHEDULER ---
if __name__ == "__main__":
    print("🚀 SiteSentry Monitoring Started...")
    print("Press Ctrl+C to stop.")
    
    # Run the check immediately once
    check_sites()
    
    # Schedule the check to run every 1 minute
    schedule.every(1).minutes.do(check_sites)
    
    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(1)