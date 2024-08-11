import string


def remove_punctuation(input_file, output_file):


  with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
      for line in f_in:
          line = line.translate(str.maketrans('', '', string.punctuation))
          f_out.write(line.lower())

# Example usage:
input_file_path = 'output text.txt'
output_file_path = 'nextoutput.txt'
remove_punctuation(input_file_path, output_file_path)

print('Successful')