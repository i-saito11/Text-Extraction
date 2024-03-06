import os
import subprocess
import re
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

def convert_pdf_to_tei(input_folder, output_folder):
    # Call the script to convert PDF to TEI XML
    subprocess.run(["python", "pdfgrobidcall.py", input_folder, output_folder])

def extract_links_from_xml(element):
    # Extract links from the attributes of the element
    links = []
    for key, value in element.items():
        if key == "target":
            links.append(value)
    
    # Extract links from the text content of the element
    if element.text:
        links.extend(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', element.text))
    
    # Recursively extract links from child elements
    for child in element:
        links.extend(extract_links_from_xml(child))
    
    return links

def find_links_in_tei_xml(tei_xml_file):
    # Parse TEI XML
    tree = ET.parse(tei_xml_file)
    root = tree.getroot()

    # Extract links from the TEI XML
    links = extract_links_from_xml(root)

    return links

def main(input_folder, output_folder):
    # Convert PDFs to TEI XML
    convert_pdf_to_tei(input_folder, output_folder)

    # Process TEI XML files and extract links
    for filename in os.listdir(output_folder):
        if filename.endswith(".grobid.tei.xml"):
            file_path = os.path.join(output_folder, filename)
            print(f"Processing TEI XML file: {file_path}")

            # Find links in TEI XML
            links = find_links_in_tei_xml(file_path)

            # Filter out unwanted links
            filtered_links = []
            for link in links:
                parsed_url = urlparse(link)
                if parsed_url.scheme and parsed_url.netloc:  # Check if the link is a valid URL
                    if not (parsed_url.netloc.endswith("github.com") or parsed_url.netloc.endswith("grobid")):
                        filtered_links.append(link)

            # Print links
            print(f"Links found in {filename}:")
            for link in filtered_links:
                print(link)

if __name__ == "__main__":
    # Prompt the user to enter the input folder path
    input_folder = input("Enter the input folder path containing raw PDFs: ")

    # Prompt the user to enter the output folder path
    output_folder = input("Enter the output folder path to save the TEI XML files: ")

    # Process TEI XML files and extract links
    main(input_folder, output_folder)
