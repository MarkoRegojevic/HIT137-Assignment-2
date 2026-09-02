def encrypt_file(shift1: int, shift2: int, input_path: str, output_path: str) -> None:

    with open(input_path,"r",encoding="utf-8") as in_file:
        txt=in_file.read()
    result=""

    for i in txt:
        if "a"<=i<="n":
            pos=ord(i)-ord("a")
            pos=(pos+shift1*shift2)%14
            result+=chr(ord("a")+pos)
        elif "o"<=i<="z":
            pos=ord(i)-ord("o")
            pos=(pos-(shift1+shift2))%12
            result+=chr(ord("o")+pos)
        elif "A"<=i<="M":
            pos=ord(i)-ord("A")
            pos=(pos-shift1)%13
            result+=chr(ord("A")+pos)
        elif "N"<=i<="Z":
            pos=ord(i)-ord("N")
            pos=(pos+shift2**2)%13
            result+=chr(ord("N")+pos)
        elif "0"<=i<="9":
            pos=ord(i)-ord("0")
            pos=(pos+shift1-shift2)%10
            result+=chr(ord("0")+pos)
        else:
            result+=i

    with open(output_path,"w",encoding="utf-8") as out_file:
        out_file.write(result)


def decrypt_file(shift1: int, shift2: int, input_path: str, output_path: str) -> None:

    with open(input_path,"r",encoding="utf-8") as in_file:
        txt=in_file.read()
    result=""

    for i in txt:
        if "a"<=i<="n":
            pos=ord(i)-ord("a")
            pos=(pos-shift1*shift2)%14
            result+=chr(ord("a")+pos)
        elif "o"<=i<="z":
            pos=ord(i)-ord("o")
            pos=(pos+shift1+shift2)%12
            result+=chr(ord("o")+pos)
        elif "A"<=i<="M":
            pos=ord(i)-ord("A")
            pos=(pos+shift1)%13
            result+=chr(ord("A")+pos)
        elif "N"<=i<="Z":
            pos=ord(i)-ord("N")
            pos=(pos-shift2**2)%13
            result+=chr(ord("N")+pos)
        elif "0"<= i<="9":
            pos=ord(i)-ord("0")
            pos=(pos-shift1+shift2)%10
            result+=chr(ord("0")+pos)
        else:
            result+=i

    with open(output_path,"w",encoding="utf-8") as out_file:
        out_file.write(result)


def verify_files(original_path: str, decrypted_path: str) -> bool:

    with open(original_path,"r",encoding="utf-8") as in_file:
        orig=in_file.read()
    with open(decrypted_path,"r",encoding="utf-8") as in_file:
        decrypted=in_file.read()

    if orig==decrypted:
        print("Decryption successful.")
        return True
    else:
        print("Decryption unsuccessful.")
        return False

if __name__ == "__main__":
    shift1=int(input("Enter shift1: "))
    shift2=int(input("Enter shift2: "))

    if shift1<0 or shift2<0:
        print("shift1 and shift2 must be non-negative integers.")
    else:
        encrypt_file(shift1,shift2,"raw_text.txt","encrypted_text.txt")
        decrypt_file(shift1,shift2,"encrypted_text.txt","decrypted_text.txt")
        verify_files("raw_text.txt","decrypted_text.txt")