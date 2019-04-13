import random, sys
from nltk import word_tokenize, sent_tokenize

class MarkovChain:

    def __init__(self):
        self.graph = dict()
        self.start_words = list()
        self.end_words = list()

    def process_raw_text(self, raw_text):
        return sent_tokenize(raw_text)

    def add_start_end_words(self, sentence):
        self.start_words.append((' ').join(sentence[0:2]))
        self.end_words.append(sentence[-1])

    def generate(self, raw_text):
        text = self.process_raw_text(raw_text)
        for raw_sentence in text:
            sentence = word_tokenize(raw_sentence)
            self.add_start_end_words(sentence)
            for i in range(len(sentence) - 2):
                words = (' ').join(sentence[i:i + 2])
                if words not in self.graph:
                    self.graph[words] = list()
                self.graph[words].append(sentence[i + 2])

    def get_first_word(self):
        return random.choice(self.start_words)

    def sentence(self):
        starting_word = self.get_first_word()
        sentence = word_tokenize(starting_word)
        while 1:
            sentence.append(random.choice(self.graph[(' ').join(sentence[-2:])]))
            if sentence[-1] in self.end_words:
                return (' ').join(sentence)


def main():
    if len(sys.argv) != 2:
        print('Usage: markov.py [filename]')
        return
    markov = MarkovChain()
    with open(sys.argv[1], 'r') as (f):
        raw_text = f.read()
    markov.generate(raw_text)
    print(markov.sentence())


if __name__ == '__main__':
    main()

