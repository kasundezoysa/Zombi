# Zombi Botnet Simulation Framework

A controlled environment for studying botnet command and control (C2) architectures.

**For educational purposes only**.

## Installation

git clone https://github.com/kasundezoysa/Zombi.git

cd Zombi

# Execution

1. Start the Command & Control (C2) Server

python3 c2.py

This will launch the c2 server to manage bot communications.

2. Launch the Zombie Master

python3 bMaster.py

Initialize the commands to be sent to the bot network.

3. Run the Bot Client

python3 bot.py

Monitor the C2 server logs for bot interactions and outputs.

