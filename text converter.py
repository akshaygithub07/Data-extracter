import os
import pymupdf


pdf_folder = "Output"  # Replace with your actual folder path

# Define the output folder
output_folder = "Converted Text"  # Replace with your desired output path

# Loop through all files in the PDF folder
for filename in os.listdir(pdf_folder):
    # Check if it's a PDF file
    if filename.endswith(".pdf"):
        # Create full path for the input PDF
        input_path = os.path.join(pdf_folder, filename)

        # Create full path for the output PDF (modified)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + "_converted.txt")

        try:
            # Open the PDF document
            doc = pymupdf.open(input_path)
            out = open(output_path, "wb")  # create a text output
            # Delete page range (adjust as needed)
            for page in doc:  # iterate the document pages
                text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
                out.write(text)  # write text of page
                out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
            out.close()

            print(f"Successfully converted: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")