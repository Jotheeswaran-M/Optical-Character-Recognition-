import easyocr

def extract_text_with_easyocr(image_path):
    reader = easyocr.Reader(['en'])  # You can add more languages, e.g., ['en', 'fr']
    results = reader.readtext(image_path)

    extracted_text = ""
    for detection in results:
        text = detection[1]
        extracted_text += text + "\n"

    return extracted_text

if __name__ == "__main__":
    image_path = r"C:\Users\Admin\OneDrive\Pictures\Screenshots\1.png"
    text = extract_text_with_easyocr(image_path)
    print("\nExtracted Text:\n")
    print(text)
