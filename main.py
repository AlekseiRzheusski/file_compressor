from filecompressor import FileCompressor

if __name__=="__main__":
    compressor = FileCompressor()
    # print(compressor.create_list_of_words())
    for i in range(9):
        print(compressor.key_generator())