import os
import fitz  # PyMuPDF library
import sys

# Function to merge PDFs in a folder
def merge_pdfs_in_folder(folder_path, output_path):
    pdf_writer = fitz.open()

    # Loop through all PDF files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            pdf_document = fitz.open(pdf_path)
            pdf_writer.insert_pdf(pdf_document)

    # Save the merged PDF to the output file
    pdf_writer.save(output_path)
    pdf_writer.close()

# Specify the folder containing the PDFs and the output path
input_folder = sys.argv[1]
folder_name = os.path.basename(input_folder)
filename = folder_name + ".pdf"
output_path = os.path.join(input_folder,filename)

# Call the merge function
merge_pdfs_in_folder(input_folder, output_path)

print('PDFs merged successfully.')