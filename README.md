# EasyOCR Text Extractor

This is a simple Python script that extracts text from images using the `easyocr` library. It's ideal for converting screenshots, scanned documents, or any image with readable text into plain text.

## 🔧 Requirements

- Python 3.7 or higher
- `easyocr`
- `torch` (automatically installed with `easyocr`)
- Compatible with Windows, macOS, and Linux

## 📦 Installation

1. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
# OR
source venv/bin/activate # On Mac/Linux

## Install dependencies
pip install easyocr

## How to Use
Replace the image path in the script:
image_path = r"C:\Users\Admin\OneDrive\Pictures\Screenshots\1.png"

## Run the script:
python ocr_script.py
