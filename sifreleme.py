import numpy as np
# kelimleri şifrelemek
sentence = input("şifresini oluşturmak istediğiniz kelimeyi giriniz:  ")
sentence = sentence.lower()
splitted = sentence.split(" ")
# a function to get all the indexes of a character in a string

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
# creating the binary digit for te word(word encoding)

zeros_dict = {}
for word in splitted:
    zeros_dict[word] =[]
    new_list = []
    for char in word:
        zeros = np.zeros((1, len(word)))
        zeros[0,find(word,char)] = 1
        new_list.append(list(zeros.flatten()))
    zeros_dict[word].append(new_list)

# finishing word encoding
for key,  value in zeros_dict.items():
    for char in value:
        char = list(map(tuple,char))
        char = list(dict.fromkeys(char))
        char = list(map(list,char))
        list_ms = []
        for m in char:
            m = list(map(int,m))
            m = list(map(str,m))
            m = "".join(m)
            # changes the string(binary code) into a decimal
            m = int(m,2)
            list_ms.append(m)
        zeros_dict[key] = list_ms

# finding x and y
alphabet = "abcçdefgğhiıjklmnoöprsştuüvyz"
x_dict = {}
for key  in zeros_dict.keys():
    xor_list= []
    for char in "".join(key):
        y = 0
        indexes = [i for i in range(len(key)) if key[i] == char]
        alphabet_order = alphabet.index(char)
        for char_1 in indexes:
            y += char_1
        y = y + key.count(char) + 3
        x = key.count(char) + 2 + alphabet_order
        polygonal_number= (x-2)* ((y*(y+1))//2) - y*(x-3)
        # print(char, x, y,polygonal_number)
        binary_digit_x = bin(x)
        binary_digit_polygonal = bin(polygonal_number)
        output_x = int(binary_digit_x,2)
        output_polygonal = int(binary_digit_polygonal,2)
        length_of_result= len(str(bin(output_polygonal)).split("b")[1])
        real_length = length_of_result - len(str(bin(output_x ^ output_polygonal)).split("b")[1])
        xor_performed = (real_length * "0") + str(bin(output_x ^ output_polygonal)).split("b")[1]
        if xor_performed not in xor_list:
            xor_list.append(xor_performed)
    zeros_dict[key] = [xor_list,zeros_dict[key]]
for key,value in zeros_dict.items():
    print(f"{key}:{value}")
