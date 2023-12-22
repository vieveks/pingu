import speech_recognition as sr

def convert_audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)  # Record the audio file

        try:
            text = recognizer.recognize_google(audio_data)
            print("Converted Text: ", text)
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    audio_file_path = "path/to/your/audio/file.wav"  # Replace with your audio file path
    convert_audio_to_text(audio_file_path)