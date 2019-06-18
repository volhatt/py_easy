# INPUT DATA
data = [
    (1000, 10),
    (2000, 17),
    (2500, 170),
    (2500, -170),
    ]

# Print the header for reference
print("REVENUE | PROFIT | PERCENT")

# THis template aligns and displays the date in the proper format
TEMPLATE = '{revenue:>7,} | {profit:>+6} | {percent:>7.2%}'
#TEMPLATE = '{revenue:>3,} | {profit:>+6} | {percent:>7.2%}'

# Print the data rows
for revenue, profit in data:
    row = TEMPLATE.format(revenue=revenue, profit=profit, percent=profit/revenue)
    print(row)
print('\n' +  ' * ' * 10 + '\n')

##### String Formatting and manupulating ####

INPUT_TEXT = """
    AFTER THE CLOSE OF THE SECOND QUARTER, OUR COMPANY, CASTAÑACORP
    HAS ACHIEVED A GROWTH IN THE REVENUE OF 7.47%. THIS IS IN LINE
    WITH THE OBJECTIVES FOR THE YEAR. THE MAIN DRIVER OF THE SALES HAS BEEN
    THE NEW PACKAGE DESIGNED UNDER THE SUPERVISION OF OUR MARKETING DEPARTMENT.
    OUR EXPENSES HAS BEEN CONTAINED, INCREASING ONLY BY 0.7%, THOUGH THE BOARD
    CONSIDERS IT NEEDS TO BE FURTHER REDUCED. THE EVALUATION IS SATISFACTORY
    AND THE FORECAST FOR THE NEXT QUARTER IS OPTIMISTIC. THE BOARD EXPECTS
    AN INCREASE IN PROFIT OF AT LEAST 2 MILLION DOLLARS.
    """

# Split text into individual words
words = INPUT_TEXT.split()

# Replace any numerical digits with an 'x' character
redacted = [''.join('X' if w.isdigit() else w for w in word) for word in words]

# Transform the text into pure ASCII
ascii_text = [word.encode('ascii', errors='replace').decode('ascii')
              for word in redacted]
print(ascii_text)
