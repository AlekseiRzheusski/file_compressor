import io

class FileCompressor():
    def __init__(self,filepath = 'files/file',compressedpath = 'files/compressedFile'):
        self.filepath = filepath
        self.compressedpath = compressedpath

    def create_list_of_words(self):
        list_of_words = {}
        words = []
        with io.open(self.filepath,'r') as file:
            for line in file.readlines():
                words.clear()
                words = line.split()
                for word in words:
                    if len(word)>3:
                        if word in list_of_words:
                            list_of_words[word] += 1
                        else:
                            list_of_words[word] = 1
        print(list_of_words)
