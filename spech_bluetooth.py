import speech_recognition as sr
import pyttsx3
import bluetooth

# Function to transmit data via Bluetooth
def transmit_data_via_bluetooth(data):
    # Replace "00:00:00:00:00:00" with the MAC address of your Bluetooth device
    target_address = "1d:c1:b7:14:1d:6a"
    
    try:
        # Create a Bluetooth socket
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        
        # Connect to the target Bluetooth device
        sock.connect((target_address, 1))
        
        # Send data over Bluetooth
        sock.send(data.encode())
        
        # Close the Bluetooth socket
        sock.close()
        print("Data transmitted successfully via Bluetooth.")
    except Exception as e:
        print("Error transmitting data via Bluetooth:", e)

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Listening... Speak something...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
    audio = recognizer.listen(source)

# Recognize speech using Google Web Speech API
try:
    print("Recognizing...")
    text = recognizer.recognize_google(audio)
    print("You said:", text)
    
    # Transmit the recognized speech via Bluetooth
    transmit_data_via_bluetooth(text)
    
    # Convert recognized speech to audio and play it on the speaker
    engine.say(text)
    engine.runAndWait()
    
except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
except sr.RequestError as e:
    print("Error retrieving results from Google Speech Recognition service:", e)
