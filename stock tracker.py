import os
import shutil

# Define the root directory and the folders to create
root_dir = 'd:/'
image_folder = os.path.join(root_dir, 'images')
document_folder = os.path.join(root_dir, 'documents')
video_folder = os.path.join(root_dir, 'videos')

# Create the folders if they don't exist
if not os.path.exists(image_folder):
    os.makedirs(image_folder)
if not os.path.exists(document_folder):
    os.makedirs(document_folder)
if not os.path.exists(video_folder):
    os.makedirs(video_folder)

# Iterate through all files in the root directory
for filename in os.listdir(root_dir):
    filepath = os.path.join(root_dir, filename)
    if os.path.isfile(filepath):  # Check if it's a file
        # Get the file extension
        file_ext = os.path.splitext(filename)[1].lower()

        # Move the file to the corresponding folder
        if file_ext in ['.jpg', '.jpeg', '.png', '.gif']:
            shutil.move(filepath, image_folder)
        elif file_ext in ['.doc', '.docx', '.pdf', '.txt']:
            shutil.move(filepath, document_folder)
        elif file_ext in ['.mp4', '.avi', '.mov']:
            shutil.move(filepath, video_folder)
        else:
            print(f"Unknown file type: {filename}")