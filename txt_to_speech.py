import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        text = input("Enter the text you want to convert to speech: ")
        if text =="q":
            text_to_speech("Bye Bye sir !!")
            break
        else:
            text_to_speech(text)
        



