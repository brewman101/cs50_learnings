# Read input
word_out=""
word_in=input("Input: ")
for _ in range(len(word_in)):
    character=(word_in[_]).lower()
    print(character)
    if character=="a" or character =="e" or character =="i" or character =="o" or character =="u":
        word_out=word_out
    else:
        word_out=word_out+word_in[_]
print(word_out)


