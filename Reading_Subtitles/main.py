import tkinter as tk
from tkinter import filedialog
from gtts import gTTS
import vlc  # for audio playback

# Specify the path to the libvlc.dll file and VLC options
vlc_options = "--no-xlib --quiet --fullscreen --no-video-title"
vlc_instance = vlc.Instance(vlc_options + " --file-caching=3000")

# Create a list to store subtitle lines
subtitle_lines = []


# Function to open and parse the subtitle file
def open_subtitle():
    subtitle_file = filedialog.askopenfilename(filetypes=[("Subtitle Files", "*.srt")])
    with open(subtitle_file, 'r', encoding='utf-8') as file:
        subtitle_data = file.read()
        # Split subtitle data into individual dialogue lines
        subtitle_lines.extend(subtitle_data.split('\n\n'))


def start():
    # Check if there are any subtitle lines to read
    if subtitle_lines:
        # Get the next dialogue line and remove it from the list
        dialogue = subtitle_lines.pop(0)

        # Extract the dialogue text and remove timestamps
        dialogue_text = '\n'.join(line.strip() for line in dialogue.split('\n')[2:])

        # Use gTTS to convert the dialogue text to speech
        tts = gTTS(text=dialogue_text, lang='en')
        tts.save("temp.mp3")

        # Load and play the audio
        media = vlc_instance.media_new("temp.mp3")
        player.set_media(media)
        player.play()
    else:
        print("No more subtitle lines to read")


# Create the VLC media player for audio playback
vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()

root = tk.Tk()
root.title("English Learning Program")

open_button = tk.Button(root, text="Open Subtitle", command=open_subtitle)
start_button = tk.Button(root, text="Start", command=start)
repeat_button = tk.Button(root, text="Repeat")
next_button = tk.Button(root, text="Next Phrase")

open_button.pack()
start_button.pack()
repeat_button.pack()
next_button.pack()

root.mainloop()
