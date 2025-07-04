
import cv2

def mask_pii_on_image(image_path, ocr_results, pii_detector):
    image = cv2.imread(image_path)



    for (bbox, text, _) in ocr_results:
        print(f"OCR text: '{text}'") 
        if pii_detector(text):
            pts = [(int(x), int(y)) for x, y in bbox]
            x1 = min(pt[0] for pt in pts)
            y1 = min(pt[1] for pt in pts)
            x2 = max(pt[0] for pt in pts)
            y2 = max(pt[1] for pt in pts)

            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 0), -1)


    masked_path = image_path.replace(".", "_masked.")
    cv2.imwrite(masked_path, image)
    return masked_path
