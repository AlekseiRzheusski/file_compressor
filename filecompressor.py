import io
import string
import random
import json


def key_generator(size=4, chars=string.ascii_letters + string.digits):
    return '#' + ''.join(random.choice(chars) for _ in range(size))


class FileCompressor():
    def __init__(self, filepath='files/file', compressedpath='files/compressedFile'):
        self.filepath = filepath
        self.compressedpath = compressedpath

    def create_list_of_words(self):
        list_of_words = {}
        words = []
        with io.open(self.filepath, 'r') as file:
            for line in file.readlines():
                words.clear()
                words = line.split()
                for word in words:
                    if len(word) > 5:
                        if word in list_of_words:
                            list_of_words[word] += 1
                        else:
                            list_of_words[word] = 1
        return list_of_words

    def create_dictionary(self):
        words = self.create_list_of_words()
        dictionary = {}
        count = 0
        for key, value in words.items():
            if value * len(key) > value * 5 + (6 + len(key)):
                dictionary_key = key
                dictionary[dictionary_key] = key_generator()
                count += 1
        print(count)
        print(len(dictionary))
        return dictionary

    def create_compressed_file(self):
        dictionary = self.create_dictionary()
        words = []
        print(dictionary)
        with io.open(self.compressedpath, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, ensure_ascii=False)
        with io.open(self.filepath, 'r') as readed_file:
            with io.open(self.compressedpath, 'a', encoding='utf-8') as writed_file:
                for line in readed_file.readlines():
                    words.clear()
                    words = line.split()
                    for i in range(len(words)):
                        if words[i] in dictionary:
                            words[i] = dictionary[words[i]]
                    writed_line = ' '.join(words)
                    print(writed_line)
                    writed_file.write(writed_line)

