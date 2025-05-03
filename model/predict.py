# model/predict.py

import cv2
import numpy as np
import os

def preprocess_and_predict(img_path):
    image = cv2.imread(img_path)
    if image is None:
        return "Invalid Image", None, None

    filename = os.path.basename(img_path)
    result_img_path = os.path.join("static", "uploads", f"result_{filename}")

    image = cv2.resize(image, (256, 256))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)

    contours, _ = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    damage_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 500]

    output_image = image.copy()
    cv2.drawContours(output_image, damage_contours, -1, (0, 0, 255), 2)
    cv2.imwrite(result_img_path, output_image)

    if len(damage_contours) > 0:
        # Dummy logic for classification based on contour area (replace with your ML model)
        total_area = sum([cv2.contourArea(c) for c in damage_contours])
        if total_area < 1500:
            damage_type = "Scratch"
        elif total_area < 4000:
            damage_type = "Dent"
        else:
            damage_type = "Debris"
        return f"Damage Detected ({len(damage_contours)} region(s))", result_img_path, damage_type
    else:
        return "No Damage Found", result_img_path, "None"
