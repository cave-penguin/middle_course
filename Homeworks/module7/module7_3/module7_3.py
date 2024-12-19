class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                strings = file.readlines()
                strings_list = []
                for string in strings:
                    p = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for symbol in p:
                        string = string.replace(symbol, '')
                    string_without_p = string.lower().split()
                    strings_list.extend(string_without_p)
                all_words[name] = strings_list
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            for index, word_from_file in enumerate(words):
                if word.lower() == word_from_file:
                    result[name] = index + 1
                    break
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            if word.lower() in words:
                result[name] = words.count(word.lower())
        return result


finder2 = WordsFinder('test_file.txt')
finder3 = WordsFinder('test_file2.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

print(finder3.get_all_words())
print(finder3.find('Need'))
print(finder3.count('That'))
