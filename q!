import cv2
import os
import time
import numpy as np
from image_manipulation import add_shadow, apply_color_overlay, adjust_brightness

# Create folder to save captured images
output_dir = "captured_images"
os.makedirs(output_dir, exist_ok=True)

# Initialize webcam
capt = cv2.VideoCapture(0)

if not capt.isOpened():
    print("Error: Cannot access webcam")
    exit()

# Set full screen preview window
cv2.namedWindow("Camera Preview with Frame", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Camera Preview with Frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

for i in range(101):
    ret, frame = capt.read()
    if not ret:
        print(f"Failed to capture image {i}")
        continue

    # Apply manipulations
    processed = adjust_brightness(frame)
    processed = add_shadow(processed)
    processed = apply_color_overlay(processed)

    # Add bright green border (20px)
    preview = cv2.copyMakeBorder(
        processed, 10, 10, 10, 10,
        borderType=cv2.BORDER_CONSTANT,
        value=[0, 0, 255]
    )

    # Show full-screen preview
    cv2.imshow("Camera Preview with Frame", preview)

    # Save processed image
    filename = os.path.join(output_dir, f"img_{i:03d}.jpg")
    cv2.imwrite(filename, processed)
    print(f"Saved {filename}")

    # Allow quitting early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.1)

# Release resources
capt.release()
cv2.destroyAllWindows()

# Final notification
cv2.namedWindow("Notification", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Notification", 500, 100)
cv2.imshow("Notification", cv2.putText(
    img = 255 * np.ones((100, 500, 3), dtype=np.uint8),
    text = "Done capturing images!",
    org = (50, 60),
    fontFace = cv2.FONT_HERSHEY_SIMPLEX,
    fontScale = 0.8,
    color = (0, 255, 0),
    thickness = 2
))
cv2.waitKey(3000)
cv2.destroyAllWindows()
