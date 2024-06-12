# IRM Image Compression Format

## Introduction
In this innovative approach, we are committed to developing a revolutionary new image compression format called IRM, which surpasses the limitations of traditional compression formats. By combining RLE, Huffman, and LZW compression techniques, the IRM format aims to offer efficient compression while preserving image quality, whether the image is binary, grayscale, or color.

Through practical and experimental simulations using Python, we will test the encoding and decoding processes for each compression method, allowing a thorough evaluation of the IRM format's performance. A user-friendly graphical interface will be developed to facilitate image compression into the .IRM format, featuring tools for measuring compression quality and compression ratio.

[Link to deployed site](https://ibtissamerrachidi.github.io/)

Authors:
- [Ibtissam Er Rachidi LinkedIn](https://www.linkedin.com/in/ibtissam-er-rachidi-44a257255/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

## Installation
To install and run this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/IbtissamErrachidi/alx-system_engineering-devops/blob/main
    cd 0x100-compression_interface
    ```
2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To use the IRM image compression tool, follow these steps:

1. Run the main script:
    ```bash
    python interface.py
    ```
2. Use the graphical interface to browse and compress images.

## Contributing
We welcome contributions to the IRM image compression project. Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Related Projects
Here are some related projects that might interest you:
- [Image Compression Using Huffman Coding](https://github.com/rajatdiptabiswas/image-compression-using-huffman-coding)
- [JPEG Compression Algorithm Implementation](https://github.com/nitin42/jpeg-compression)
- [LZW Image Compression](https://github.com/arthurprs/lzw-image-compression)
- [Image Compression with K-means](https://github.com/bibekkakati/image-compression-using-k-means)

## Screenshot
![Screenshot](https://github.com/IbtissamErrachidi/IbtissamErrachidi.github.io)

## Steps of the IRM Compression Algorithm
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

## User Interface Development
The user interface is crucial for the IRM format innovation. It should allow smooth and intuitive interaction, providing functionalities to load, view, compress, and save images. Key interface elements include buttons to browse files, display image information, start compression, show the compressed image, and clear displayed information.

## Development Language and Libraries
- **Python**: Main language for its efficiency and extensive standard library.
- **Matplotlib.pyplot**: For data visualization.
- **PyQt5**: For creating the graphical interface.
- **Numpy**: For handling multidimensional arrays.
- **sklearn.cluster.KMeans**: For color clustering.
- **PIL.Image**: For image processing.
- **os**: For interacting with the operating system.
- **OpenCV (cv2)**: For image and video processing.

## Development Tools
- **Jupyter Notebook**: For interactive data analysis and result communication.

## Interface Features
- **"Browse" Button**: Allows selecting an image to compress.
- **"Information" Button**: Displays details of the selected image.
- **"Start Compression" Button**: Initiates image compression.
- **"Show IRM Image File" Button**: Displays the compressed and decompressed image.
- **"Clear" Button**: Clears displayed information and images.

## Conclusion
This project proposes an innovative image compression format, IRM, combining the best practices of current compression techniques to overcome their limitations. The graphical user interface simplifies the use of this format, providing a comprehensive and functional solution for image compression.





## Project Story
Inspiration
The idea for the IRM image compression format stemmed from a desire to push the boundaries of existing compression techniques. I have always been fascinated by how data can be minimized without losing essential information. This curiosity drove me to explore various compression algorithms and eventually led to the creation of the IRM format. The goal was to develop a format that not only compresses efficiently but also maintains high image quality.

## Challenges
During the development process, I encountered several challenges. One of the most significant hurdles was optimizing the combination of RLE, Huffman, and LZW algorithms to work seamlessly together. Each algorithm has its strengths and weaknesses, and balancing them to achieve optimal performance required extensive experimentation and fine-tuning.

Another challenge was creating an intuitive graphical user interface. I wanted the interface to be user-friendly and accessible, even for those who might not be familiar with image compression techniques. Ensuring that the interface was both functional and aesthetically pleasing required careful design and iterative testing.

## Technical Details
The IRM format leverages the strengths of three powerful compression algorithms:

Run-Length Encoding (RLE): Efficiently compresses sequences of repeated values.
Huffman Encoding: Utilizes variable-length codes based on symbol frequency, ensuring minimal space usage.
Lempel-Ziv-Welch (LZW) Encoding: Builds a dictionary of sequences encountered in the data, enabling further compression.
By converting the image to the YCbCr color space, the IRM format takes advantage of the human eye's varying sensitivity to color and brightness. This allows for more efficient compression without perceptible loss of quality.

## Future Iterations
Looking ahead, I envision several improvements and additions to the IRM format. These include:

Enhanced Compression Algorithms: Exploring more advanced algorithms to further reduce file sizes.
Support for Animated Images: Extending the format to handle sequences of images, enabling efficient video compression.
Cloud Integration: Allowing users to compress and store images directly in the cloud for easy access and sharing.
Personal Reflection
This project has been a significant learning experience. It challenged me to deepen my understanding of data compression, improve my coding skills, and develop a practical application from scratch. Through this journey, I have gained a greater appreciation for the complexities of compression algorithms and the importance of clean, efficient code. I am excited to continue refining the IRM format and exploring new avenues for innovation.


