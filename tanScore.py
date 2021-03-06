import spacy
import multiprocessing
from functools import partial
import gc

nlp = spacy.load("en_core_web_md")


SMALLEST_SIM = 0.34
LARGEST_SIM = 0.68
TARGET_SIM = SMALLEST_SIM + ((LARGEST_SIM - SMALLEST_SIM)/2)

def process_text(text):
    doc = nlp(text.lower())
    result = []
    for token in doc:
        if token.text in nlp.Defaults.stop_words:
            continue
        if token.is_punct:
            continue
        if token.lemma_ == '-PRON-':
            continue
        result.append(token.lemma_)
    result = [item.strip() for item in result if item.strip()]
    return " ".join(result)

def scoreTangentiality(text_a, text_b):
    score = nlp(text_a).similarity(nlp(text_b))
    return abs(TARGET_SIM-score), text_a


def getBestMatch(text):
    gc.collect()
    bestScore = 1
    bestMatch = ""
    # text = process_text(text)
    #
    # pool = multiprocessing.Pool(multiprocessing.cpu_count()-1)
    # results = pool.map(partial(scoreTangentiality, text_b=text), data)
    with open("dataset.txt") as f:
        for row in f.readlines():
            if row.strip():
                score = scoreTangentiality(row.strip(), text)
                if score < bestScore:
                    bestScore = score
                    bestMatch = row

    return bestMatch
