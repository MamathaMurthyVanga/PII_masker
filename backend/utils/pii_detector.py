

import re

def detect_pii(text):
    raw = text.upper()
    normalized = normalize_for_pii(raw)

    pii_patterns = {
        "aadhaar": r"\b\d{4}\s?\d{4}\s?\d{4}\b",
        "dob": r"\b\d{2}/\d{2}/\d{4}\b",
        "phone": r"\b\d{10}\b",
        "email": r"[A-Z0-9_.+-]+@[A-Z0-9-]+\.[A-Z0-9-.]+",
        # Allow 1/I in final character and digit-letter mix in middle
        "pan_strict": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",          
        "pan_fuzzy": r"\b[A-Z1]{5}[0-9]{4}[A-Z1]\b"
        
    }

    for label, pattern in pii_patterns.items():
        if label.startswith("pan"):
            if re.search(pattern, normalized):
                print(f"Detected {label} PII: {raw}")
                return True
        else:
            if re.search(pattern, raw):
                print(f"Detected {label} PII: {raw}")
                return True
    return False


def normalize_for_pii(text):
    """Light normalization to account for OCR confusion while keeping structure."""
    return (
        text.replace('I', '1')
            .replace('L', '1')
            .replace('O', '0')
            .replace('Q', '0')
    )
