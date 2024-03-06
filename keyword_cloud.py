import os
import subprocess
from collections import Counter
from wordcloud import WordCloud
import xml.etree.ElementTree as ET
import sys
import matplotlib.pyplot as plt

def convert_pdf_to_tei(input_folder, output_folder):
    # Call the script to convert PDF to TEI XML
    subprocess.run(["python", "pdfgrobidcall.py", input_folder, output_folder])

def parse_tei_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    abstracts = []
    for abstract_elem in root.findall(".//{http://www.tei-c.org/ns/1.0}abstract"):
        abstract_text = ""
        for p_elem in abstract_elem.findall(".//{http://www.tei-c.org/ns/1.0}p"):
            abstract_text += p_elem.text.strip() + " "
        abstracts.append(abstract_text.strip())

    return abstracts

def extract_keywords(text):
    # Perform text preprocessing and extract keywords
    # This can include steps like tokenization, removing stop words, etc.
    # For simplicity, we'll use a basic approach here
    words = text.lower().split()  # Split text into words
    # Count word frequencies
    word_freq = Counter(words)
    # Filter out common words (e.g., stop words)
    stop_words = set(["the", "and", "of", "in", "a"])  # Example stop words
    word_freq = {word: freq for word, freq in word_freq.items() if word not in stop_words}
    return word_freq

def generate_keyword_cloud(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".grobid.tei.xml"):
            file_path = os.path.join(input_folder, filename)
            print(f"Processing TEI XML file: {file_path}")
            abstracts = parse_tei_xml(file_path)
            print(f"Abstracts found: {abstracts}")
            for idx, abstract in enumerate(abstracts):
                if abstract:  # Check if the abstract is not empty
                    word_freq = extract_keywords(abstract)
                    if word_freq:  # Check if word frequency dictionary is not empty
                        # Generate word cloud
                        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
                        # Display word cloud
                        plt.imshow(wordcloud, interpolation='bilinear')
                        plt.axis("off")
                        plt.show()

if __name__ == "__main__":
    # Prompt the user to enter the input folder path
    input_folder = input("Enter the input folder path containing raw PDFs: ")

    # Prompt the user to enter the output folder path
    output_folder = input("Enter the output folder path for TEI XML files: ")

    # Convert PDFs to TEI XML
    convert_pdf_to_tei(input_folder, output_folder)
    
    # Generate and display keyword clouds
    generate_keyword_cloud(output_folder, output_folder)
