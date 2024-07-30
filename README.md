# RealTime-TS
This is a Python application built using PyQt and Stable-TS to provide real time subtitling for any audio input (or output) audio device. The application heavly relies on the Stable-TS library to provide the transcription of audio. This application is only supported on Linux operating systems for now. Other operating systems may work, but have not been tested on. It is a work in progress and is not yet ready for production use.

As of currently, the application requires a CUDA enabled GPU to run. Apple Sllicon and AMD GPUs may work, but have not been tested on. The application is not yet optimized for CPU only usage. Almost any modern NVIDIA GPU should work, with CUDA toolkit installed. 

## Features

- **Real-Time Audio Transcription**: Utilize the power of Stable-TS for instant audio to text conversion, ensuring litte lag between speech and subtitles.
- **Audio Device Selection**: Choose any connected audio input or output device for transcription, offering flexibility for various use cases.
- **Linux Compatibility**: Optimized for Linux environments, ensuring smooth operation and integration with your system's audio infrastructure.
- **Offline Mode**: Use the application without an active internet connection, ensuring privacy and security for sensitive audio data. Before using the application in offline mode, you need to use the application in online mode once to download the required models.

## Installation

### Linux Automated Installation
1. Download the installation script and make it executable.
```bash
wget https://raw.githubusercontent.com/KUKHUA/ui-sub-live-rewrite/main/scripts/installer.sh
chmod +x installer.sh
```

2. Run the installation script.
```bash
./installer.sh
```

### Windows Automated Installation
Not yet supported.

### Manual Installation
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

1. Select a backend, "Stable-TS Transformers" is recommended for most use cases.

2. Select a working folder, this is where the application will store the subtile output as a .TXT file.

3. Select a transcription model, the default model is the best for most use cases.

4. Check the VAD (Voice Activity Detection) box if you want the application to enable VAD.

5. Select a denoiser model, a denoiser model removes background noise, such as music or traffic.

6. Select a batch size, the batch size is the number of audio frames processed at once. Considering the audio data is short, a smaller batch size is recommended.

7. Select an audio device, this is the audio device the application will transcribe.