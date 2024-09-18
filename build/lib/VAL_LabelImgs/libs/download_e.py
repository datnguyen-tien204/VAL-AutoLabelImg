import requests
import os
import shutil

url = "https://raw.githubusercontent.com/matlab-deep-learning/pretrained-yolo-v4/main/src/%2Bhelper/coco-classes.txt"
filename = "classes.txt"


def get_classestxt(original_root: str, local_source: str):
    filepath = os.path.join(original_root, filename)

    try:
        # Thử tải file từ URL
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            with open(filepath, "w") as file:
                file.write(response.text)
            print("File downloaded and saved successfully.")
        else:
            raise requests.ConnectionError
    except (requests.ConnectionError, requests.Timeout):
        # Nếu không tải được, sao chép từ folder A (local_source)
        local_file = os.path.join(local_source, filename)
        if os.path.exists(local_file):
            shutil.copy(local_file, filepath)
            print(f"File copied from {local_source} to {original_root}.")
        else:
            print("Local file does not exist.")
