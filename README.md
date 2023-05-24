# Text-Detect-from-Image

The Python-tesseract library provides a convenient interface to interact with the Tesseract-OCR Engine in Python. It allows you to extract text from images by leveraging the powerful OCR capabilities of Tesseract.

# Installment procedure of Python-tesseract 

To install the pytesseract please follow the following link
```sh
https://github.com/UB-Mannheim/tesseract/wiki
```

# Error
The following error can be arised:

```sh
Pytesseract : "TesseractNotFound Error: tesseract is not installed or it's not in your path"
```

# Error solve

If you face the above-mentioned problem. please follow the below: 

1. At first Download the Python-tesseract from the  [Link](https://github.com/UB-Mannheim/tesseract/wiki) and install it manually as like other software. 

2. Then,copy the installment path which means the Python-tesseract installation path, and replace the path in main.py

pytesseract.pytesseract.tesseract_cmd = r'path'

Example:

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

here ":\Program Files\Tesseract-OCR\tesseract.exe" this is my installation path.

# Runnning this file
Use the below commond to execute the python file:-

```sh
python main.py
```


