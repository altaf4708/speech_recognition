import speech_recognition as sr
import pyttsx3
import numpy as np
import sounddevice as sd

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to recognize speech, process audio, and perform actions
def process_audio(add_noise=False, remove_noise=False, auto_tune=False):
    with sr.Microphone() as source:
        print("Listening... Speak something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    # Apply auto-tuning if specified
    if auto_tune:
        audio = auto_tune_audio(audio)
    
    # Recognize speech using Google Web Speech API
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        
        # Apply noise addition if specified
        if add_noise:
            audio = add_noise_to_audio(audio)
            play_processed_audio(audio)
        
        # Apply noise removal if specified
        if remove_noise:
            audio = remove_noise_from_audio(audio)
            play_processed_audio(audio)
        
        # Play the audio after processing if not already played
        if not add_noise and not remove_noise:
            play_processed_audio(audio)
        
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Error retrieving results from Google Speech Recognition service:", e)

# Function to add white noise to audio
def add_noise_to_audio(audio_data, noise_level=0.05):
    # Placeholder function, not implemented in this example
    return audio_data

# Function to remove noise from audio (Simple low-pass filter)
def remove_noise_from_audio(audio_data, cutoff_freq=4000):
    # Placeholder function, not implemented in this example
    return audio_data

# Function to auto-tune audio
def auto_tune_audio(audio_data, pitch_shift=2):
    # Placeholder function, not implemented in this example
    return audio_data

# Function to play processed audio
def play_processed_audio(audio_data):
    # Convert audio data to numpy array of 16-bit integers
    audio_array = np.frombuffer(audio_data.frame_data, dtype=np.int16)
    
    # Play the audio through sounddevice
    sd.play(audio_array, audio_data.sample_rate)

# Provide options to the user
print("Choose an option:")
print("1. Process audio (recognize speech)")
option = int(input("Enter option number: "))

if option == 1:
    process_audio()
else:
    print("Invalid option.")

