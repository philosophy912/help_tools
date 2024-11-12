# -*- coding:utf-8 -*-
# --------------------------------------------------------
# Copyright (C), 2016-2020, omosoft, All rights reserved
# --------------------------------------------------------
# @Name:        t8.py
# @Author:      lizhe
# @Created:     2024/10/8 - 11:21
# --------------------------------------------------------
import stanza
from collections import Counter

stanza.download('zh')

nlp = stanza.Pipeline('zh', processors='tokenize,pos,lemma,depparse', use_gpu=False)
file = r"/Users/lizhe/Downloads/yuzeng/test.txt"

with open(file, "r", encoding="utf-8") as f:
    contents = f.read()
    doc = nlp(contents)
    nlp_list = [(word.text, word.upos) for sent in doc.sentences for word in sent.words if
                word.upos not in ("PUNCT", "NUM")]

keyword = "责任"
keyword_list = [(index, word, upos) for index, (word, upos) in enumerate(nlp_list) if
                keyword == word and upos in ["NOUN", "VERB"]]

relate_keyword_list = []
previous_keyword_list = []
next_keyword_list = []
# upos_set = set()

words_list = []
for index, word, upos in keyword_list:
    if index == 0:
        next_word, next_upos = nlp_list[index + 1]
        next_keyword_list.append((next_word, next_upos))
        words_list.append((next_word, next_upos))
    elif index == len(nlp_list) - 1:
        last_word, last_upos = nlp_list[index - 1]
        previous_keyword_list.append((last_word, last_upos))
        words_list.append((last_word, last_upos))
    else:
        last_word, last_upos = nlp_list[index - 1]
        next_word, next_upos = nlp_list[index + 1]
        words_list.append((next_word, next_upos))
        words_list.append((last_word, last_upos))
        previous_keyword_list.append((last_word, last_upos))
        next_keyword_list.append((next_word, next_upos))

noun_list = [word for word, upos in words_list if upos == "NOUN"]
verb_list = [word for word, upos in words_list if upos == "VERB"]

previous_noun_list = [word for word, upos in previous_keyword_list if upos == "NOUN"]
previous_verb_list = [word for word, upos in previous_keyword_list if upos == "VERB"]

next_noun_list = [word for word, upos in next_keyword_list if upos == "NOUN"]
next_verb_list = [word for word, upos in next_keyword_list if upos == "VERB"]

noun_counts = Counter(noun_list)
verb_counts = Counter(verb_list)

next_noun_counts = Counter(next_noun_list)
next_verb_counts = Counter(next_verb_list)

previous_noun_counts = Counter(previous_noun_list)
previous_verb_counts = Counter(previous_verb_list)

print(f"{noun_counts = }")
print(f"{verb_counts = }")

print(f"{next_noun_counts = }")
print(f"{next_verb_counts = }")

print(f"{previous_noun_counts = }")
print(f"{previous_verb_counts = }")



