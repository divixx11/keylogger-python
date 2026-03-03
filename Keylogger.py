import pynput
from pynput.keyboard import Key, Listener

current_word = ""

def save_word(word):
    if word.strip() == "":
        return
    with open("log.txt", "a") as f:
        f.write(word + "\n")

def on_press(key):
    global current_word

    try:
        if key.char is not None:
            current_word += key.char
            print(key.char, end="", flush=True)

    except AttributeError:
        if key == Key.space or key == Key.enter:
            save_word(current_word)
            print()
            current_word = ""

        elif key == Key.backspace:
            current_word = current_word[:-1]
            print("\b \b", end="", flush=True) 

def on_release(key):
    if key == Key.esc:
        print("\nStopping listener...")
        return False

print("Keyboard monitor running (Press ESC to stop)")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
