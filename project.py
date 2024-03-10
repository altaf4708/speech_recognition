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
    # Convert audio data to numpy array
    audio_array = np.frombuffer(audio_data.frame_data, dtype=np.int16)
    
    # Generate white noise
    noise = np.random.normal(scale=noise_level * np.max(audio_array), size=len(audio_array))
    
    # Add noise to audio data
    audio_array_with_noise = audio_array + noise
    
    # Create new AudioData object with noise
    return sr.AudioData(audio_array_with_noise.tobytes(), audio_data.sample_rate, audio_data.sample_width)

# Function to remove noise from audio (Simple low-pass filter)
def remove_noise_from_audio(audio_data, cutoff_freq=4000):
    # Convert audio data to numpy array
    audio_array = np.frombuffer(audio_data.frame_data, dtype=np.int16)
    
    # Create new AudioData object with noise removed
    return sr.AudioData(audio_array.tobytes(), audio_data.sample_rate, audio_data.sample_width)

# Function to auto-tune audio
def auto_tune_audio(audio_data, pitch_shift=2):
    # Convert audio data to numpy array
    audio_array = np.frombuffer(audio_data.frame_data, dtype=np.int16)
    
    # Create new AudioData object with auto-tuned audio
    return sr.AudioData(audio_array.tobytes(), audio_data.sample_rate + pitch_shift, audio_data.sample_width)


# Function to play processed audio
# Function to play processed audio
def play_processed_audio(audio_data):
    # Convert audio data to numpy array of 16-bit integers
    audio_array = np.frombuffer(audio_data.frame_data, dtype=np.int16)
    
    # Convert the audio array to a bytes object
    audio_bytes = audio_array.tobytes()
    
    # Play the audio through the system's speakers
    engine.say("")
    engine.say("Playing processed audio")
    engine.runAndWait()
    engine.say(audio_bytes)
    engine.runAndWait()



# Provide options to the user
print("Choose an option:")
print("1. Process audio (recognize speech)")
print("2. Add noise to audio and play")
print("3. Remove noise from audio and play")
option = int(input("Enter option number: "))

if option == 1:
    auto_tune = input("Enable auto-tune? (y/n): ").lower() == 'y'
    process_audio(auto_tune=auto_tune)
elif option == 2:
    process_audio(add_noise=True)
elif option == 3:
    process_audio(remove_noise=True)
else:
    print("Invalid option.")
