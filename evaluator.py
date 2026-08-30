import os

# makes the tokens from expression
def tokenize(text):
    i=0
    while i < len(text):
        char=text[i]
if char.isspace():
    i +=1 
    continue

if char.isdigit():
    start=i
    while i < len(text) and text[i].isdigit():
       i+= 1
    if i < len(text) and text[i] == '.':
        i+= 1
        if i>= len(text) or not text[i].isdigit():
            raise ValueError (f"bad number format at position {start}")
        while i< len(text) or not text[i].isdigit():
            i+= 1
        tokens.append(('NUMBER', float(text[start:i])))
        continue

 #   This block will deal wit the plus and minus
 def expression(tokens, position): 
    left, position = term(tokens, position)

    while tokens [position][0] == "OP" and tokens [position][1] in ("+", "-"):
        operator = tokens[position][1]
        right, position = term(tokens, position + 1)
        left = (operator, left, right)
    return left, position 

# This block will deal with multuplication, division and remainder, and also implicit multiplication. . 
def term(tokens, position): 
    left, position = unary(tokens, position) 

while true: 
    if tokens[position][0] == "OP" and tokens[position][1] in ("*", "/", "%"):
        operator = tokens[position][1]
        right, position = unary(tokens, position + 1)
        left = (operator, left, right)

    elif tokens[position][0] == "NUM" :
        raise ValueError()
    
    elif tokens[position][0] == "LPAREN":
        right, position = unary(tokens, position)
        left = ("*", left, right) 
    else: 
        break

    return left, position

/////////////// #jacobs part next

# This block deals with negative numbers 
def unary(tokens, position):

    if tokens[position][0] == "OP":
        if tokens[position][1] == "-":
            answer, position = unary(tokens, position + 1)
            return ("neg", answer), position
        if tokens[position][1] == "+":
            raise ValueError()
    return power(tokens, position)

# This block will deal with powers
def power (tokens, position):

    left, position = primary(tokens, position)

    if tokens[position][0] == "OP":
        if tokens[position][1] == "^":
            right, position = unary(tokens, position +1)
            left = ("^", left, right)

    return left, position

#This block deals with numbers and brackets 
def primary (tokens, position):
    if tokens[position][0] == "NUM":
        number = float(tokens[position][1])
        return number, position + 1
    if tokens[position][0] == "LPAREN":
        answer, position = expression(tokens, position + 1)
        if tokens[position][0] != "RPAREN":
            raise ValueError
        return,answer, position +1
raise ValueError ()

////// markos part next

# works out the answer from the tree




# changes the tree into the format needed by the assginment



#changes tokens into required format


////// jacobs part next


# makes the result look like the required format
def result_string(number):
    if number.is_integer():
        return str(int(number))

    return str(round(number, 4))

# evalutes one line
def evaluate_line(line):
    try: 
        tokens = tokenize(line)

        if len(tokens) == 1:
            raise ValueError

        tree, position = expression(tokens, 0)

        # ensures the entire line was read 
        if tokens[position][0] != "END":
            raise ValueError

        answer = calculate(tree)

        return {
            "input": line,
            "tree": tree_string(tree),
            "tokens": token_string (tokens),
            "result": answer
        }

    