 [![DOI](https://zenodo.org/badge/763659834.svg)](https://zenodo.org/doi/10.5281/zenodo.10790932)

# Text Extraction Project

This project focuses on extracting structured data from PDF files using the Grobid tool and Python scripts.

## Scripts

### keyword_cloud.py

This script generates a keyword cloud from the abstracts extracted from TEI XML files produced by Grobid.

### figures.py

This script counts the number of figures in TEI XML files generated by Grobid and visualizes the counts.

### links.py

This script extracts links from TEI XML files produced by Grobid and filters out unwanted links.

## Requirements

- Python 3.x
- Grobid (running instance, port 8070)
- [Grobid Client Python](https://github.com/kermitt2/grobid_client_python) library

## Usage

1. Install Python and Grobid.
2. Clone this repository: `git clone https://github.com/i-saito11/Text-Extraction.git`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the Python scripts:

```bash
python keyword_cloud.py
python figures.py
python links.py
```
5. Follow the prompts to provide input folder paths containing raw PDFs and output folder paths for TEI XML files

## Preferred Citation

If you use this project, please cite:
Iñigo Rodriguez Saito. Text Extraction Project.

## Input data

The input data for the scripts can be stored in any folder on your system. However, its preferred to use the provided 'input_pdfs' folder withing the project directory. 

## Output data

The output of the scripts will be generated in the same way the input works. 

## More Information

- [Grobid Documentation](https://grobid.readthedocs.io/en/latest/)
- [Grobid Client Python Documentation](https://github.com/kermitt2/grobid_client_python?tab=readme-ov-file#using-the-client-in-your-python)
- [DOAJ (Directory of Open Access Journals)](https://doaj.org) - A site for obtaining open access PDFs used in the project.


