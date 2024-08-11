import re

# Path to your input file
input_file_path = 'try_cleaned_Handbook on Legal System & Procedure_removed.txt'

# Path to save the output file
output_file_path = 'output_file_newestnew.txt'

# Read the content from the input file
with open(input_file_path, 'r') as file:
    content = file.read()

patterna = r'(\d),'

# Replace the comma with a period
content_with_periods = re.sub(patterna, r'\1.', content)


patternb = r'\.\s+(\d)'

# Replace the space with nothing (i.e., remove it)
content_without_space = re.sub(patternb, r'.\1', content_with_periods)

# Regular expression pattern to match numbers like 1.1, 2.1, 1.1.1, 2.1.1, etc.
patternc = r'(\n)(\d+\.\d+(\.\d+)?)'

# Replace the pattern with a blank line before the matched number
content_with_blank_lines = re.sub(patternc, r'\1\n\2', content_without_space)

patterne = r'[-~]'

# Replace the comma with a period
content_without_hyphens = re.sub(patterne, r'', content_with_blank_lines)


# Write the modified content to the output file
with open(output_file_path, 'w') as file:


    file.write(content_without_hyphens)

print(f"Processed content saved to {output_file_path}")
