# %%
import numpy as np

class Sudoku:
    def __init__(self):
        self.sudoku:np.ndarray[np.ndarray] = np.zeros((9,9)).astype(int)

    def __repr__(self) -> str:
        def delimit(str_list, delimiter, every, end=""):
            return "".join(str_list[:every])+delimiter+"".join(str_list[every:2*every])+delimiter+"".join(str_list[2*every:])+end
            
        lines = []
        for line in s.sudoku:
            line = line.astype(str)
            line = delimit(line, '  ', 3, "\n")
            lines.append(line)
        return delimit(lines,' '*9+'\n', 3)
    
    def get_square(self, square_nb):
        square_i, square_j = square_nb//3, square_nb%3
        return self.sudoku[square_i*3: square_i*3+3, square_j*3: square_j*3+3]

    
    def set(self, i, j, number):
        self.sudoku[i,j] = number

    def total_lines(self):
        return s.sudoku.sum(axis=1)
    def total_columns(self):
        return s.sudoku.sum(axis=0)
    def total_squares(self):
        return np.array([np.sum(self.square_mask(square_nb)*self.sudoku) for square_nb in range(9)])
    
    def is_correct(self):
        def has_no_duplicates(array:np.ndarray):
            uniqs,nuniqs = np.unique(array, return_counts=1)
            verif = 0 in uniqs
            return np.all(nuniqs[verif:]<2)
            
        for ij in range(9):
            if not has_no_duplicates(self.sudoku[:,ij]):
                return False
            
            if not has_no_duplicates(self.sudoku[ij,:]):
                return False
            
            if not has_no_duplicates(self.get_square(ij)):
                return False
            
            return True
            



# class brute_force:
#     def __init__(self, sudoku: Sudoku):
#         self.sudoku = sudoku
#         self.i, self.j=0,0
    
#     def next(self):

    

#     def can_fill_lines(self):
#         rest_lines = self.sudoku.sum(axis=1)-35
#         i_lines = np.where(rest_lines > 0)
#         self.fill_line(i_lines[0], rest_lines[i_lines[0]])

#     def fill_line(self, i, number):
#         j = np.where(self.sudoku[i,:] == 0)
#         s.sudoku[i,j] = number


#     def can_fill(self):
#         np.array(self.totals())-35
#         can_fil = lines,columns,squares

# %%
s = Sudoku()
s.set(0,0,1)
s.set(0,7,1)
print(s.is_correct())
print(s)