#This script needs 2 arguments, the "input" folder in which you would need to have the pdfs you wish to have them converted to TEI XML
#And the second argument is the "output" folder in which you would wish to have those TEI XML dumped in
import sys
from grobid_client.grobid_client import GrobidClient

def run_grobid_client(input_folder, output_folder):
    # Initialize Grobid client
    client = GrobidClient(config_path="./config.json")

    # Process full-text documents
    client.process("processFulltextDocument", input_folder, n=20, output=output_folder)

if __name__ == "__main__":
    # Check if both input and output folder paths are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python pdfgrobidcall.py <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    # Run the Grobid client
    run_grobid_client(input_folder, output_folder)
