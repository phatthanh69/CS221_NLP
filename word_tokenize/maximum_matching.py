import re

f = open("word_tokenize/dictionary.txt", mode="r", encoding="utf-8").read().splitlines()

dictionary = set(f)

train = open("word_tokenize/train_data.txt", mode="r", encoding="utf-8").read().splitlines()
for item in train:
    item = item.strip().split()
    if "" in item:
        item.remove("")
    for word in item:
        word = word.replace("_", " ")
        dictionary.add(word)
# special_character
special_character = [",", "–", ";", ":", '''"''', "(", ")", "?", "!", "..."]
special_character = set(special_character)


# oa, oe, uy -> /wa/, /wɛ/, /wi/ nên phải bỏ dấu vào chữ a, e và y
# sources: https://vi.wikipedia.org/wiki/Quy_t%E1%BA%AFc_%C4%91%E1%BA%B7t_d%E1%BA%A5u_thanh_trong_ch%E1%BB%AF_qu%E1%BB%91c_ng%E1%BB%AF

# split sentences to words with space and special character
def split_sentences(sentences):
    final_array = []
    cur = 0
    i = 0

    while i < len(sentences):
        # if has special character -> split
        if sentences[i] in special_character:
            # reported speech
            if sentences[i] == ":":
                if sentences[i + 1] == " ":
                    sentences = sentences[:i + 1] + sentences[i + 2:]
            # check ! and ? at the end of sentences
            if not (sentences[i] == "!" and i != len(sentences) - 1):
                left = sentences[cur:i].strip().split(" ")

                if left[0] != "":

                    for item in left:
                        final_array.append(item)
                final_array.append(sentences[i])
                cur = i + 1
        i = i + 1
    # if no special character -> split
    if cur < len(sentences):
        left = sentences[cur:i].strip().split(" ")
        for item in left:
            final_array.append(item)
    return final_array


# match word with maximum matching
def split_string(string):
    array = split_sentences(string)
    i = 0
    pos = 4
    final_arr = []
    while i < len(array):
        while True:
            cur_string = " ".join(array[i:i + pos])
            # if pos = 1 -> break
            if pos == 1:
                break
            # if string has
            if not re.search("[,()–:;.?!\"]", cur_string):
                # check noun, word start with capital letter and not contain number
                if cur_string.istitle() and not re.search("\d", cur_string):
                    # check if word is at the beginning of the line. Or after ? or !
                    if i == 0:
                        # if word is at the beginning of the line -> break
                        # tuy nhiên cách này cũng k bao phủ tất cả trường hợp, ví dụ trong tên riêng từ đầu có trong từ điển
                        if array[i].lower() in dictionary:
                            final_arr.append(array[i])
                            cur_string = " ".join(array[i + 1:i + pos])

                    i = i + pos - 1
                    break
                # check word is in dictionary
                if cur_string.lower() in dictionary:
                    i = i + pos - 1
                    break
            pos = pos - 1
        final_arr.append(cur_string.replace(" ", "_"))
        pos = 4
        i = i + 1
    return final_arr


# test
sentences = open("word_tokenize/test_data.txt", mode="r", encoding="utf-8").read().splitlines()
for item in sentences:
    result = split_string(item)
    print(*result)