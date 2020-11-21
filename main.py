from filecompressor import FileCompressor
from filedecompressor import FileDecompressor

if __name__=="__main__":
    compressor = FileCompressor()
    # compressor.create_compressed_file()
    decompressor = FileDecompressor()
    decompressor.crete_dictionary()