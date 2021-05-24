"""
Here ois the main Biz Logic of the any hardware
"""
from dotenv import load_dotenv
from os import getenv
from time import sleep
import requests, sound_ai

load_dotenv()
DOMAIN = getenv('CLOUD_DOMAIN')

device = {
    "SSID": getenv("SSID"),
    "Owner": getenv("OWNER_ID"),
    "Type": getenv("TYPE"),
}


def connect_to_wifi() -> bool:
    # Todo: load from save data the wifi and pass word
    # Todo: if not exsists
    # Todo: start local hotspot
    pass


def start_local_hotspot() -> bool:
    # Todo: start local hotspot
    # Todo: create login GUI
    pass


def is_connected():
    return requests.get(DOMAIN).status_code == 200


def main1():
    s_ai = sound_ai.AudioAI()
    print("Listening...")
    sen = s_ai.recognize_audio_stream(f"Untitled 2.wav")
    print(f'detected sound translation to text...')
    print(f'.')
    sleep(0.3)
    print(f'.')
    sleep(0.3)
    print(f'.')
    sleep(0.3)
    print("----" * 5)
    print(f"{sen}")
    print("----" * 5)
    try:
        j = {
            "device": device,
            "sentence": sen
        }
        try:
            res = requests.post(DOMAIN + '/api/analysis', json=j)
            if res.status_code == 200:
                # Todo: if needed some more response logic
                pass
            else:
                # Todo: some error occurred talking to server
                # Todo: some more error communication
                pass
        except ConnectionError as e:
            print("Connection error", e.strerror)
    except sound_ai.UnableToParse:
        print("Log unable to hear anything")


if __name__ == '__main__':
    print("----" * 5)
    print("IOT system")
    print("----" * 5)
    while True:
        # check if server is alive
        try:
            res = requests.get(DOMAIN)
        except ConnectionError as e:
            print("Connection error", e.strerror)
        if res.status_code != 200:
            while True:
                # try rapidity to reconnect
                connected = connect_to_wifi()
                if not connected:
                    # if no wifi was accessed then ope hotspot and let the user define it
                    # should blink led or something on hardware
                    connected = start_local_hotspot()
                    if connected:
                        break
            sleep(0.5)
        main1()
        y = input("run again? y/n ")
        if y == 'n':
            break
