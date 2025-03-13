import os
import numpy as np
from PIL import Image

# Parameters
num_images = 50          # Har class ke liye images ki sankhya
img_height, img_width = 128, 128

# Directories create karein
os.makedirs('dataset/Fast', exist_ok=True)
os.makedirs('dataset/Delayed', exist_ok=True)

for i in range(num_images):
    # "Fast" class ke liye: yahan hum thoda green dominant images banayenge
    fast_image = np.zeros((img_height, img_width, 3), dtype=np.uint8)
    # Green channel ko high random values dein
    fast_image[..., 1] = np.random.randint(100, 256, (img_height, img_width))
    # Baaki channels ko thoda low random values dein
    fast_image[..., 0] = np.random.randint(0, 100, (img_height, img_width))
    fast_image[..., 2] = np.random.randint(0, 100, (img_height, img_width))
    img_fast = Image.fromarray(fast_image)
    img_fast.save(f'dataset/Fast/fast_{i+1}.jpg')
    
    # "Delayed" class ke liye: yahan hum red dominant images banayenge
    delayed_image = np.zeros((img_height, img_width, 3), dtype=np.uint8)
    # Red channel ko high random values dein
    delayed_image[..., 0] = np.random.randint(100, 256, (img_height, img_width))
    # Baaki channels ko thoda low random values dein
    delayed_image[..., 1] = np.random.randint(0, 100, (img_height, img_width))
    delayed_image[..., 2] = np.random.randint(0, 100, (img_height, img_width))
    img_delayed = Image.fromarray(delayed_image)
    img_delayed.save(f'dataset/Delayed/delayed_{i+1}.jpg')

print("Dummy dataset successfully created in the 'dataset' folder!")
