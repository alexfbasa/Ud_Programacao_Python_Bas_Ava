import requests
import pygame
from io import BytesIO

url = "https://www.oxfordlearnersdictionaries.com/media/english/uk_pron/a/aba/aband/abandon__gb_2.mp3"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Send a GET request to the MP3 URL
response = requests.get(url, headers=headers, verify=False)

# Check if the request was successful
if response.status_code == 200:
    # Initialize the pygame mixer with the video system set to dummy
    pygame.init()
    pygame.mixer.init()

    # Create a dummy screen (needed for audio initialization)
    pygame.display.set_mode((1, 1))

    # Create a BytesIO object from the response content
    mp3_data = BytesIO(response.content)

    # Set the volume of channel 0
    pygame.mixer.Channel(0).set_volume(5.0)  # Set the volume to max

    # Play the MP3 using channel 0
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(mp3_data))

    # Wait for the audio to finish playing (you can add other code here if needed)
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.event.wait()

    # Quit pygame
    pygame.quit()

else:
    print("Failed to retrieve the MP3 file. Status code:", response.status_code)
