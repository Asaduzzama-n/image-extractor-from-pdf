# image-extractor-from-pdf

This Python script extracts images from a PDF file and saves them in a specified output folder. It uses PyPDF2 for reading the PDF and PIL (Pillow) for handling image processing.

Features
Extracts images from each page of a PDF.
Supports common image formats (jpg, png, jp2).
Automatically creates an output folder if it does not exist.
Saves images with descriptive filenames indicating the page and image number.
Prerequisites
Python 3.x
PyPDF2 library
Pillow library (PIL)
Installation
Install the required libraries:

bash
Copy code
pip install PyPDF2 Pillow
Clone or copy the script into your project directory.

Usage
Update the file path and output directory in the example usage section:

python
Copy code
pdf_file_path = 'example.pdf' # Replace with your PDF file path
output_dir = 'extracted_images' # Replace with desired output folder
Run the script:

bash
Copy code
python image_extractor.py
Extracted images will be saved in the specified output folder.

Code Explanation
PDF Reading: Uses PyPDF2.PdfReader to load the PDF file.
Image Extraction: Iterates over pages and extracts images if /XObject resources are present.
Image Format Handling: Detects image type based on filters (/DCTDecode for JPG, /FlateDecode for PNG, /JPXDecode for JP2).
File Saving: Saves images with names like page_1_image_1.jpg.
Example Output
If the script processes a PDF with two pages containing one image each:

arduino
Copy code
Saved image: extracted_images/page_1_image_1.jpg
Saved image: extracted_images/page_2_image_1.png
Notes
Images with unknown filter types are saved with a .bin extension.
Ensure your PDF has extractable images; some PDFs store images in non-standard formats or as vector graphics.
Limitations
This script does not handle vector graphics or complex PDF structures with nested object references beyond standard /XObject usage.
License
This project is available under the MIT License.
