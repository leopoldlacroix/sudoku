# %%
import numpy as np

class Sudoku:
    def from_inline_sudoku(inline_sudoku):
        sudoku = np.array(list(inline_sudoku)).reshape((9,9)).astype(int)
        return Sudoku(sudoku)
            
        
    def __init__(self, sudoku=np.zeros((9,9)).astype(int)):
        self.sudoku: np.ndarray[np.ndarray] = sudoku
        correct, reason = self.is_correct()
        assert reason

    def __repr__(self) -> str:
        def delimit(str_list, delimiter, every, end=""):
            return "".join(str_list[:every])+delimiter+"".join(str_list[every:2*every])+delimiter+"".join(str_list[2*every:])+end
            
        lines = []
        for line in self.sudoku:
            line = line.astype(str)
            line = delimit(line, '  ', 3, "\n")
            lines.append(line)
        return delimit(lines,' '*9+'\n', 3)
    
    def copy(self):
        return Sudoku(self.sudoku.copy())
    
    def get_square(self, square_nb):
        square_i, square_j = square_nb//3, square_nb%3
        return self.sudoku[square_i*3: square_i*3+3, square_j*3: square_j*3+3]

    
    def set(self, i, j, number):
        assert self.sudoku[i,j] == 0, f"cell {i},{j} is not empty"
        copy = self.copy()
        copy.sudoku[i,j] = number
        is_correct, reason = copy.is_correct()
        assert is_correct, f"setting {number} in cell {i,j} is not correct: {reason}"
        
        self.sudoku[i,j] = number
        return self
    def total_lines(self):
        return self.sudoku.sum(axis=1)
    def total_columns(self):
        return self.sudoku.sum(axis=0)
    def total_squares(self):
        return np.array([np.sum(self.get_square(square_nb)) for square_nb in range(9)])
    def where_empty(self):
        return np.stack(np.where(self.sudoku == 0), axis=1)
    
    def is_correct(self):
        def has_no_duplicates(array:np.ndarray):
            uniqs, nuniqs = np.unique(array, return_counts=1)
            problematic_numbers = uniqs[nuniqs>1]
            return problematic_numbers.sum() == 0, problematic_numbers
            
        for ij in range(9):
            no_duplicates, pb_number = has_no_duplicates(self.sudoku[ij,:])
            if not no_duplicates:
                # print(f'line {ij} has duplicate')
                return False, f"number {pb_number} in line #{ij}"
            
            no_duplicates, pb_number = has_no_duplicates(self.sudoku[:,ij])
            if not no_duplicates:
                # print(f'column {ij} has duplicate')
                return False, f"number {pb_number} in col #{ij}"
            
            no_duplicates, pb_number = has_no_duplicates(self.get_square(ij))
            if not no_duplicates:
                # print(f'square {ij} has duplicate')
                return False, f"number {pb_number} in square #{ij} appears at least twice"
            
        return True, "all_good"
    
    def is_win(self):
        correct, reason = self.is_correct()
        return self.sudoku.sum() == 9*45 and correct
    
class Sudoku_state:
    def __init__(self, sudoku: Sudoku):
        self.sudoku = sudoku
        
    def __repr__(self) -> str:
        return self.sudoku.__repr__()
        
    def next_states(self):     
        line, col = self.sudoku.where_empty()[0]
        
        next_states: list[Sudoku_state] = []
        for num in range(1,10):
            next_sudoku = self.sudoku.copy()
            try:
                next_sudoku.set(line, col, num)
                next_states.append(Sudoku_state(sudoku=next_sudoku))
            except AssertionError as message:
                # print(message)
                pass
        
        return next_states
    
    def score(self):
        return (self.sudoku.sudoku.sum() - 9*sum(range(10)))**2
    
# class nexxxsfjsdkf:
#     def can_fill_lines(self):
#         rest_lines = self.sudoku.sum(axis=1)-35
#         i_lines = np.where(rest_lines > 0)
#         self.fill_line(i_lines[0], rest_lines[i_lines[0]])

#     def fill_line(self, i, number):
#         j = np.where(self.sudoku[i,:] == 0)
#         self.sudoku[i,j] = number


#     def can_fill(self):
#         np.array(self.totals())-35
#         can_fil = lines,columns,squares

# %%
# s = Sudoku()
# s.set(0,0,1)
# s.set(0,7,1)
# print(s.is_correct())
# print(s)

# inline_sudoku = '123456789'+"745398162"+"869172345"+"981735426"+"634821597"+"257649813"+"376214958"+"492500000"+"000000030"
ss = Sudoku()
# print(ss)
# ss.is_correct()

explored = [Sudoku_state(ss)]

# %%
left = []
tried = 0
while not explored[-1].sudoku.is_win():
    tried += 1
    left+=explored[-1].next_states()
    explored.append(left.pop())
explored[-1]
# print(brute_0)
# print(brute_0)
# %%
