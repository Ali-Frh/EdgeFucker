import os
import sys
import win32api
import urllib.parse
import subprocess

def find_chrome_path():
    # Possible Chrome installation paths
    possible_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Users\%s\AppData\Local\Google\Chrome\Application\chrome.exe" % os.environ.get('USERNAME')
    ]
    
    # Check each path
    for path in possible_paths:
        if os.path.isfile(path):
            return path
            
    # Default path if none found
    return r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        
def extract_url(args):
   ## win32api.MessageBox(0, " ".join(args), "proc", 0x10)

    # Check if args contain microsoft-edge protocol
    for arg in args:
        if arg.startswith("microsoft-edge:"):
            # Extract URL from ?url= parameter
            url_part = arg.split("?url=")[-1]
            try:
                # Decode URL-encoded string
                decoded_url = urllib.parse.unquote(url_part)
                # Ensure it starts with http:// or https://, add if missing
                if not decoded_url.startswith(("http://", "https://")):
                    decoded_url = "http://" + decoded_url
                return decoded_url
            except Exception:
                continue
    # Return first non-empty argument if it looks like a URL, otherwise None
    for arg in args:
        if arg and any(arg.startswith(proto) for proto in ["http://", "https://"]):
            return arg
    return None

def main():
    # Find Chrome path
    chrome_path = find_chrome_path()
    if not chrome_path:
        win32api.MessageBox(0, "Google Chrome not found. Please ensure Chrome is installed.", "Error", 0x10)
        sys.exit(1)

    # Get command-line arguments
    args = sys.argv[1:]  # Skip argv[0] (script name)
    print(f"Command line arguments: {args}")
    url = extract_url(args)
    print(f"Extracted URL: {url}")

    try:
        if url:
            # Launch Chrome with the extracted URL
            print(f"Launching Chrome with URL: {url}")
            print(f"Chrome path: {chrome_path}")
            subprocess.Popen([chrome_path, url])
        else:
            # Launch Chrome without arguments if no valid URL
            print("No URL found, launching Chrome without arguments")
            subprocess.Popen([chrome_path])
    except Exception as e:
        error_message = f"Failed to launch Google Chrome: {str(e)}"
        print(f"Error: {error_message}")
        win32api.MessageBox(0, error_message, "Error", 0x10)
        sys.exit(1)

if __name__ == "__main__":
    main()