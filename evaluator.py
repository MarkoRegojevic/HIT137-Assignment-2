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

     if char in '+-*/()':
        tokens.append((char, char))
        i+= 1
        continue

    if char == "(":
        tokens.append(('LPAREN', char))
        i+= 1
        continue

    if char == ")":
        tokens.append(('RPAREN', char))
        i+= 1
        continue

    raise ValueError(f"Unknown character {char} at position {i}")

tokens.append(('EOF', None))
return tokens

