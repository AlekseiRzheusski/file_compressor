from filecompressor import FileCompressor
from filedecompressor import FileDecompressor
import logging

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    compressor = FileCompressor()
    compressor.create_compressed_file()
    decompressor = FileDecompressor()
    decompressor.create_dictionary()
