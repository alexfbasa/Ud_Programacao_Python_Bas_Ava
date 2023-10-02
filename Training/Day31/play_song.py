import pygame

# Initialize the mixer module (you need to do this before playing audio)
pygame.mixer.init()

# Load the song
pygame.mixer.music.load('ability__gb_1.mp3')

# Play the song
pygame.mixer.music.play()

# Add a delay to ensure the song plays completely before the script exits
pygame.time.delay(10000)  # 10 seconds (adjust as needed)

# Stop the song
pygame.mixer.music.stop()
