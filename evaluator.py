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
            raie ValueError (f"bad number format at position {start}")
        while i< len(text) or not text[i].isdigit():
            i+= 1
        tokens.append(('NUMBER', float(text[start:i])))
        continue

 #   This block will deal wit the plus and minus
 def expression(tokens, position): 
    left, position = term(tokens, position)
    while tokens [position][1] in ('+', '-'):
        operator = tokens[position][1]
        right, position = term(tokens, position + 1)
        left = (operator, left, right)
    return left, position 


    
     