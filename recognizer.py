import speech_recognition as sr
import keyboard

def listen_and_convert():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening... Speak something.")
        audio_data = recognizer.listen(source, timeout=None)  # No timeout

        try:
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

def stop_listening():
    print("Stopping the listener.")
    keyboard.press_and_release('esc')  # Change 'esc' to the key you want to use

if __name__ == "__main__":
    keyboard.add_hotkey('ctrl+k', stop_listening)  # Change 'ctrl+alt+s' to your desired hotkey
    listen_and_convert()
