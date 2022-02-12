encoded = input("deşifre yazılımı için şifresini oluşturduğunuz her kelimeyi ayrı ayrı olarak girmeniz gerekmektedir.Yazılımı her kelime için bir kez çalıştırmalısınız.\n"
                "şifrenin girilmesi gereken format:x-y-z-(kelimenin şifreleri aralarında virgül olacak şekilde).\nÖrnek:1001-1000010100-10001101-(8, 6, 1)\nçözmek istediğiniz kodu giriniz:  ")
encoded_1 = encoded.split("-")

# in number list there are the number values of the letters
number_list = []
# bu göngü ile hem binary kodun sayısal değerini hemde bu binary kodu elde edebilmek için kullanabileceğimiz bütün
# kodların uzunluğunu elde ediyoruz

for char in encoded_1[0:-1]:
    number = 2**(len(char)) - 1
    number_2 = int(char,2)
    number_list.append([number,number_2,char])

# finding the polygonal number and x number and y number
# a function to find the indexes of each character in a word
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

# stripping the y value
y_value = encoded_1[-1]
stripped_y = y_value.replace("(", "")
stripped_y_2 = stripped_y.replace(")", "")
y_list = stripped_y_2.split(",")

binary_digits = list()
n = 0

alphabet = "abcçdefgğhiıjklmnoöprsştuüvyz"
letter_list = list()
for char in number_list:
    word = y_list[n]
    n = n + 1
    binary_code = bin(int(word))
    real_code = ((len(str(bin(int(max(y_list)))).split("b")[1]) - len(str(binary_code).split("b")[1])) * "0") + binary_code.split("b")[1]
    indexes = find(real_code,"1")
    y = sum(indexes) + len(indexes) + 3
    outputs_list = []
    for i in range(char[0] + 1):
        binary_digits.append(bin(i))
        binary_digits_2 = binary_digits.copy()
    for t in binary_digits:
        output_t = int(t,2)
        for c in binary_digits_2:
            output_c = int(c,2)
            length_1 = int(len(str(c))) -2
            length_2 = int(len(str(t))) - 2
            variable_1 = (max(length_2,length_1) - len(str(bin(output_c ^ output_t)).split("b")[1] ))
            # print((variable_1 * "0") + str(bin(output_c ^ output_t)).split("b")[1],"value")
            if (variable_1 * "0") + str(bin(output_c ^ output_t)).split("b")[1] == char[2]:
                if [output_c,output_t] not in outputs_list:
                    outputs_list.append([output_c,output_t])
    for ns in outputs_list:
        x = ns[0]
        polygonal = ns[1]
        if (((x - 2) * (y ** 2)) - (x - 4) * y) // 2 == polygonal:
            letter = x - 2 - binary_code.count("1")
            if alphabet[letter] not in letter_list:
                letter_list.append(alphabet[letter])
    binary_digits = []

p = 0
real_word = (len(bin(int(max(y_list)))) - 2) * "-"
real_word = list(real_word)

for char in letter_list:
    word = y_list[p]
    p = p + 1
    first_part = str(bin(int(word))).split("b")[1]
    bin_word = ((len(bin(int(max(y_list)))) - 2) - len(first_part)) * "0" + first_part
    indexes_of_ones = find(bin_word, "1")
    for c in indexes_of_ones:
        real_word[int(c)] =char
        print("".join(real_word))