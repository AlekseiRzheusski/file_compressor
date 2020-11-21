import io


class FileDecompressor:
    def __init__(self, compressedpath='files/compressedFile', decompressedpath='file/decompressedFile'):
        self.compressedpath = compressedpath
        self.decompressedpath = decompressedpath

    def create_dictionary(self):
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
                    if i>=len(line_dictionary):
                        break
                word_dictionary[key]=value
        print(word_dictionary)
