# word tokenize using underthesea
import pandas as pd
import numpy as np
from underthesea import word_tokenize


def word_tokenize_underthesea(text):
    return word_tokenize(text, format="text")


# read content.txt
with open('word_tokenize/test_data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
content_under = word_tokenize_underthesea(content)
content_under = content_under.split("/n")
# save to txt file
with open('word_tokenize/result_underthesea.txt', 'w', encoding='utf-8') as f:
    for item in content_under:
        f.write("%s\n" % item)
