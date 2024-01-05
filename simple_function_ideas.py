import python_debug as dbg
# two modes:
#       [t, x, y, z] mode
#       [t, r, \theta, \phi] mode

def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@dbg.debug_function
def index_translator(line):
    @dbg.debug_function
    def index_translator_translate(index):
        index_translation = {
                "t":"0",
                "x":"1",
                "r":"1",
                "y":"2",
                "\\theta":"2",
                "z":"3",
                "\\phi":"3"
                }
        if index in index_translation:
            return index_translation[index]
        else:
            return index # idk what I should do with this right now...
    return index_translator_translate(line)
    # check for "^" or "_", 

@dbg.debug_function
def kronecker_delta(i,j):
    if i.isnumb() and j.isnumb():
        if i == j:
            return 1
        elif i != j:
            return 0
        # give capabity for either one to have a numerical value and the other to not, so would either give something like i=1:  [1,0,0,0] or j=3: [[0],[0],[1],[0]]
    delta = []
    for i in range(square):
        row = []
        for j in range(square):
            row += [1] if i==j else [0]
        if i.isdigit():
            return row

        delta.append(row)
    return delta

@dbg.debug_function
def latex_interpretation(line):
    # input: \delta_{ij}
    # look for _ or ^
    new_line = ""
    line_length = len(line)
    n = 0
    while n <= line_length:
        index = False
        new_line += line[n]
        n += 1
        if n > 0:
            section = line[n-1] + line[n]
            if section == "_{":
                current = "{"
                while current != "}" or n <= line_length: # need to get it to ignore things between "\" and " ".
                    n += 1
                    new_line += index_translator(line[n])
    return new_line
dbg.debug("Cheese")
print(latex_interpretation("2x_{txyp}"))
