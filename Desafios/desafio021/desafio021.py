from posixpath import dirname
import pygame
from os import path

AUDIO_PATH = path.join(path.dirname(__file__), "audio.mp3")

print('Você está escutando: Elektronomia - Sky High pt. II [NCS Release]')
print('Music provided by NoCopyrightSounds.\nWatch: https://youtu.be/lG6HVrrXup8')
print('Free Download / Stream: http://ncs.io/SkyHigh2')

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(AUDIO_PATH)
pygame.mixer.music.play()

while True:
    continue