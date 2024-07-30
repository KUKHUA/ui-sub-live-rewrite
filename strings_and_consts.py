import torch
import sounddevice
import os
# Store all strings in this file
strings = { "English": {}}
data = {}
strings["English"]["loading_hf_message"] = "Loading HuggingFace model."
strings["English"]["total_process_time_message"] = "Total Process Time: "
strings["English"]["preloading_message"] = "After you press OK the model will be preloaded. The window might freeze or close. Please wait."
strings["English"]["stop_and_close"] = "Stop and Close"
strings["English"]["threads_started"] = "All threads have started."
strings["English"]["app_name"] = "RealTime-TS"  
strings["English"]["select_working_folder"] = "Select Working Folder"
strings["English"]["select_transcribe_model"] = "Select Transcribe Model"
strings["English"]["select_denoiser"] = "Select Denoiser:"
strings["English"]["select_device"] = "Select Device to Run the Model On:"
strings["English"]["select_backend"] = "Select Backend:"
strings["English"]["audio_device"] = "Audio Device to Transcibe:"
strings["English"]["start"] = "Start"
strings["English"]["distil_english_only_message"] = "Distil models and models marked with '.en' only support English."
strings["English"]["batch_size"] = "Batch Size:"
strings["English"]["batch_size_message"] = "Increasing the batch size can improve speed, but too high of a value can cause the program to crash.\nThe optimal batch size depends on the model size, denoiser and your computer's hardware."
strings["English"]["working_folder_console"] = "Working Folder is now set to"
strings["English"]["working_folder_console_error"] = "Working folder does not exist, telling the user to select a new one."
strings["English"]["working_folder_message_box_error"] = "Invalid working folder, it does not exist. Please select a new one."
strings["English"]["transcribe_model_console"] = "Transcribe model is now set to"
strings["English"]["denoiser_console"] = "Denoiser is now set to"
strings["English"]["batch_size_console"] = "Batch Size is now set to"
strings["English"]["audio_device_console"] = "Audio Device is now set to"
strings["English"]["backend_console"] = "Backend is now set to"
strings["English"]["vad_console"] = "VAD is now"
strings["English"]["subtitle_progress"] = "Subtitle in progress..."
strings["English"]["nothing_subtitled"] = "Nothing has been subtitled yet."
strings["English"]["ctrl_c_exit"] = "Press Ctrl+C to exit."

# Options are language independent DO NOT TRANSLATE
data["denosier_options"] = ["None", "demucs", "dfnet", "noisereduce"]
data["model_size_options"] = [
"distil-whisper/distil-large-v3",
"large-v3",
"medium",
"medium.en",
"small",
"small.en",
"base",
"base.en",
"tiny",
"tiny.en",
]
data["whisper_cpp_models"] = [
    ["disrtil-large-v3", "https://www.google.com"],
]
data["backend"] = [
    "Stable-TS Transformers (HuggingFace)",
    "Stable-TS FasterWhisper",
]
data["device"] = []
data["audio_devices"] = []
data["start"] = False
data["start_record"] = False

# Set default values
data["set_working_folder"] = os.path.join(os.getcwd(),"subtitle_output.txt")
data["set_transcribe_model"] = "distil-whisper/distil-large-v3"
data["set_denoiser"] = None
# This should be small enough to not crash the program for most users (at least with a GPU), but let me know if it does.
data["set_batch_size"] = 10
# get default audio device name
data["set_audio_device"] = sounddevice.default.device
data["set_backend"] = data["backend"][0]
data["set_vad"] = True
data["currentText"] = "Nothing has been subtitled yet."

# Get all audio devices
for device in sounddevice.query_devices():
    data["audio_devices"].append(device["name"])
# Remove duplicates
data["audio_devices"] = list(set(data["audio_devices"]))

# Set to False in production
data["debug"] = False

# print out all the data
if data["debug"] == True:
    print(data)


# TODO: make a language selection dialog
language = "English"
