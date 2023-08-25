# Specify the path to the file
import PyPDF2

file_path = "kodfinal.txt"

# Open the file in read mode
with open(file_path, "r") as file:
    # Read all lines from the file and store them in a list
    lines = file.readlines()

# Remove leading and trailing whitespace from each line and create a list
lines = [line.strip() for line in lines]

# Print the list of lines


def get_kodfinal():
    return lines


def manipulate_first_column(first_column_value):
    if isinstance(first_column_value, str):
        words = first_column_value.split()
        if len(words) > 1:
            first_column_value = words[0]

        if first_column_value[-2:] == ".E":
            first_column_value = first_column_value[:-2]

    return first_column_value


def manipulate_last_column(last_column_value):
    if isinstance(last_column_value, str):
        # Split the last_column_value by whitespaces if it's splittable
        values = last_column_value.split() if last_column_value.strip() else None
        # If the value contains multiple values separated by whitespaces, take the last one
        last_column_value = values[-1] if values else last_column_value
        # Check if the value ends with a percentage sign (%)
        if last_column_value.endswith("%"):
            try:
                # Remove the percentage sign and replace any comma (,) with a dot (.)
                last_column_value = float(last_column_value[:-1].replace(",", "."))
            except ValueError:
                last_column_value = 0.0
        else:
            try:
                # Replace any comma (,) with a dot (.) and convert to float
                last_column_value = float(last_column_value.replace(",", "."))
            except ValueError:
                last_column_value = 0.0
    return last_column_value


def get_page_sizes(pdf_path):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize a list to store page sizes (width and height)
        # Loop through each page and get its size
        for page in pdf_reader.pages:
            page_width = float(page.mediabox.width)
            page_height = float(page.mediabox.height)

            return page_width, page_height
