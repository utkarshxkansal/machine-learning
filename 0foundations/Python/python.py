import pyjokes
import pyttsx3
joke = pyjokes.get_joke()
engine = pyttsx3.init()
engine.say(joke)
engine.runAndWait()
print(joke)
print("utkarsh")
print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

Twinkle, twinkle, little star,
How I wonder what you are!''')