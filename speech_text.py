import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
        return None

if __name__ == "__main__":
    speech_to_text()
