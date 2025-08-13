# import os

# os.makedirs("data/raw",exist_ok=True)
# print("Data directory created !")
# os.makedirs("src",exist_ok=True)
# print("Source directory created !")

import os

def create_dir(path):
    if os.path.exists(path):
        print(f"✅ Directory already exists: {path}")
    else:
        os.makedirs(path)
        print(f"📂 Directory created: {path}")

create_dir("data/raw")
create_dir("src")
