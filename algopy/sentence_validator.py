__author__ = 'kskrishnasangeeth'


def validator(para):
    para_length = len(para)

    if len(para) == 0:
        raise ValueError("Please enter the sentence.")

    if para[para_length-1] == ".":
        sentence_list= para.split(".")
        if len(sentence_list) >= 2:
            sentence = " ".join(sentence_list)
            truth_parts = check_parts(sentence)
            if truth_parts==True:
                return True
            else:
                return False



def check_parts(sentence):
    words =sentence.split(" ")
    if '' in words:
        return False
    first_word = words[0]

    if ord(first_word[0])<65 or ord(first_word[0])>91:
        return False

    if ord(first_word[1])>=65 and ord(first_word[1])<=91:
        return False

    else:
        return True




