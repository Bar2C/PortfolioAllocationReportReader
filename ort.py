import os
import PdfDownloader
import kodscraper
import process_pdf
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

def process_pdf_and_print_result():
    pdf_url = url_entry.get()
    pdf_file_path = PdfDownloader.pdf_downloader(pdf_url, "pdffiles")

    if pdf_file_path:
        lines = kodscraper.scrape_contents_from_url('https://www.kap.org.tr/tr/bist-sirketler')
        result_dict = process_pdf.process_pdf_tables(pdf_file_path)

        # Clear the result text box before printing the new result
        result_text.delete("1.0", tk.END)
        # Create the pie chart data
        labels = []
        sizes = []


        for key, value in result_dict.items():
            # Convert the float value to a string with 2 decimal places and add a percentage sign
            value_str = f"{value:.2f}%"
            result_text.insert(tk.END, f"{key}: {value_str}\n")
            # Add the data to the pie chart
            labels.append(key)
            sizes.append(value)

        # Create and display the pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title("Result")
        plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

        status_label.config(text=f"Total {len(result_dict.items())} items found.")

        # Set the height of the text widget to fit all the lines
        num_lines = len(result_dict)
        result_text.config(height=num_lines + 1)

    else:
        status_label.config(text="PDF download failed.")

def browse_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        lines = kodscraper.scrape_contents_from_url('https://www.kap.org.tr/tr/bist-sirketler')
        result_dict = process_pdf.process_pdf_tables(file_path)

        # Clear the result text box before printing the new result
        result_text.delete("1.0", tk.END)

        for key, value in result_dict.items():
            # Convert the float value to a string with 2 decimal places and add a percentage sign
            value_str = f"{value:.2f}%"
            result_text.insert(tk.END, f"{key}: {value_str}\n")

        status_label.config(text=f"Total {len(result_dict.items())} items found.")

        # Set the height of the text widget to fit all the lines
        num_lines = len(result_dict)
        result_text.config(height=num_lines + 1)

    else:
        status_label.config(text="PDF file not selected.")

# Create the main window
root = tk.Tk()
root.title("PDF Processor")

# Set the window size
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

# Create input elements
url_label = tk.Label(root, text="Enter the URL of the PDF:")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.pack()

download_button = tk.Button(root, text="Download PDF and Process", command=process_pdf_and_print_result)
download_button.pack()

browse_button = tk.Button(root, text="Browse PDF and Process", command=browse_pdf)
browse_button.pack()

# Create output elements
result_text = tk.Text(root, height=20, width=70)
result_text.pack()

status_label = tk.Label(root, text="")
status_label.pack()

# Automatically adjust the view to the end of the text
result_text.yview(tk.END)

# Start the main event loop
root.mainloop()
