import PyPDF2
import os
import argparse
import sys

# Create the argument parser
parser = argparse.ArgumentParser(description='Merge multiple PDF files into one.')
parser.add_argument('input_files', metavar='input_file', nargs='+',
                    help='input PDF files to merge')
parser.add_argument('-o', '--output', dest='output_file', default='merged.pdf',
                    help='output file name (default: merged.pdf)')

# Parse the command-line arguments
args = parser.parse_args()

# Get the input PDF files
input_files = args.input_files

# Prompt user for output file name
output_file = args.output_file

# Create a new PDF merger object
pdf_merger = PyPDF2.PdfMerger()

# Merge the input PDF files
for input_file in input_files:
    # Open each PDF file
    with open(input_file, 'rb') as pdf_file:
        # Add the PDF to the merger object
        pdf_merger.append(pdf_file)

# Create the output directory if it doesn't exist
if not os.path.exists("output"):
    os.makedirs("output")

# Save the merged PDF to the output directory
output_path = os.path.join("output", output_file)
with open(output_path, 'wb') as output_file:
    pdf_merger.write(output_file)

# Open the merged PDF with the default PDF viewer
if sys.platform.startswith('darwin'):
    os.system(f'open "{output_path}"')
elif os.name == 'nt':
    os.system(f'start "" "{output_path}"')
elif os.name == 'posix':
    os.system(f'xdg-open "{output_path}"')
