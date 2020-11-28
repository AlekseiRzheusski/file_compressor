import io
import functions
import string


class FileDecompressor:
    def __init__(self, compressedpath='files/compressedFile', decompressedpath='files/decompressedFile'):
        self.compressedpath = compressedpath
        self.decompressedpath = decompressedpath

    @functions.decor
    def create_dictionary(self):
        '''creates dict from dictionary of compressed file'''
        word_dictionary = {}
        with io.open(self.compressedpath, 'r', encoding='utf-8') as file:
            line_dictionary = file.readlines()[0]
        length = int(line_dictionary[0])
        print(length)
        value = ""
        for i in range(1, len(line_dictionary)):
            if line_dictionary[i] == '#':
                key = ""
                for j in range(length):
                    key += line_dictionary[i]
                    i += 1
                value = ''
                while line_dictionary[i] != '#':
                    value += line_dictionary[i]
                    i += 1
                    if i >= len(line_dictionary):
                        break
                word_dictionary[key] = value
        return word_dictionary

    @functions.decor
    def create_decompressed_file(self):
        """creates decompressed file"""
        dictionary = self.create_dictionary()
        result_line = ""
        words = []
        is_dot = False
        with io.open(self.compressedpath, 'r', encoding='utf-8') as readed_file:
            lines = readed_file.readlines()
        del lines[0]
        for line in lines:
            words.clear()
            words = line.split()
            for i in range(len(words)):
                tmp_str = ""
                index = 1
                if words[i][0] in "!$%&()*+, -./:;<=>?@[]^_`{|}~":
                    index = 0
                    tmp_str += words[i][0]
                    translator = str.maketrans('', '', "!$%&()*+, -./:;<=>?@[]^_`{|}~")
                    words[i] = words[i].translate(translator)
                elif words[i][-1] in "!$%&()*+, -./:;<=>?@[]^_`{|}~":
                    tmp_str += words[i][-1]
                    index = -1
                    translator = str.maketrans('', '', "!$%&()*+, -./:;<=>?@[]^_`{|}~")
                    words[i] = words[i].translate(translator)

                if words[i] in dictionary:
                    if index == 0:
                        key = dictionary[words[i]]
                        words[i] = tmp_str
                        words[i] += key
                    elif index == -1:
                        words[i] = dictionary[words[i]]
                        words[i] += tmp_str
                    else:
                        words[i] = dictionary[words[i]]

            writed_line = ' '.join(words)
            writed_line += '\n'
            result_line += writed_line
        with io.open(self.decompressedpath, 'w', encoding='utf-8') as writed_file:
            writed_file.write(result_line)

