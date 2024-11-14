import os
from PIL import Image
import imagehash
import shutil

# Set the folder path containing your images
folder_path = 'frames'
duplicates_folder = 'duplicates'

# Ensure the duplicates folder exists
os.makedirs(duplicates_folder, exist_ok=True)

# Dictionary to store image hashes and paths
image_hashes = {}

# Dictionary to store duplicates with original as the key
duplicates_dict = {}

# Supported image file extensions
image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"}

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Check if the file has a valid image extension
    if not any(filename.lower().endswith(ext) for ext in image_extensions):
        print(f"Skipping non-image file: {filename}")
        continue

    # Open and hash each image
    try:
        with Image.open(file_path) as img:
            # Generate a hash for the image
            img_hash = imagehash.average_hash(img)

            # Check if the hash already exists
            if img_hash in image_hashes:
                original_file = image_hashes[img_hash]
                if original_file not in duplicates_dict:
                    duplicates_dict[original_file] = []
                duplicates_dict[original_file].append(file_path)

                # Move duplicate to the "duplicates" folder
                duplicates_destination = os.path.join(duplicates_folder, filename)
                shutil.move(file_path, duplicates_destination)
                print(f"Moved duplicate: {file_path} -> {duplicates_destination}")
            else:
                image_hashes[img_hash] = file_path
    except Exception as e:
        print(f"Could not process {filename}: {e}")

# Output duplicates in tree structure
if duplicates_dict:
    print("Duplicate images found and moved:")
    for original, duplicates in duplicates_dict.items():
        print(f"Original: {original}")
        for duplicate in duplicates:
            print(f"Moved to 'duplicates' folder: {duplicate}")
else:
    print("No duplicate images found.")

#This is how to run the program in the termial type: (python filename.py) 
# python tool02__remove_image_duplicates.py