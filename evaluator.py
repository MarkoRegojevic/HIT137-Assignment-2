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

    return left, positionn 

/////////////// #jacobs part next

# This block deals with negative numbers 


# This block will deal with powers


#This block deals with numbers and brackets 






