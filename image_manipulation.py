import cv2
import numpy as np
import random

def add_shadow(frame):
    shadow_mask = np.zeros_like(frame)
    x1, y1 = random.randint(0, frame.shape[1] // 2), random.randint(0, frame.shape[0] // 2)
    x2, y2 = x1 + random.randint(100, 200), y1 + random.randint(50, 150)
    cv2.rectangle(shadow_mask, (x1, y1), (x2, y2), (0, 0, 0), -1)
    shadow_intensity = random.uniform(0.3, 0.7)
    frame = cv2.addWeighted(frame, 1.0, shadow_mask, shadow_intensity, 0)
    return frame

def apply_color_overlay(frame):
    overlay_color = np.random.randint(0, 256, 3)
    overlay = np.ones_like(frame, dtype=np.uint8)
    overlay[:] = overlay_color
    alpha = random.uniform(0.2, 0.5)
    frame = cv2.addWeighted(frame, 1 - alpha, overlay, alpha, 0)
    return frame

def rotate_image(frame):
    (h, w) = frame.shape[:2]
    center = (w // 2, h // 2)
    angle = random.uniform(-10, 10)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_frame = cv2.warpAffine(frame, M, (w, h))
    return rotated_frame

def adjust_brightness(frame):
    brightness_factor = random.uniform(0.5, 1.5)  # Random brightness factor
    return cv2.convertScaleAbs(frame, alpha=brightness_factor, beta=0)
