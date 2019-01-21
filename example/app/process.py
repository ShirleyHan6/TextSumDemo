# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from gensim.summarization.summarizer import _format_results
from .summarizer import summarize
from gensim.summarization.textcleaner import clean_text_by_sentences as _clean_text_by_sentences

import en_coref_md

nlp = en_coref_md.load()


def find_coreference_replace_pronominal(original_sents):
    u = original_sents.decode('utf8','ignore')
    #u = unicode(original_sents[i], "utf-8")
    doc = nlp(u)
    if doc._.has_coref:
        original_sents = str(doc._.coref_resolved)
    return original_sents


def summary_highlight(text, coref, ratio):
    if coref:
        coref_text = find_coreference_replace_pronominal(text)
    else:
        coref_text = text

    sum_text = summarize(text, coref_text, ratio=ratio)
    # extracted_sentences_number = get_extracted_number(sum_text, text)

    original_sentence_list = _format_results(_clean_text_by_sentences(text), True)
    extracted_sentence_list = _format_results(_clean_text_by_sentences(sum_text), True)

    index = 0
    for i in original_sentence_list:
        try:
            if i == extracted_sentence_list[index]:
                original_index = original_sentence_list.index(i)
                i = '<mark><em>' + i + '</em></mark>'
                original_sentence_list[original_index] = i
                if index < len(extracted_sentence_list)-1:
                    index += 1
        except IndexError:
            pass

    return " ".join(original_sentence_list)
