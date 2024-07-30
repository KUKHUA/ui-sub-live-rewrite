import os
from strings_and_consts import data, strings, language
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from PyQt5.QtWidgets import QFileDialog, QMessageBox

def set_vad(qt_object):
    vad = qt_object
    print(f"{Fore.GREEN}{strings[language]["vad_console"]} {Fore.BLUE}{vad}{Style.RESET_ALL}")
    data["set_vad"] = vad

def set_backend(qt_object):
    backend = qt_object.currentText()
    print(f"{Fore.GREEN}{strings[language]["backend_console"]} {Fore.BLUE}{backend}{Style.RESET_ALL}")
    data["set_backend"] = backend

def set_working_folder(qt_object):
    working_folder = QFileDialog.getExistingDirectory()
    if os.path.exists(working_folder):
        print(f"{Fore.GREEN}{strings[language]["working_folder_console"]} {Fore.BLUE}{working_folder}{Style.RESET_ALL}")
        data["set_working_folder"] = os.path.join(working_folder,"subtitle_output.txt")
    else:
        print(f"{Fore.YELLOW}{strings[language]["working_folder_console_error"]}{Style.RESET_ALL}")
        QMessageBox.warning(qt_object, "Error", strings[language]["working_folder_message_box_error"])

def set_transcribe_model(qt_object):
    model = qt_object.currentText()
    print(f"{Fore.GREEN}{strings[language]["transcribe_model_console"]} {Fore.BLUE}{model}{Style.RESET_ALL}")
    data["set_transcribe_model"] = model

def set_denoiser(qt_object):
    denoiser = qt_object.currentText()
    print(f"{Fore.GREEN}{strings[language]["denoiser_console"]} {Fore.BLUE}{denoiser}{Style.RESET_ALL}")
    if denoiser == "None":
        denoiser = None
    data["set_denoiser"] = denoiser

def set_batch_size(qt_object):
    batch_size = qt_object.text()
    print(f"{Fore.GREEN}{strings[language]["batch_size_console"]} {Fore.BLUE}{batch_size}{Style.RESET_ALL}")
    data["set_batch_size"] = batch_size

def set_audio_device(qt_object):
    audio_device = qt_object.currentText()
    print(f"{Fore.GREEN}{strings[language]["audio_device_console"]} {Fore.BLUE}{audio_device}{Style.RESET_ALL}")
    data["set_audio_device"] = audio_device