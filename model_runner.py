import soundfile 
import io
import os
import contextlib
import numpy as np
import time
import stable_whisper
import textwrap
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from audio_rec import audio_data
from strings_and_consts import data, strings
baseModel = None

def model_runner():
    global data
    global strings
    global baseModel
    while True:
        # CPUs don't like doing stuff forever, so let's give it a break.
        time.sleep(0.1)
        if not audio_data.empty() and data["start"] == True:
            if data["set_backend"] == data["backend"][0]:
                baseModel = stable_whisper.load_hf_whisper(data["set_transcribe_model"])
            elif data["set_backend"] == data["backend"][1]:
                baseModel = stable_whisper.load_faster_whisper(data["set_transcribe_model"])
            elif data["set_backend"] == data["backend"][2]:
                print(f"{Fore.LIGHTRED_EX}Whisper.CPP is not supported yet.{Style.RESET_ALL}")
            start_time = time.time()
            print(f"{Fore.LIGHTGREEN_EX}Audio received. Processing...{Style.RESET_ALL}")
            # While the queue is not empty, get each item and append it
            recording = audio_data.get()
            while not audio_data.empty():
                 if recording.ndim > new_audio_data.ndim:
                    new_audio_data = np.expand_dims(new_audio_data, axis=0)
                 else:
                    recording = np.expand_dims(recording, axis=0)
            recording = np.concatenate((recording, audio_data.get()))
            recording = np.squeeze(recording)
            # Convert numpy array to PCM_16 wav bytes in memory 
            with io.BytesIO() as f:
                soundfile.write(f, recording, 44100, 'PCM_16', format="WAV")
                audio_bytes = f.getvalue()
                user_text = baseModel.transcribe(audio_bytes, vad=data["set_vad"], word_timestamps="true", denoiser=data["set_denoiser"], 
                                                 batch_size=int(data["set_batch_size"]), use_word_position="true")
                end_time = time.time() - start_time
                print(f"{Fore.LIGHTGREEN_EX}Audio processed. Time taken: {end_time} seconds.{Style.RESET_ALL}")
                print(f"{Fore.LIGHTGREEN_EX}Transcription: {user_text.text}{Style.RESET_ALL}")
                data["currentText"] = user_text.text
                #Add new lines, limiting it to 30 characters per line
                split_text = textwrap.fill(user_text.text, width=30)
                # Open file, with write permissions, remove the old text and write the new text
                with open(data["set_working_folder"], "w") as f:
                    f.write(split_text)

            
