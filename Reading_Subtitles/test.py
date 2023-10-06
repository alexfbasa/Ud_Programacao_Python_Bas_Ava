import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Set a specific voice (you can choose from available voices)
engine.setProperty('voice', voices[0].id)  # Index 1 may correspond to a different accent

engine.say("You aren't supposed to relieve me.")
engine.runAndWait()
