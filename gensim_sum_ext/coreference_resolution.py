import en_coref_md

nlp = en_coref_md.load()

def find_coreference_replace_pronominal(original_sents):
    u = original_sents.decode('utf8','ignore')
    #u = unicode(original_sents[i], "utf-8")
    doc = nlp(u)
    if doc._.has_coref:
        original_sents = str(doc._.coref_resolved)
    return original_sents