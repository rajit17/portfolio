import os
from PIL import Image

# === CONFIGURATION ===
input_folder = "New folder"     # Folder containing cropped images
output_folder = "cropped images_compress"   # Folder to save compressed images
scale_factor = 0.5          # 50% compression (half width and height)
jpeg_quality = 85  # Added quality parameter for JPEG compression

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# === MAIN LOOP ===
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".tif", ".tiff", ".jpg", ".jpeg", ".png")):
        try:
            input_path = os.path.join(input_folder, filename)
            # Change output extension to jpg for better compatibility
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(output_folder, output_filename)

            # Open and convert image to RGB
            img = Image.open(input_path)
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')

            # Compute new size
            w, h = img.size
            new_size = (int(w * scale_factor), int(h * scale_factor))

            # Resize with high-quality downsampling (LANCZOS)
            img_resized = img.resize(new_size, Image.LANCZOS)

            # Save compressed image as JPEG
            img_resized.save(output_path, 'JPEG', quality=jpeg_quality)

            print(f"✔ Compressed and saved: {output_path}")
            
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

print("\n✅ All images compressed successfully and saved in 'cropped images_compress' folder.")
