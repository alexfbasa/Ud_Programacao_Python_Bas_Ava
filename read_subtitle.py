import tkinter as tk
import pysrt
import re

def read_subtitle_file(file_path):
    try:
        subtitles = pysrt.open(file_path, encoding='latin1')
        return subtitles
    except Exception as e:
        print(f"Error reading subtitle file: {e}")
        return None

def clean_text(subtitle_text):
    # Remove HTML tags and special formatting
    clean_text = re.sub('<.*?>', '', subtitle_text)
    return clean_text

def display_subtitles(subtitles):
    root = tk.Tk()
    root.title("Subtitle Reader")

    subtitle_text = tk.StringVar()
    subtitle_index = tk.StringVar()
    subtitle_time = tk.StringVar()

    subtitle_index_label = tk.Label(root, textvariable=subtitle_index, font=("Arial", 14, "bold"))
    subtitle_index_label.pack()

    subtitle_time_label = tk.Label(root, textvariable=subtitle_time, font=("Arial", 12))
    subtitle_time_label.pack()

    subtitle_text_label = tk.Label(root, textvariable=subtitle_text, font=("Arial", 12), wraplength=500)
    subtitle_text_label.pack()

    def update_subtitle(subtitle):
        subtitle_index.set(f"Index: {subtitle.index}")
        subtitle_time.set(f"Time: {subtitle.start} --> {subtitle.end}")
        subtitle_text.set(clean_text(subtitle.text))

    def next_subtitle(event=None):
        nonlocal current_subtitle_index
        if current_subtitle_index < len(subtitles) - 1:
            current_subtitle_index += 1
            update_subtitle(subtitles[current_subtitle_index])

    def previous_subtitle(event=None):
        nonlocal current_subtitle_index
        if current_subtitle_index > 0:
            current_subtitle_index -= 1
            update_subtitle(subtitles[current_subtitle_index])

    current_subtitle_index = 0
    update_subtitle(subtitles[current_subtitle_index])

    root.bind("<Right>", next_subtitle)
    root.bind("<Left>", previous_subtitle)
    root.mainloop()


# Example usage
subtitle_file_path = 'Reminiscence.2021.srt'
subtitles = read_subtitle_file(subtitle_file_path)

if subtitles:
    display_subtitles(subtitles)
