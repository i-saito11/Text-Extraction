import os
import subprocess
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

def convert_pdf_to_tei(input_folder, output_folder):
    # Call the script to convert PDF to TEI XML
    subprocess.run(["python", "pdfgrobidcall.py", input_folder, output_folder])

def count_figures(tei_xml_file):
    tree = ET.parse(tei_xml_file)
    root = tree.getroot()

    figure_count = 0
    for figure in root.findall(".//{http://www.tei-c.org/ns/1.0}figure"):
        figure_count += 1

    return figure_count

def visualize_figure_counts(output_folder):
    figure_counts = {}
    for filename in os.listdir(output_folder):
        if filename.endswith(".grobid.tei.xml"):
            tei_xml_file = os.path.join(output_folder, filename)
            print(f"Processing TEI XML file: {tei_xml_file}")
            figure_count = count_figures(tei_xml_file)
            figure_counts[filename] = figure_count
    
    # Plot the figure counts
    plt.bar(figure_counts.keys(), figure_counts.values())
    plt.xlabel("TEI XML File")
    plt.ylabel("Number of Figures")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Prompt the user to enter the input folder path
    input_folder = input("Enter the input folder path containing raw PDFs: ")

    # Prompt the user to enter the output folder path
    output_folder = input("Enter the output folder path to save TEI XML files: ")

    # Convert PDFs to TEI XML
    convert_pdf_to_tei(input_folder, output_folder)
    
    # Generate and display figure counts
    visualize_figure_counts(output_folder)
