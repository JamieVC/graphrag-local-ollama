import os
import PyPDF2

def convert_folder_pdfs_to_txts(pdf_folder, txt_folder):
    """
    Converts all PDF files in a specified folder to TXT files,
    and saves them into a separate folder.

    Args:
        pdf_folder (str): Path to the folder containing PDF files.
        txt_folder (str): Path to the folder where TXT files will be saved.

    """
    # Ensure the output folder exists
    os.makedirs(txt_folder, exist_ok=True)
    
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, filename)
            txt_path = os.path.join(txt_folder, os.path.splitext(filename)[0] + '.txt')
            
            try:
                convert_pdf_to_txt(pdf_path, txt_path)
                print(f"Converted {filename}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

def convert_pdf_to_txt(pdf_path, txt_path):
    """
    Converts a single PDF file to a TXT file.

    Args:
        pdf_path (str): Path to the input PDF file.
        txt_path (str): Path to the output TXT file.

    """
    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            if reader.is_encrypted:
                print(f"Skipping encrypted file: {pdf_path}")
                return
            
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)
    except PyPDF2.errors.PdfReadError as e:
        print(f"Could not read {pdf_path}: {e}")

if __name__ == "__main__":
    # Specify the folders for PDFs and TXT files
    pdf_folder_path = './ragtest_npu/input/pdfs'
    txt_folder_path = './ragtest_npu/input'
    
    # Ensure the PDF folder exists
    if not os.path.isdir(pdf_folder_path):
        print(f"PDF folder does not exist: {pdf_folder_path}")
    else:
        convert_folder_pdfs_to_txts(pdf_folder_path, txt_folder_path)
        print("All possible PDFs have been converted.")