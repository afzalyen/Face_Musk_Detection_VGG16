import os
import shutil
import pandas as pd



# Paths
csv_file = 'E:/Downloads/Covid-19-PIS.v2i.multiclass/_classes.csv'  # Replace with your CSV file path
print(1)

image_folder = 'E:/Downloads/Covid-19-PIS.v2i.multiclass/train'       # Replace with the folder containing your images
output_folder_with_mask = 'E:/Downloads/Covid-19-PIS.v2i.multiclass/with_mask'  # Replace with the folder for "with_mask"
output_folder_without_mask = 'E:/Downloads/Covid-19-PIS.v2i.multiclass/without_mask'  # Replace with the folder for "without_mask"
# Create output directories if they don't exist
os.makedirs(output_folder_with_mask, exist_ok=True)
os.makedirs(output_folder_without_mask, exist_ok=True)
# Load CSV file
df = pd.read_csv(csv_file)  



for _, row in df.iterrows():
    filename = row['filename']
    with_mask = row[' with_mask']  
    without_mask = row[' without_mask']
    src_path = os.path.join(image_folder, filename)

    if not os.path.exists(src_path):
        print(f"Image {filename} not found, skipping.")
        continue

    if with_mask == 1:
        dest_path = os.path.join(output_folder_with_mask, filename)
    elif without_mask == 1:
        dest_path = os.path.join(output_folder_without_mask, filename)
    else:
        print(f"Image {filename} does not have a clear label, skipping.")
        continue
    # Move the file
    shutil.move(src_path, dest_path)
print("Images successfully split into 'with_mask' and 'without_mask' folders.")