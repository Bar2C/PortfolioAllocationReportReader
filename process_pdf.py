import tabula
import bar2_utilities as util

def process_pdf_tables(pdf_path):
    # Call the function to get the lines list from the get_kodfinal function in bar2_utilities.py
    lines = util.get_kodfinal()

    # Use the `read_pdf` function to extract tables from the PDF with the `guess` option
    page_width_cm, page_height_cm = util.get_page_sizes(pdf_path)


    # Conversion factor from centimeters to points


    # Distance of the table from the page edges (in centimeters)
    distance_from_top_cm = 0
    distance_from_left_cm = 0
    distance_from_bottom_cm = 0
    distance_from_right_cm = 0

    # Calculate the coordinates in points
    top = distance_from_top_cm
    left = distance_from_left_cm
    bottom = (page_height_cm - distance_from_bottom_cm)
    right = (page_width_cm - distance_from_right_cm)


    # Define the area coordinates
    area_coordinates = [top, left, bottom, right]



    tables = tabula.read_pdf(pdf_path, guess=False, pages='all', pandas_options={'header': None}, area=area_coordinates)



    # Initialize an empty dictionary to store the results
    result_dict = {}
    last_added = None
    last_added_to_dict = "A"

    # Iterate through the tables and access the table data
    for df in tables:
        # Check if the table has at least two columns
        if df.shape[1] >= 2:
            # Iterate through the rows of the table
            for index, row in df.iterrows():
                first_column_value = row.iloc[0]
                #print(first_column_value)
                first_column_value = util.manipulate_first_column(first_column_value)
                last_column_value = row.iloc[-1]
                #print(last_column_value)

                last_column_value = util.manipulate_last_column(last_column_value)

                #print(first_column_value, last_column_value)

                # Check if the first column value is in the lines list
                if first_column_value in lines and first_column_value >= last_added_to_dict :
                    print(first_column_value, last_column_value)

                    # If the key already exists in the dictionary, add the last column value to the existing value
                    if first_column_value in result_dict:
                        if last_added == first_column_value and last_column_value <10:
                            result_dict[first_column_value] += last_column_value
                            #print(first_column_value, last_column_value)
                            last_added = first_column_value
                    # If the key does not exist, create a new entry in the dictionary
                    elif last_column_value < 11:
                        result_dict[first_column_value] = last_column_value
                        last_added = first_column_value
                        last_added_to_dict = first_column_value
                        #print(first_column_value, last_column_value,"yeni")
                elif  first_column_value in lines:
                    last_added = first_column_value



    # Remove keys with values equal to 0
    result_dict = {k: v for k, v in result_dict.items() if v != 0.00}
    sum = 0
    for key, value in result_dict.items():
        sum += value
    print(sum)


    return result_dict

# Specify the path to the PDF file
#pdf_path = "YDI.pdf"

# Call the function and get the result
#result_dict = process_pdf_tables("TZD.pdf")

# Print the resulting dictionary
#for key, value in result_dict.items():
    #print(f"{key}: {value}")


