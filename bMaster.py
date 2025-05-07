import requests
import time
import os
import socket
import random

# Configuring C2 Server
C2_SERVER = "http://127.0.0.1:5000"  # Replace with your test server
BEACON_INTERVAL = 20  # Seconds between check-ins

def beacon():
    while True:
        try:
            # Simulate sending command info to C2
            hostname = socket.gethostname()
            bid=input("Enter boat ID > ")
            cmd=input("Enter the command > ")
            data = {
                "bot_id": bid,
                "command": cmd
            }
            
            # Send beacon to C2
            response = requests.post(
                f"{C2_SERVER}/command",
                json=data,
                timeout=10
            )
            
            # Check for commands
            if response.status_code == 200:
                print(f"C2 Server acknowledged the instruction : {response.json()}")

        except Exception as e:
            print(f"[!] Error: {e}")
        
        time.sleep(BEACON_INTERVAL)

if __name__ == "__main__":
    print("[*] Zombie Master simulator started...")
    beacon()
