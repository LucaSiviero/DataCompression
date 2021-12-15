from huffman import HuffmanCoding

#TODO costruttore

class Huffman:
    path = "Huffman\\test.txt"

    h = HuffmanCoding(path)

    output_path = h.compress()
    print("Compressed file path: " + output_path)

    decom_path = h.decompress(output_path)
    print("Decompressed file path: " + decom_path)