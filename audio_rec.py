import sounddevice
import queue
import time
import sys
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from strings_and_consts import data, strings
# Make a queue for the audio data
audio_data = queue.Queue()

def audio_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    audio_data.put(indata.copy())

def start_record():
    global data
    global strings
    while True:
        # CPUs don't like doing stuff forever, so let's give it a break
        time.sleep(0.1)
        if data["start"] == True and data["start_record"] == True:
            # Get the audio device
            audio_device = data["set_audio_device"]
            # Get the audio delay
            sounddevice.default.device = audio_device
            print(f"{Fore.LIGHTRED_EX}Recording audio...{Style.RESET_ALL}")

            with sounddevice.InputStream(samplerate=44100, channels=1, callback=audio_callback):
                while data["start_record"] == True:
                    time.sleep(0.1)