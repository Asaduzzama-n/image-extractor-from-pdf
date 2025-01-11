import os
from PyPDF2 import PdfReader
from PIL import Image

def extract_images_from_pdf(pdf_path, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the PDF
    reader = PdfReader(pdf_path)

    image_count = 0
    for page_number, page in enumerate(reader.pages, start=1):
        # Check if the page contains images
        if '/XObject' in page['/Resources']:
            xObject = page['/Resources']['/XObject'].get_object()
            for obj_name in xObject:
                obj = xObject[obj_name]
                if obj['/Subtype'] == '/Image':
                    size = (obj['/Width'], obj['/Height'])
                    data = obj._data  # Extract image data

                    # Determine image mode
                    if obj['/ColorSpace'] == '/DeviceRGB':
                        mode = "RGB"
                    else:
                        mode = "P"

                    # Process the image based on the filter type
                    if obj['/Filter'] == '/DCTDecode':
                        image_ext = "jpg"
                    elif obj['/Filter'] == '/FlateDecode':
                        image_ext = "png"
                    elif obj['/Filter'] == '/JPXDecode':
                        image_ext = "jp2"
                    else:
                        image_ext = "bin"  # Unknown filter type

                    # Save the image
                    image_filename = f"page_{page_number}_image_{image_count + 1}.{image_ext}"
                    image_path = os.path.join(output_folder, image_filename)

                    with open(image_path, "wb") as image_file:
                        image_file.write(data)

                    print(f"Saved image: {image_path}")
                    image_count += 1

    if image_count == 0:
        print("No images found in the PDF.")
    else:
        print(f"Extracted {image_count} images from the PDF.")

# Example usage
pdf_file_path = 'Salongoicons.pdf'  # Replace with your PDF file path
output_dir = 'extracted_images'  # Replace with desired output folder
extract_images_from_pdf(pdf_file_path, output_dir)
