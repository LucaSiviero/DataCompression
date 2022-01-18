from lzw_impl import LZW
import os
import utils


here = os.path.dirname(os.path.abspath(__file__))
unc = os.path.join(here, "huffman.txt")
com = os.path.join(here, "lzw.bin")

l = LZW()

l.compress(unc, com)

print(utils.compression_ratio_from_file(unc, com))
