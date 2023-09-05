import openpyxl

# Initialize an empty list to store the column data
column_data = []

def readData():
    # Open the Excel file
    workbook = openpyxl.load_workbook('Reports/data.xlsx')

    # selecting the worksheet
    sheet = workbook['Sales Rating']

    column_number = 1

    
    global column_data

    # Iterate through the rows in the column and append each cell's value to the list
    for row in sheet.iter_rows(min_row=2, min_col=column_number, values_only=True):
        if row[0] is not None:  # Check if the cell is not empty
            column_data.append(row[0])

    # Close the Excel file
    workbook.close()
    return column_data