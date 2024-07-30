import threading
from ui import launch_ui
from audio_rec import start_record
from model_runner import model_runner
from strings_and_consts import data

def main():
    ui_thread = threading.Thread(target=launch_ui)
    audio_thread = threading.Thread(target=start_record)
    model_thread = threading.Thread(target=model_runner)

    model_thread.start()
    ui_thread.start()
    audio_thread.start()

    # Join threads to ensure they complete before the main thread exits
    model_thread.join()
    ui_thread.join()
    audio_thread.join()

if __name__ == "__main__":
    main()