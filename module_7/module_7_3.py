class WordsFinder:
    def __init__(self, *files):
        self.file_names = []
        for file in files:
            self.file_names.append(file)

    def get_all_words(self):
        all_words = {}
        beams = {',', '.', '=', '!', '?', ';', ':', ' - '}
        for file in self.file_names:
            with open(file, encoding='utf-8') as _file:
                words = ''
                for lines in _file:
                    for char in lines:
                        if char not in beams:
                            words += char
                all_words[file] = words.lower().split()
        return all_words

    def find(self, word):
        words = self.get_all_words()
        word = word.lower()
        find_words = {}
        for key in words.keys():
            ind = 0
            if word in words[key]:
                for num in words[key]:
                    ind += 1
                    if word == num:
                        break
            if ind != 0:
                find_words[key] = ind
        return find_words

    def count(self, word):
        words = self.get_all_words()
        word = word.lower()
        count_words = {}
        for key in words.keys():
            ind = 0
            if word in words[key]:
                for num in words[key]:
                    if word == num:
                        ind += 1
            if ind != 0:
                count_words[key] = ind
        return count_words

finder2 = WordsFinder('test_file.txt', 'Walt Whitman - O Captain! My Captain!.txt', 'Rudyard Kipling - If.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
print(finder2.find('captain'))
print(finder2.count('captain'))
print(finder2.find('if'))
print(finder2.count('if'))


