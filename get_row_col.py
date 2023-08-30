board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]
letter_to_number = {"A": 0, 
                    "B": 1, 
                    "C": 2}    
number_to_number = {"1": 0, 
                    "2": 1, 
                    "3": 2} 

def get_row_col(cell_name):
    capital_letter = cell_name[0]
    number = cell_name[1]
    # number = int(cell_name[1])-1 das Beste

    for k, v in letter_to_number.items():
        if capital_letter == k:
            column = list(letter_to_number.values())[v]

    for k, v in number_to_number.items():
        if number == k:
            row = list(number_to_number.values())[v]

    tuple_result = (row, column)
    print(tuple_result)

get_row_col("B3")