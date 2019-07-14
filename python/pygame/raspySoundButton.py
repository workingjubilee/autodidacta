from pygame import mixer
from gpiozero import Button

# Constructed from memory, may contain errors.

mixer.init()

hatsune = mixer.Sound("~/class/ambi_whoosh.wav")
def play_sound():
    hatsune.play()

btn = Button(14)
btn.when_pressed = play_sound

while True:
    pass