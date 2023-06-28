# cound word in result_byhand.txt, result_maxmat.txt, result_underthesea.txt

import pandas as pd
import numpy as np
import re
import os
# read full_sentences.txt
with open('word_tokenize/full_sentences.txt', 'r', encoding='utf-8') as f:
    content = f.read()
full_sentences = content.split("\n")
# read result_byhand.txt
with open('word_tokenize/result_byhand.txt', 'r', encoding='utf-8') as f:
    content = f.read()
content_byhand = content.split("\n")
# read result_maxmat.txt
with open('word_tokenize/result_maxmat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
content_maxmat = content.split("\n")
# read result_underthesea.txt
with open('word_tokenize/result_underthesea.txt', 'r', encoding='utf-8') as f:
    content = f.read()
content_under = content.split("\n")
# read result_maxmat_notrain.txt
with open('word_tokenize/result_maxmat_notrain.txt', 'r', encoding='utf-8') as f:
    content = f.read()
content_maxmat_notrain = content.split("\n")
# count max and min word in a sentence in full_sentences.txt
max_word = 0
min_word = 100
for item in full_sentences:
    if item != "":
        if len(item.split(" ")) > max_word:
            max_word = len(item.split(" "))
        if len(item.split(" ")) < min_word:
            min_word = len(item.split(" "))
# count word in result_byhand.txt
count_byhand = 0
for item in content_byhand:
    if item != "":
        count_byhand = count_byhand + len(item.split(" "))
# count word in result_maxmat.txt
count_maxmat = 0
for item in content_maxmat:
    if item != "":
        count_maxmat = count_maxmat + len(item.split(" "))
# count word in result_underthesea.txt
count_under = 0
for item in content_under:
    if item != "":
        count_under = count_under + len(item.split(" "))
# count word in result_maxmat_notrain.txt
count_maxmat_notrain = 0
for item in content_maxmat_notrain:
    if item != "":
        count_maxmat_notrain = count_maxmat_notrain + len(item.split(" "))
# print result
print("result_byhand.txt: ", count_byhand)
print("result_maxmat.txt: ", count_maxmat)
print("result_underthesea.txt: ", count_under)
print("result_maxmat_notrain.txt: ", count_maxmat_notrain)
print("max_word: ", max_word)
print("min_word: ", min_word)
