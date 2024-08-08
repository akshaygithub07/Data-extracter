import os
import pymupdf

# Define the folder containing PDFs
pdf_folder = "Access To Justice"  # Replace with your actual folder path

# Define the output folder
output_folder = "Output"  # Replace with your desired output path

# Loop through all files in the PDF folder
for filename in os.listdir(pdf_folder):
  # Check if it's a PDF file
  if filename.endswith(".pdf"):
    # Create full path for the input PDF
    input_path = os.path.join(pdf_folder, filename)

    # Create full path for the output PDF (modified)
    output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + "_modified.pdf")

    try:
      # Open the PDF document
      doc = pymupdf.open(input_path)

      # Delete page range (adjust as needed)
      doc.delete_pages(from_page=0, to_page=1)

      # Save the modified document
      doc.save(output_path)

      print(f"Successfully processed: {filename}")
    except Exception as e:
      print(f"Error processing {filename}: {e}")

print("Finished processing all PDFs.")











