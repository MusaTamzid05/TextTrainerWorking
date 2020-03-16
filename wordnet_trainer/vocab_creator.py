import os
from wordnet_trainer.cleaner import clean_english_doc
from collections import Counter

class VocabCreator:

    def __init__(self , src_path , lang = "en"):
        self.src_path = src_path
        self.lang = lang
        self.vocab = Counter()

    def create(self , save_path , min_occurane = 2):

        print("Create vocabulary.")

        for filename in os.listdir(self.src_path):
            path = os.path.join(self.src_path , filename)
            self._process_doc(path)

        print(self.vocab.most_common(50))
        print("Total : {}".format(len(self.vocab)))
        tokens = [key for key , count in self.vocab.items() if count >= min_occurane]
        print("Final token length : {}".format(len(tokens)))
        self._save(tokens , save_path)


    def _process_doc(self , path):

        with open(path) as f:
            text = f.read()
            if self.lang == "en":
                tokens = clean_english_doc(text)
                self.vocab.update(tokens)



    def _save(self , tokens , save_path):

        data = "\n".join(tokens)

        with open(save_path , "w") as f:
            f.write(data)





