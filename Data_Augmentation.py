import torch
from torchvision import transforms
from torchvision.transforms import functional as F
import numpy as np
import cv2
from PIL import Image, ImageFilter
import os

# 定義資料擴增操作
transform = transforms.Compose([
    transforms.RandomRotation(20),
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(brightness=0.5, contrast=0.1, saturation=0.1, hue=0.05),
])

# 設定原始圖片目錄和保存目錄
original_images_dir = r'C:\Users\yahfou\Desktop\ardiuno_image'
save_dir = r'C:\Users\yahfou\Desktop\ardiuno_data'

option = int(input('訓練或驗證集? (訓練集:1，驗證集:2):'))


def normal(original_images_dir):
    image_files = [f for f in os.listdir(original_images_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
    total_generated_images = 0
    for image_file in image_files:
    
        original_image_path = os.path.join(original_images_dir, image_file)
        img = Image.open(original_image_path)
        
        if option == 1:
            
            o_save_path = os.path.join(save_dir, f'{image_file}')
            img.save(o_save_path)
        
        num_generated_images = 0
        
        while num_generated_images < desired_total_generated_images:
            
            augmented_img = transform(img)
            
            save_path = os.path.join(save_dir, f'arduino_augmented_{total_generated_images}.jpg')
            augmented_img.save(save_path)
            
            # 增加生成的總圖片數量和每張原始圖片生成的擴增後的圖片數量
            total_generated_images += 1
            num_generated_images += 1
    
            if total_generated_images >= desired_total_generated_images:    # 檢查是否達到期望的生成總數量
                break

            
def blur(save_dir):
    
    # 高斯模糊sigma
    sigma_min = 2 
    sigma_max = 5
    
    for filename in os.listdir(save_dir):

        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):

            img_path = os.path.join(save_dir, filename)
            img = Image.open(img_path)
            

            sigma = np.random.uniform(sigma_min, sigma_max)
            augmented_img = img.filter(ImageFilter.GaussianBlur(radius=sigma))
            
            save_path = os.path.join(save_dir, f'{os.path.splitext(filename)[0]}_blurred.jpg')
            augmented_img.save(save_path)


            

if option == 1:
    desired_total_generated_images = 147 # 控制生成的圖片數量
    normal(original_images_dir)
    blur(save_dir)
    
elif option == 2:
    desired_total_generated_images = 12 # 控制生成的圖片數量
    normal(original_images_dir)
    blur(save_dir)
    
else:
    print('錯誤')
