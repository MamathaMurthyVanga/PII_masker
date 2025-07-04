import easyocr

reader = easyocr.Reader(['en'], gpu=False)

def extract_text_with_boxes(image_path):
    results = reader.readtext(image_path)
  
    return results  # Each item: (bbox, text, confidence)
