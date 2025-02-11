import re
from collections import Counter


stop_words= {"i", "a", "the", "and","is", "it", "in", "on","for","of", "to","at","this"}

def analizowanieTekstu(text):




    slowa=re.findall(r'\\b\\w+\\b',text)

    zdania=list(filter(bool, re.split(r'[.!?]', text)))
    akap=list(filter(bool, text.split("\\n")))

    word_count = len(slowa)
    sentence_count = len(zdania)
    paragraph_count = len(akap)




    transform_text= " ".join(
        map(lambda word: word[::-1]

        if word.lower().startswith("a")

        else word, slowa)
    )

    return {
        "word_count": word_count,

        "sentence_count": sentence_count,

        "paragraph_count": paragraph_count,

        "transform_text": transform_text
    }


sample_text = (
   "lorem ipsum dolor "
   ""
   "igfhewfhwehfjew fjjhwejfhewjf iefkmj djawn  aaaa a a erthemfwemndkaldm, aghdfhdb aghfejd good agood "
   " hello dark jdfhgjf hello hghsfhs hello fjshej hello fhjsfghsf hello  alala a alalal ala lala allalal alala lala laa ala ala ala alalalalala "
   ""
   "     alalalalalal alalalaal    alalala la "
   " lslslslsl ls lsl sl sl ls ls ls ls ls "
   )


result=analizowanieTekstu (sample_text)


print("Liczba słów:", result["word_count"])

print("Liczba zdań:", result["sentence_count"])

print("Liczba akapitów:", result["paragraph_count"])

print("Tekst po transformacji:", result["transform_text"])
