# PDF Image Extractor

This Python script extracts images from a PDF file and saves them in a specified output folder. It uses the `PyPDF2` library for reading the PDF and `Pillow` (PIL) for handling image processing.

## Features

- Extracts images from each page of a PDF.
- Supports common image formats: **JPG**, **PNG**, **JP2**.
- Automatically creates an output folder if it does not exist.
- Saves images with descriptive filenames indicating the page and image number.

## Prerequisites

- Python 3.x
- `PyPDF2` library
- `Pillow` library (PIL)

## Installation

Install the required libraries using pip:

```bash
pip install PyPDF2 Pillow
```

- pdf_file_path = 'example.pdf' # Replace with your PDF file path
- output_dir = 'extracted_images' # Replace with desired output folder

Run the script:

```bash
python image_extractor.py
```

Extracted images will be saved in the specified output folder.

## Code Explanation

Notes

- Images with unknown filter types are saved with a .bin extension.
- Ensure your PDF has extractable images; some PDFs store images in non-standard formats or as vector graphics.

## Limitations

-- This script does not handle vector graphics or complex PDF structures with nested object references beyond standard /XObject usage.

## License

This project is available under the MIT License.
