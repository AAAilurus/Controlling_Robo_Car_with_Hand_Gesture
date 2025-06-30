import requests


pi_ip = "192.168.1.253"  

url = f"http://{pi_ip}:5000/command"


command_to_send = "None"  

payload = {"command": command_to_send}

try:
    response = requests.post(url, json=payload)
    print("Sent command:", command_to_send)
    print("Response from Pi:", response.text)
except Exception as e:
    print("Failed to send command:", e)
