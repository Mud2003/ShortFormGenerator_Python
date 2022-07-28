def generator(sentence):
    word_list = sentence.split()
    short_form =""
    for i in word_list:
        short_form = short_form + i[0].upper()
    print(short_form)

text = input("text here.........")

generator(text)