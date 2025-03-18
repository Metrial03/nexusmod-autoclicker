import pyautogui
import time

def locate_image_with_retry(image_path, retries=5, delay=2):
    for attempt in range(retries):
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location is not None:
                return location
        except pyautogui.ImageNotFoundException:
            pass  # Ignore the exception and try again
        time.sleep(delay)  # Wait before the next attempt
    return None  # Return None if the image is not found after all retries

def find_and_click(image):
    location = locate_image_with_retry(image)
    if location:
        pyautogui.click(location)
        return True
    else:
        return False

def main():
    download_button = 'download.png'
    slow_download_button = 'slowdownload.png'

    while True:
        if not find_and_click(download_button):
            continue
        time.sleep(10)
        if not find_and_click(slow_download_button):
            continue
        time.sleep(10)

if __name__ == "__main__":
    main()