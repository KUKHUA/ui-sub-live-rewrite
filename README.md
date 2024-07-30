# RealTime-TS
This is a Python application built using PyQt and Stable-TS to provide real time subtitling for any audio input (or output) audio device. The application heavly relies on the Stable-TS library to provide the transcription of audio. This application is only supported on Linux operating systems for now. Other operating systems may work, but have not been tested on. It is a work in progress and is not yet ready for production use.

As of currently, the application requires a CUDA enabled GPU to run. Apple Sllicon and AMD GPUs may work, but have not been tested on. The application is not yet optimized for CPU only usage. Almost any modern NVIDIA GPU should work, with CUDA toolkit installed. 

## Features

- **Real-Time Audio Transcription**: Utilize the power of Stable-TS for instant audio to text conversion, ensuring litte lag between speech and subtitles.
- **Audio Device Selection**: Choose any connected audio input or output device for transcription, offering flexibility for various use cases.
- **Linux Compatibility**: Optimized for Linux environments, ensuring smooth operation and integration with your system's audio infrastructure.
- **Offline Mode**: Use the application without an active internet connection, ensuring privacy and security for sensitive audio data. Before using the application in offline mode, you need to use the application in online mode once to download the required models.

## Installation
1. Clone the repository to your local machine.
```bash
git clone https://github.com/KUKHUA/RealTime-TS-V2.git
```

2. Install the required dependencies. It is recommended to use a virtual environment to avoid conflicts with other Python packages.
```bash
# Create a virtual environment
python -m venv RealTime-TS

# For Linux or MacOS: 
# source RealTime-TS/bin/activate

# For Windows: 
# .\RealTime-TS\Scripts\activate

# Navigate to the project directory
cd RealTime-TS-V2

# Change the ending of the file depending on your operating system.
# Install the required dependencies
pip install -r requirements-linux.txt
```
3. Run the application.
```bash
python main.py
```

4. If you get any errors, please check the terminal output and install the required dependencies.

## Usage

2. Select a transciber model from the dropdown menu. The "distil-large-v3" model is recommended for English transcription. The "distil-large-v3" model is a fine-tuned version of the "large-v3" model. If you are offline, you must use a model that you have downloaded before. If you are online, you can use any model.

3. Select a denoiser model from the dropdown menu. Denoiser models are used to remove background noise from the audio input. A denoiser model is not required, but it is recommended to use one for better transcription results. Again, if you are offline, you must use a model that you have downloaded before. If you are online, you can use any model.

4. Input a "Batch Size" value. The batch size value determines the number of audio frames processed at once. A higher batch size value can increase the transcription speed at higher audio delays, but may crash the program or your GPU to run out of memory. At lower audio delays, a higher batch size value may not increase the transcription speed at all. It is also worth noting that a less powerful GPU may need need a higher batch size to get the same transcription speed as a more powerful GPU. But, a less powerful GPU may not be able to handle a higher batch size value.

5. Select an audio input or output device from the dropdown menu. The application will only transcribe audio from the selected device.

6. Click the "Start" button to begin transcription. This will hide the previous window, and show the in progress window. To stop transcription, click the "Stop" button.