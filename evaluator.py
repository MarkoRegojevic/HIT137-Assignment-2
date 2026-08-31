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

 #jacobs part next

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

    token = tokens[position]

    #number
    if token[0] == "NUM":
        number = float(token[1])
        return number, position + 1

    #brackets
    if token[0] == "LPAREN":
        answer, position == expression(tokens, position + 1)

        if tokens[position][0] != "RPAREN":
            raise ValueError()

        return answer, position +1

    raise ValueError()


 #markos part next

#This function block of code will work out the answer from the tree 
def calculate(tree): 

    if isinstance(tree, float): #If the tree is jsut a number then return the number
        return tree
    if tree[0] == "neg": #If the tree is a negative number then return the negative of the number
        return -calculate(tree[1])

    operator = tree[0] 
    left = calculate(tree[1])
    right = calculate(tree[2])

    if operator == "+":
        return left + right
    elif operator == "-":
        return left - right
    elif operator == "*":
        return left * right
    elif operator == "/":
        if right == 0: 
            raise ZeroDivisionError()
        return left / right
    elif operator == "%":
        if right == 0: 
            raise ZeroDivisionError()
        return left % right
    elif operator == "^":
        return left ** right

    raise ValueError() # So if none of the above conditions work, then there will be an error

# This function block of code will chagne the tree into the format for the output file 
def tree_string(tree): 
    if isinstance(tree, float):
        return str(tree)

    return str(tree)
if tree[0] == "neg":
    return "(neg " + tree_string(tree[1]) + ")"
return "(" + tree[0] + " " + tree_string(tree[1]) + " " + tree_string(tree[2]) + ")" 

#changes tokens into required format
def token_string(tokens):
    answer = []

    for token in tokens: # It will go through each token one at a time 
        token_type = token[0]
        value = token[1]

        if token_type == "END": 
            answer.append("[END]")
        else: 
            answer.append("[" + token_type + ":" + value + "]")

    return " ".join(answer)  # This will put a space in between each token 


# jacobs part next

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
            "result": answer}

# Markos Part Nexttt ///////////

# This block of code function will read the input file provided and create the output file 
def evaluate_file(input_path: str):

    results = []

    with open(input_path, "r") as file:
        lines = file.readlines()

    for line in lines: 
        expression-text = line.rstrip("\n") 
        answer = evaluate_line(expression_text) 

        results.append(answer)

    if folder == "": 
        output_path = "output.txt" 
    else: 
        output_path = os.path.join(folder, "output.txt") 
    with open(output_path, "w") as file: 

        for results in results: 

            file.write("Input: " + result["input"] + "\n")
            file.write("Tree: " + result["tree"] + "\n")
            file.write("Tokens: " + result["tokens"] + "\n") 
            if result["result"] == "ERROR" : 
                file.write("Result: ERROR\n")
            else: 
                file.write("Result: " + result_string(result["result"]) + "\n")

            file.write("\n") 

    return results

# This block of code will run the  program 
if __name__ == "__main__":
    evaluate_file("sample_input.txt") 