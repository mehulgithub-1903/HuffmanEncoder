from huffman import HuffmanCoding
import sys
path=input("Enter the path of file :")
x=input("Enter 'c' to compress and 'd' to decompress:")
if(x=='c'):
    h = HuffmanCoding(path)
    output_path = h.compress()
    print("Compressed file path: " + output_path)

else:
    h = HuffmanCoding(path)
    output_path = h.compress()
    decom_path = h.decompress(output_path)
    print("Decompressed file path: " + decom_path)
