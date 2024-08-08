
import os


# Define the folder containing PDFs
text_folder = "Converted Text"  # Replace with your actual folder path

# Define the output folder
output_folder = "Flowchart removed"  # Replace with your desired output path

# Loop through all files in the PDF folder
for filename in os.listdir(text_folder):
  # Check if it's a PDF file
  if filename.endswith(".txt"):
    # Create full path for the input PDF
    input_path = os.path.join(text_folder, filename)

    # Create full path for the output PDF (modified)
    output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + "_removed.txt")

    try:
      # Open the PDF document
      with open(input_path, 'r') as f_in, open(output_path, 'w') as f_out:
        for line in f_in:
          words = line.split()
          if len(words) > 1:
            f_out.write(line)

      print(f"Successfully removed: {filename}")
    except Exception as e:
      print(f"Error processing {filename}: {e}")

print("Finished processing all texts.")