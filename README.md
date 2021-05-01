# svdcompression
Uses SVD matrix decomposition to create compressed media

### how it works
Single value decomposition yields decompositions of varying sizes based on the original matrix. Since there is no one way of organizing a bit-string of data into a two dimensional array, we can optimize the array to either 1). minimize the number of eigenvalues or 2). maximize the multiplicity of 0's. In doing this, the reduced decomposition will be of minimal size. Note that minimizing the number of eigenvalues will most likely require a larger domain or co-domain which might not be conducive to a smaller compressed size, so we will prioritize maximizing the multiplicity of 0's so that the decomposition is smaller and easier to store.  
Not all files will have a number of bits that fit the optimal matrix dimensions, so we will have to trim the beginning and/or the end and store those trimmings as smaller chunks of data. Whether or not those smaller chunks should also be compressed with SVD is up for investigation as SVD is not necessarily guaranteed to make them smaller if they are already small.  
Data from files will be converted as follows:  
```
                                         /-----------------------------------------------------------|--------------|--------------|--------------|--------------\
                                         | byte offset to next file (32 bits)                        | bit offset   | pre-trim     | len. sigma   | post-trim    |
                                         |                                                           | to next file | (8 bits)     | (8 bits)     | (8 bits)     |
                                         |                                                           | (8 bits)     |              |              |              |
                                         |-----------------------------------------------------------|--------------|--------------|--------------|--------------|
.-------------------.                    | row U (32 bits)                                           | col U (32 bits)                                           |  
| uncompressed file | == "compress" ==>  |-----------------------------------------------------------|-----------------------------------------------------------|
'-------------------'                    | row V  (32 bits)                                          | col V (32 bits)                                           |
                                         |-----------------------------------------------------------|-----------------------------------------------------------|
                                         |                                                                                                                       |
                                         | Data                                                                                                                  |
                                         |                                                                                                                       |
                                         \-----------------------------------------------------------------------------------------------------------------------/
```
Byte offset to next file will be 32 bits to encompass file sizes of decompressed size up to 1 gigabyte. This is accompanied by 8 bits of offset for offsets that are not in whole bytes.  
Pre-trim and post-trim do not have to be very long, but I'm not sure how long they should be yet. Most numbers can fit around a rectangle with little excess.  
The dimensions of U, sigma eigenvalues, and V(transpose) are then specified. To handle worst case scenario, the dimensions of U and V are also 32 bits (made to fit 1gb).  
The header will be of fixed size 

### todo
import file directory for compression  
compression multithreading to speed up for multiple files  
bit interpreter for decompressing new filetype .spd  
conversion from different file types (.png, .txt, .docx, etc.) to binary for compression and then binary back to the file type  
error correction bits  

### references
https://www.geeksforgeeks.org/python-pil-image-convert-method/  
https://www.pythonforthelab.com/blog/storing-binary-data-and-serializing/  
https://www.frankcleary.com/svdimage/  
https://mashable.com/2012/10/22/zip-files/  
https://blog.tensorflow.org/2020/02/matrix-compression-operator-tensorflow.html  
