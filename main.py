import sys
import glob
import asyncio
import logging
import importlib
import urllib3
import os
from flask import Flask
from threading import Thread

from pathlib import Path
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Flask app for port detection
app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Alpha Spam Bot is Running Successfully! ⚡"

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

def load_plugins(plugin_name):
    path = Path(f"RAUSHAN/modules/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"RAUSHAN.modules.{plugin_name}", path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["RAUSHAN.modules." + plugin_name] = load
    print("Altron has Imported " + plugin_name)


files = glob.glob("RAUSHAN/modules/*.py")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\n𝐀𝐥𝐩𝐡𝐚 𝐒𝐩𝐚𝐦 𝐁𝐨𝐭𝐬 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ⚡\nMy Master ---> @ll_ALPHA_BABY_lll")

# Start Flask server in a separate thread
flask_thread = Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

print(f"🌐 Flask server running on port {os.environ.get('PORT', 5000)}")

async def main():
    await asyncio.gather(
        X1.run_until_disconnected(),
        X2.run_until_disconnected(),
        X3.run_until_disconnected(),
        X4.run_until_disconnected(),
        X5.run_until_disconnected(),
        X6.run_until_disconnected(),
        X7.run_until_disconnected(),
        X8.run_until_disconnected(),
        X9.run_until_disconnected(),
        X10.run_until_disconnected()
    )

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
