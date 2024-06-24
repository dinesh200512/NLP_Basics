import spacy
nlp = spacy.load('en_core_web_sm')
def show_lemmas(text):
    print(f'{"Token":{12}} {"POS":{6}} {"Lemma":{22}} {"Lemma_":{12}} {"Dependency":{12}} {"Children":{12}}')
    print('-' * 90)
    for token in text:
        print(f'{token.text:{12}} {token.pos_:{6}} {token.lemma:<{22}} {token.lemma_} \t {token.dep_:{12}} {list(token.children)}')
text1=nlp("The children were playing happily in the playground with their colorful toys.")
show_lemmas(text1)


