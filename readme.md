### Python Implementaion of Huffman Coding

Consists **compress** and **decompress** function.


#### Testing / Running the program

1. Save / Clone the above repository
2. The repository consists of a sample text file of size 2MB and 4MB
3. Run the python code `useHuffman.py` to compress & decompress the given sample file. For eg. open terminal and run `python3 useHuffman.py`
4.Then choose the option 'c' to compress or 'd' to decompress
5. The above command will perform compression and decompression on the sample.txt file present here. Both the compressed and decompressed file will be present at the same location.


To run the code for compression of any other text file, edit the `path` variable in the `useHuffman.py` file.


For now, the *decompress()* function is to be called from the same object from which the *compress()* function was called. (as the encoding information is stored in the data members of the object only) 