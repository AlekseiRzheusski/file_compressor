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

    def create_utf8(self):
        with io.open(self.filepath, 'r', encoding='utf-8') as file:
            tmp_string = file.read()
        with io.open(self.filepath, 'a', encoding='utf-8') as writed_file:
            writed_file.write(tmp_string)

    def create_list_of_words(self):
        list_of_words = {}
        words = []
        with io.open(self.filepath, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                words.clear()
                translator = str.maketrans('', '', string.punctuation)
                line = line.translate(translator)
                line = line.lower()
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
        key_line = '5'
        for key, value in dictionary.items():
            key_line += value + key
        with io.open(self.compressedpath, 'w', encoding='utf-8') as file:
            file.write(key_line)
        with io.open(self.filepath, 'r', encoding='utf-8') as readed_file:
            with io.open(self.compressedpath, 'a', encoding='utf-8') as writed_file:
                for line in readed_file.readlines():
                    words.clear()
                    words = line.split()
                    for i in range(len(words)):
                        tmp_str = ""
                        index = 1
                        if words[i][0] in string.punctuation:
                            index = 0
                            tmp_str += words[i][0]
                            translator = str.maketrans('', '', string.punctuation)
                            words[i] = words[i].translate(translator)
                        elif words[i][-1] in string.punctuation:
                            tmp_str += words[i][-1]
                            index = -1
                            translator = str.maketrans('', '', string.punctuation)
                            words[i] = words[i].translate(translator)

                        if words[i].lower() in dictionary:
                            if index == 0:
                                key = dictionary[words[i].lower()]
                                words[i] = tmp_str
                                words[i] += key
                            elif index == -1:
                                words[i] = dictionary[words[i].lower()]
                                words[i] += tmp_str
                            else:
                                words[i] = dictionary[words[i].lower()]
                    writed_line = ' '.join(words)
                    print(writed_line)
                    writed_file.write(writed_line + '\n')
