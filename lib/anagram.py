# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, list_of_words: list):
        matches = []

        for word in list_of_words:
            flag = True
            counter = 0
            if len(word) != len(self.word):
                continue
            else:
                while flag and counter < len(self.word):
                    if word.count(word[counter]) != self.word.count(self.word[counter]):
                        flag
                        flag = False
                    else:
                        counter += 1
            matches.append(word) if flag else None
        return matches
