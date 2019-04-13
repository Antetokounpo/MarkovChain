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
        self.start_words.append(sentence[0])
        self.end_words.append(sentence[-1])

    def generate(self, raw_text):
        text = self.process_raw_text(raw_text)
        for raw_sentence in text:
            sentence = word_tokenize(raw_sentence)
            self.add_start_end_words(sentence)
            for i in range(len(sentence) - 1):
                word = sentence[i]
                if word not in self.graph:
                    self.graph[word] = list()
                self.graph[word].append(sentence[i + 1])

    def get_first_word(self):
        return random.choice(self.start_words)

    def sentence(self):
        starting_word = self.get_first_word()
        sentence = [starting_word]
        while 1:
            sentence.append(random.choice(self.graph[sentence[-1]]))
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

