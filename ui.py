import numpy as np
import time
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from strings_and_consts import data, strings, language
from ui_func import set_working_folder, set_transcribe_model, set_denoiser, set_batch_size, set_audio_device, set_backend, set_vad
from audio_rec import audio_data

# Create UI thread 
def launch_ui():
    global language
    global data

    class SubtitleUIWindow(QMainWindow):
        def __init__(self):
            super(SubtitleUIWindow, self).__init__()
            self.setWindowTitle(strings[language]["app_name"])
            # On close, kill python process
            self.setAttribute(Qt.WA_QuitOnClose, True)
            data["widgets"] = []

            # Set backend label
            backendLabel = QLabel(strings[language]["select_backend"])
            backendLabel.setAlignment(Qt.AlignCenter)
            data["widgets"].append(backendLabel)

            # Select Backend
            selectBackend = QComboBox()
            selectBackend.addItems(data["backend"])
            selectBackend.setCurrentIndex(0)
            selectBackend.currentIndexChanged.connect(lambda: set_backend(selectBackend))
            data["widgets"].append(selectBackend)

            # Select Working Folder
            selectWorkingFolder = QPushButton(strings[language]["select_working_folder"])
            selectWorkingFolder.setGraphicsEffect(QGraphicsColorizeEffect())
            selectWorkingFolder.clicked.connect(lambda: set_working_folder(selectWorkingFolder))
            data["widgets"].append(selectWorkingFolder)

            # Transcibe model label
            selectTranscribeModelLabel = QLabel(strings[language]["select_transcribe_model"])
            selectTranscribeModelLabel.setAlignment(Qt.AlignCenter)
            data["widgets"].append(selectTranscribeModelLabel)

            # Transcribe model message
            selectTranscribeModelMessage = QLabel(strings[language]["distil_english_only_message"])
            selectTranscribeModelMessage.setAlignment(Qt.AlignCenter)
            data["widgets"].append(selectTranscribeModelMessage)

            # Select Transcribe Model
            selectTranscribeModel = QComboBox()
            selectTranscribeModel.addItems(data["model_size_options"])
            selectTranscribeModel.setCurrentIndex(0)
            selectTranscribeModel.currentIndexChanged.connect(lambda: set_transcribe_model(selectTranscribeModel))
            data["widgets"].append(selectTranscribeModel)

            #VAD Checkbox
            vadCheckbox = QCheckBox("VAD")
            vadCheckbox.setChecked(True)
            vadCheckbox.stateChanged.connect(lambda: set_vad(vadCheckbox.isChecked()))
            data["widgets"].append(vadCheckbox)

            # select denoiser label
            selectDenoiserLabel = QLabel(strings[language]["select_denoiser"])
            selectDenoiserLabel.setAlignment(Qt.AlignCenter)
            data["widgets"].append(selectDenoiserLabel)

            # Select Denoiser
            selectDenoiser = QComboBox()
            selectDenoiser.addItems(data["denosier_options"])
            selectDenoiser.setCurrentIndex(0)
            selectDenoiser.currentIndexChanged.connect(lambda: set_denoiser(selectDenoiser))
            data["widgets"].append(selectDenoiser)

            # Select Batch Size Label
            batchSizeLabel = QLabel(strings[language]["batch_size"])
            batchSizeLabel.setAlignment(Qt.AlignCenter)
            data["widgets"].append(batchSizeLabel)

            # Batch Size Message
            batchSizeMessage = QLabel(strings[language]["batch_size_message"])
            batchSizeMessage.setAlignment(Qt.AlignCenter)
            data["widgets"].append(batchSizeMessage)

            # Batch Size Input
            batchSizeInput = QLineEdit()
            batchSizeInput.setValidator(QIntValidator())
            batchSizeInput.setAlignment(Qt.AlignCenter)
            batchSizeInput.setText(str(data["set_batch_size"]))
            batchSizeInput.textChanged.connect(lambda: set_batch_size(batchSizeInput))
            data["widgets"].append(batchSizeInput)

            # Audio Device Label
            audioDeviceLabel = QLabel(strings[language]["audio_device"])
            audioDeviceLabel.setAlignment(Qt.AlignCenter)
            data["widgets"].append(audioDeviceLabel)

            # Select Audio Device
            selectAudioDevice = QComboBox()
            selectAudioDevice.addItems(data["audio_devices"])
            selectAudioDevice.setCurrentIndex(0)
            selectAudioDevice.currentIndexChanged.connect(lambda: set_audio_device(selectAudioDevice))
            data["widgets"].append(selectAudioDevice)

            # Start Button
            startButton = QPushButton(strings[language]["start"])
            startButton.setGraphicsEffect(QGraphicsColorizeEffect())
            # Create a function to set the start flag to True
            startButton.clicked.connect(lambda: interalStartFuncion())
            def interalStartFuncion():
                # We need to create an empty wav file, so the model can start processing real audio as it is received.
                # This is because the model takes a while to load.
                QMessageBox.information(startButton, "Info", strings[language]["preloading_message"])
                empty_audio = np.zeros(int(float(44100) * float(5)))
                audio_data.put(empty_audio)
                data.update({"start": True}) 
                time.sleep(15)
                data.update({"start_record": True})
                windowInProcess.show()
                self.hide()
            data["widgets"].append(startButton)

            def exit():
                data["start"] = False
                data["start_record"] = False
                self.hide()
                window.show()
                print(strings[language]["ctrl_c_exit"])
                sys.exit()
            exitButton = QPushButton(strings[language]["stop_and_close"])
            exitButton.setGraphicsEffect(QGraphicsColorizeEffect())
            exitButton.clicked.connect(lambda: exit())
            data["widgets"].append(exitButton)

            centralWidget = QWidget()
            layout = QVBoxLayout(centralWidget)
            layout.setSpacing(10)

            for option in data["widgets"]:
                layout.addWidget(option)
            self.setCentralWidget(centralWidget)
    class InSubtitleProcess(QMainWindow):
        def __init__(self):
            global timer
            super(InSubtitleProcess, self).__init__()
            self.setWindowTitle(strings[language]["app_name"])
            data["widgets_in_process"] = []
            #say subtiling from audiodevicename 
            subtitleLabel = QLabel(strings[language]["subtitle_progress"])
            subtitleLabel.setAlignment(Qt.AlignCenter)
            data["widgets_in_process"].append(subtitleLabel)

            miniDeviceLabel = QLabel(str(data["set_audio_device"]))
            miniDeviceLabel.setAlignment(Qt.AlignCenter)
            miniDeviceLabel.setStyleSheet("font-size: 8px;")
            data["widgets_in_process"].append(miniDeviceLabel)

            currentSubtitle = QLabel(strings[language]["nothing_subtitled"])
            currentSubtitle.setAlignment(Qt.AlignCenter)
            currentSubtitle.setWordWrap(True)
            currentSubtitle.setStyleSheet("font-size: 15px; font-weight: bold; background-color: #171717; color: #FFFFFF;")
            def updateSubtitle():
                global data
                currentSubtitle.setText(str(data["currentText"]))
            timer = QTimer()
            timer.timeout.connect(updateSubtitle)
            timer.start(500)
            data["widgets_in_process"].append(currentSubtitle)

            def exit():
                data["start"] = False
                data["start_record"] = False
                self.hide()
                window.show()
                audio_data.queue.clear()
            exitButton = QPushButton(strings[language]["stop_and_close"])
            exitButton.setGraphicsEffect(QGraphicsColorizeEffect())
            exitButton.clicked.connect(lambda: exit())
            data["widgets_in_process"].append(exitButton)
            
            centralWidget = QWidget()
            layout = QVBoxLayout(centralWidget)
            layout.setSpacing(10)

            for option in data["widgets_in_process"]:
                layout.addWidget(option)
                self.setCentralWidget(centralWidget)
            
    app = QApplication([])
    window = SubtitleUIWindow()
    windowInProcess = InSubtitleProcess()
    windowInProcess.hide()
    window.show()
    app.exec_()
