import os
import PdfDownloader
import kodscraper
import process_pdf

# Get the current working directory
current_directory = os.getcwd()

# Step 1: Take the PDF URL as input
pdf_url = input("Enter the URL of the PDF: ")

# Step 2: Download the PDF
pdf_file_path = PdfDownloader.pdf_downloader(pdf_url, current_directory)

if pdf_file_path:
    # Step 3: Scrape contents from the URL
    lines = kodscraper.scrape_contents_from_url('https://www.kap.org.tr/tr/bist-sirketler')

    # Step 4: Process the PDF and get the result dictionary
    result_dict = process_pdf.process_pdf_tables(pdf_file_path)

    # Step 5: Print the resulting dictionary
    for key, value in result_dict.items():
        # Convert the float value to a string with 2 decimal places and add a percentage sign
        value_str = f"{value:.2f}%"
        print(f"{key}: {value_str}")

    print(len(result_dict.items()))
else:
    print("PDF download failed.")

