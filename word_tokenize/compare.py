# compare result of word_tokenize
special_character = [",", "–", ";", ":", '''"''', "(", ")", "?", "!", "..."]
special_character = set(special_character)

# split sentences to words


def split_compare_sentences(_sen):
    array = []
    cur_pos = 0
    i = 0
    while i < len(_sen):
        if _sen[i] == " ":
            array.append(_sen[cur_pos: i])
            cur_pos = i
        elif _sen[i] == "_":
            array.append(_sen[cur_pos: i])
            cur_pos = i
        i += 1
    array.append(_sen[cur_pos:])
    return array

# compare two sentences


def result_compare_sentences(sentences1, sentences2):
    sentences1 = split_compare_sentences(sentences1)
    sentences2 = split_compare_sentences(sentences2)

    i = 0
    result = 0
    while i < len(sentences1):
        if sentences1[i][0] == "_":
            cur_sentences = [sentences1[i - 1], sentences1[i]]
            if i + 1 < len(sentences1):
                if sentences1[i + 1][0] == "_":
                    cur_sentences.append(sentences1[i + 1])
                    if i + 2 < len(sentences1):
                        if sentences1[i + 2][0] == "_":
                            cur_sentences.append(sentences1[i + 2])

            compare_sentences = []
            for j in range(i - 1, i - 1 + len(cur_sentences)):
                compare_sentences.append(sentences2[j])

            if cur_sentences == compare_sentences:
                result += 1
            i += len(cur_sentences) - 1
        i += 1
    return result


# read result from txt file
hand_result = open("word_tokenize/result_byhand.txt", mode="r",
                   encoding="utf-8").read().splitlines()
under_result = open("word_tokenize/result_underthesea.txt", mode="r",
                    encoding="utf-8").read().splitlines()
mm_result = open("word_tokenize/result_maxmat.txt", mode="r",
                 encoding="utf-8").read().splitlines()
mm_result_notrain = open("word_tokenize/result_maxmat_notrain.txt", mode="r",
                         encoding="utf-8").read().splitlines()
sum_score_under = 0
sum_score_mm = 0
sum_score_mm_notrain = 0
# compare result
for i in range(0, len(hand_result)):
    sum_score_under += result_compare_sentences(
        hand_result[i], under_result[i])
    sum_score_mm += result_compare_sentences(hand_result[i], mm_result[i])
    sum_score_mm_notrain += result_compare_sentences(
        hand_result[i], mm_result_notrain[i])
max_score = 0
for item in hand_result:
    item = item.split(" ")
    for j in item:
        if j.count("_") > 0:
            max_score += 1
print("Xác suất phương pháp Maximum Matching không train: " +
      str(sum_score_mm_notrain / max_score * 100))
print("Xác suất phương pháp Maximum Matching đã train: " +
      str(sum_score_mm / max_score * 100))
print("Xác suất phương pháp Underthesea: " +
      str(sum_score_under / max_score * 100))
