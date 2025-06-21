import os
import pydicom
import numpy as np
import cv2
from tqdm import tqdm

def convert_dicom_to_jpg(root_folder, output_folder, target_size=None):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Gather all .dcm files first
    dicom_files = []
    for subfolder in os.listdir(root_folder):
        dicom_path = os.path.join(root_folder, subfolder, "DICOM_anon")
        if not os.path.isdir(dicom_path):
            continue  # Skip if no DICOM_anon folder

        for filename in os.listdir(dicom_path):
            if filename.endswith(".dcm"):
                dcm_file = os.path.join(dicom_path, filename)
                dicom_files.append((subfolder, dcm_file))

    print(f"Total DICOM files found: {len(dicom_files)}")

    # Process with progress bar
    for subfolder, dcm_file in tqdm(dicom_files, desc="Converting DICOM to JPG"):
        try:
            ds = pydicom.dcmread(dcm_file)
            img = ds.pixel_array.astype(np.float32)

            # Normalize to 0-255 for image saving
            img = (img - np.min(img)) / (np.max(img) - np.min(img) + 1e-5) * 255.0  # add epsilon to avoid division by zero
            img = img.astype(np.uint8)

            # Resize if target_size provided
            if target_size is not None:
                img = cv2.resize(img, target_size)

            # Generate output filename
            base_filename = os.path.basename(dcm_file).replace('.dcm', '.jpg')
            output_filename = f"{subfolder}_{base_filename}"
            output_path = os.path.join(output_folder, output_filename)

            # Save as JPG
            cv2.imwrite(output_path, img)
        except Exception as e:
            print(f"Error processing {dcm_file}: {e}")

# Your paths:
root_ct_folder = "/Users/geraldalanraja/Desktop/NIT Trichy/Synthetic CT Generation/Datasets/CHAOS/CHAOS_Train_Sets/Train_Sets/CT"
output_folder = "/Users/geraldalanraja/Desktop/NIT Trichy/Synthetic CT Generation/Datasets/CHAOS_Processed/Train"

# Call the function:
# Set target_size=(128, 128) if you want resizing
convert_dicom_to_jpg(root_ct_folder, output_folder, target_size=None)
