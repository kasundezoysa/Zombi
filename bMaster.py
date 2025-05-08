# Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
## CC BY-NC-SA 4.0
#  [Full Legal Code](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

### You are free to:
#- **Share** — copy and redistribute the material
#- **Adapt** — remix, transform, and build upon the material

### Under these terms:
#- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
#- **NonCommercial** — You may not use the material for commercial purposes.
#- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license.

### Additional Educational Restrictions:
# 1. **Ethical Use Clause**  
#   This software is provided solely for:
#   - Academic research
#   - Cybersecurity education
#   - Defensive security training

# 2. **Prohibited Uses**  
#   Explicitly forbidden:
#   - Malicious hacking
#   - Unauthorized penetration testing
#   - Military/weapons applications
#   - Commercial security products

# 3. **Liability**  
#   The licensor bears no responsibility for misuse of this software.

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
