# import pyttsx3

# # Initialize the engine
# engine = pyttsx3.init()


# # Set properties (optional)
# engine.setProperty('rate', 150) # Speed of speech

# # Command to speak
# engine.say("Hello, I am your Python assistant!")
# engine.runAndWait()

import pywhatkit

# Send a WhatsApp message at a specific time
# Format: phone_number (with country code), message, hour, minute
# pywhatkit.sendwhatmsg("+917696274536", "Hello from Python!", 0, 1)


text = "Hello, this is a test of the text to handwriting feature."
pywhatkit.text_to_handwriting(text, save_to="handwriting.png")

# Search on Google
# pywhatkit.search("https://sahil002620q.run.place")