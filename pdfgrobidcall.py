#This script needs 2 arguments, the "input" folder in which you would need to have the pdfs you wish to have them converted to TEI XML
#And the second argument is the "output" folder in which you would wish to have those TEI XML dumped in
import subprocess
import os
import sys

def find_config_file():
    # Get the directory of the current script file
    script_directory = os.path.dirname(os.path.realpath(__file__))
    
    # Specify the relative path to the folder containing config.json
    config_folder = os.path.join(script_directory, ".\grobid_client_python")
    
    # Check if config.json exists in the specified folder
    config_path = os.path.join(config_folder, 'config.json')
    if os.path.exists(config_path):
        return config_path
    else:
        print("Error: config.json file not found.")
        return None

def run_grobid_client(input_folder, output_folder):
    # Find the path to config.json file
    config_path = find_config_file()

    if config_path is None:
        return

    # Run grobid_client script with input, output, and config file arguments
    subprocess.run(["grobid_client", "--input", input_folder, "--output", output_folder, "--config", config_path, "processFulltextDocument"])

if __name__ == "__main__":
    # Check if both input and output folder paths are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python pdfgrobidcall.py <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    # Run the grobid_client script
    run_grobid_client(input_folder, output_folder)
