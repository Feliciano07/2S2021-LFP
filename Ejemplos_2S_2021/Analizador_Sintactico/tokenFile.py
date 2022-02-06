class Token():
    def __init__(self, valid_lexeme, type, row, column):
        self.valid_lexeme = valid_lexeme
        self.type = type
        self.row = row
        self.column = column