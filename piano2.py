import tkinter as tk
import pygame

key_notes = {
    '1': {'note': 'C', 'audio': '1.wav'},
    '2': {'note': 'D', 'audio': '2.wav'},
    '3': {'note': 'E', 'audio': '3.wav'},
    '4': {'note': 'F', 'audio': '4.wav'},
    '5': {'note': 'G', 'audio': '5.wav'},
    '6': {'note': 'A', 'audio': '6.wav'},
    '7': {'note': 'B', 'audio': '7.wav'},
    '8': {'note': 'C5', 'audio': '8.wav'},
    '9': {'note': 'D5', 'audio': '9.wav'},
    '0': {'note': 'E5', 'audio': '0.wav'}
}

key_colors = {
    '1': 'red',
    '2': 'orange',
    '3': 'yellow',
    '4': 'green',
    '5': 'blue',
    '6': 'indigo',
    '7': 'violet',
    '8': 'purple',
    '9': 'pink',
    '0': 'cyan'
}

key_sizes = {
    '1': (6, 12),
    '2': (8, 12),
    '3': (6, 12),
    '4': (8, 12),
    '5': (6, 12),
    '6': (8, 12),
    '7': (6, 12),
    '8': (8, 12),
    '9': (6, 12),
    '0': (8, 12)
}

# List of alternating key colors
key_colors = ['black', 'white']

# Initialize Pygame mixer
pygame.mixer.init()

# Function to play the sound corresponding to a piano key
def play_sound(key):
    note_data = key_notes.get(key)
    if note_data:
        audio_file = note_data['audio']
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

# Function to highlight the active key with color and animation
def highlight_key(key):
    btn = key_buttons.get(key)
    btn.config(bg='gray')
    btn.after(200, lambda: btn.config(bg=get_key_initial_color(key)))

# Function to get the initial background color for a key
def get_key_initial_color(key):
    color_index = int(key) % len(key_colors)
    return key_colors[color_index]

# Create the Tkinter window
window = tk.Tk()
window.title("Avan's Piano")

# Create a container for the piano keys
keys_frame = tk.Frame(window)
keys_frame.pack(pady=10)

# Create piano keys as buttons
key_buttons = {}
keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
is_long_key = True  # Flag to toggle between long and short keys
for key in keys:
    width, height = key_sizes.get(key, (4, 12))
    if is_long_key:
        btn = tk.Button(keys_frame, text=key, width=width, height=height*2, font=("Arial", 12), relief="raised",
                        command=lambda k=key: play_sound(k), bg=get_key_initial_color(key), fg='red')
    else:
        btn = tk.Button(keys_frame, text=key, width=width, height=height, font=("Arial", 12), relief="raised",
                        command=lambda k=key: play_sound(k), bg=get_key_initial_color(key), fg='red')
    btn.pack(side=tk.LEFT, padx=2)
    key_buttons[key] = btn
    is_long_key = not is_long_key  # Toggle the flag for the next key

# Function to handle keyboard events
def key_press(event):
    key = event.char
    play_sound(key)
    highlight_key(key)

# Bind the keyboard events to the key_press function
window.bind('<KeyPress>', key_press)

# Start the Tkinter event loop
window.mainloop()