from wordnet_trainer.vocab_creator import VocabCreator

def main():

    vocab_creator = VocabCreator(src_path = "/home/musa/data/language/english/aclImdb/aclImdb/train/pos")
    vocab_creator.create(save_path = "./vocab.txt")

if __name__ == "__main__":
    main()
