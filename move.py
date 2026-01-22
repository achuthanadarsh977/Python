# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 19:46:30 2025

@author: User
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def translate_image(image, tx, ty):
    """
    Translates an image by tx pixels along the x-axis and ty pixels along the y-axis.
    """
    rows, cols = image.shape

    # Translation matrix (for shifting the image)
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

    # Apply affine transformation (translation)
    translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
    
    return translated_image

def move_silhouette(image, total_frames):
    """
    Animate the movement of the silhouette by applying translation.
    """
    rows, cols = image.shape
    video_frames = []
    
    # Define movement parameters
    dx = 5  # Translation on the x-axis per frame
    dy = 5  # Translation on the y-axis per frame
    
    for i in range(total_frames):
        # Translate the silhouette by dx and dy
        translated_image = translate_image(image, dx * i, dy * i)
        
        # Add the frame to the list
        video_frames.append(translated_image)
    
    # Combine frames into a video or display them one by one
    for frame in video_frames:
        cv2.imshow('Silhouette Movement', frame)
        cv2.waitKey(100)  # Wait for 100ms per frame
    
    cv2.destroyAllWindows()

# Example usage
image_path = r'C:\Users\User\Downloads\GaitDatasetB-silh\113\nm-06\180\113\nm-06\180\113-nm-06-180-102.png'  # Provide the path to your silhouette image
image = cv2.imread(image_path, 0)  # Load the silhouette image in grayscale
move_silhouette(image, 20)  # Animate for 20 frames




def show_image(image):
    plt.imshow(image, cmap='gray')
    plt.axis('off')  # Hide the axes for better visualization
    plt.show()

# Example usage in move_silhouette function:
for frame in video_frames:
    show_image(frame)
    plt.pause(0.1)  # Pause for 100ms between frames
