### Introduction

In this innovative approach, we are committed to developing a revolutionary new image compression format called IRM, which surpasses the limitations of traditional compression formats. By combining RLE, Huffman, and LZW compression techniques, the IRM format aims to offer efficient compression while preserving image quality, whether the image is binary, grayscale, or color.

Through practical and experimental simulations using Python, we will test the encoding and decoding processes for each compression method, allowing a thorough evaluation of the IRM format's performance. A user-friendly graphical interface will be developed to facilitate image compression into the .IRM format, featuring tools for measuring compression quality and compression ratio.

### Steps of the IRM Compression Algorithm

1. **Preprocessing**: Extract pixel matrices from the RGB image.
2. **Color Space Conversion**: Convert the image to YCbCr color space for better compression.
3. **Palette Creation**: Use K-means clustering to create an efficient color palette.
4. **Mapping**: Map each pixel to a color in the palette.
5. **Image Subdivision**: Divide the image into 8x8 pixel blocks.
6. **Subsampling**: Reduce the values of the blocks without modification.
7. **Matrix Traversal**: Vectorize the matrix to maximize repetitions for RLE encoding.
8. **RLE Encoding**: Reduce data size without losing information.
9. **Huffman Encoding**: Efficiently represent symbols based on their frequency.
10. **LZW Encoding**: Final encoding using a code table, resulting in the compressed file with header information for decompression.

### User Interface Development

The user interface is crucial for the IRM format innovation. It should allow smooth and intuitive interaction, providing functionalities to load, view, compress, and save images. Key interface elements include buttons to browse files, display image information, start compression, show the compressed image, and clear displayed information.

### Development Language and Libraries

- **Python**: Main language for its efficiency and extensive standard library.
- **Matplotlib.pyplot**: For data visualization.
- **PyQt5**: For creating the graphical interface.
- **Numpy**: For handling multidimensional arrays.
- **sklearn.cluster.KMeans**: For color clustering.
- **PIL.Image**: For image processing.
- **os**: For interacting with the operating system.
- **OpenCV (cv2)**: For image and video processing.

### Development Tools

- **Jupyter Notebook**: For interactive data analysis and result communication.

### Interface Features

- **"Browse" Button**: Allows selecting an image to compress.
- **"Information" Button**: Displays details of the selected image.
- **"Start Compression" Button**: Initiates image compression.
- **"Show IRM Image File" Button**: Displays the compressed and decompressed image.
- **"Clear" Button**: Clears displayed information and images.

### Conclusion

This project proposes an innovative image compression format, IRM, combining the best practices of current compression techniques to overcome their limitations. The graphical user interface simplifies the use of this format, providing a comprehensive and functional solution for image compression.
