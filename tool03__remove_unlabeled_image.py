import os
import shutil

# Set the directory paths
frames_dir = "frames"
unlabeled_dir = "unlabeled"  # Place 'unlabeled' folder outside 'frames'

# Create the 'unlabeled' directory if it doesn't exist
os.makedirs(unlabeled_dir, exist_ok=True)

# Loop through all files in the frames directory
for file_name in os.listdir(frames_dir):
    if file_name.endswith(".jpg"):  # Check only image files
        # Check for the corresponding .txt file
        label_file = os.path.splitext(file_name)[0] + ".txt"
        label_path = os.path.join(frames_dir, label_file)

        # Move image if corresponding .txt file is missing
        if not os.path.exists(label_path):
            image_path = os.path.join(frames_dir, file_name)
            shutil.move(image_path, unlabeled_dir)
            print(f"Moved {file_name} to 'unlabeled' folder.")

# To run this: python tool03__remove_unlabeled_image.py
