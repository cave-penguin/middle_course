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
                        string_without_p = string.lower().format(symbol,
                                                                 '').split()
                    strings_list.extend(string_without_p)
                all_words[name] = strings_list
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        for name, words in all_words.items():
            for index, word_from_file in enumerate(words):
                if word.lower() == word_from_file:
                    return {name: index + 1}

    def count(self, word):
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word.lower() in words:
                return {name: words.count(word.lower())}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего