
# Coin Detection and Panorama Creation

This repository contains Python scripts to perform **coin detection and segmentation** and **panorama creation**. The goal of the project is to detect coins in images, segment them, and then create a panorama by stitching multiple images together.

## Requirements

- Python 3.x
- OpenCV
- Matplotlib
- NumPy

You can set up the required environment using the `environment.yml` file. To create the environment, run:

```bash
conda env create -f environment.yml
```

Activate the environment:

```bash
conda activate images
```

## Task 1: Coin Detection and Segmentation

This script detects and segments coins in a given image. It identifies coins based on their circular shape and segments the image using watershed segmentation.

### Steps:
1. **Load Image**: The script loads an image of coins.
2. **Grayscale Conversion**: The image is converted to grayscale to simplify processing.
3. **Coin Detection**: The Hough Circle Transform is applied to detect circular objects in the image.
4. **Segmentation**: Watershed segmentation is used to separate the detected coins from the background.
5. **Display and Save Results**: The results are displayed and saved in the `outputs` folder.

### Running the Script

To run the **coin detection** script, use the following command:

```bash
python coins.py <image_name>
```

Example:

```bash
python coins.py coins1
```

Where `coins1.jpeg` is the image file located in the `assets` folder. 

### Results

The output will include:
- **Detected Coins Mask**: The coins are detected and highlighted in the mask.
- **Segmentation Result**: The coins are segmented and labeled.
- **Coin Count**: The number of coins detected in the image.

### Example Output:
- **coins_detection1.jpeg**: Detected coins in the first image.
- **coins_detection2.jpeg**: Detected coins in the second image.

---

## Task 2: Panorama Creation

This script creates a panorama by stitching together multiple images using keypoint matching and image alignment.

### Steps:
1. **Load Images**: The script loads multiple images to be stitched into a panorama.
2. **Keypoint Detection**: ORB (Oriented FAST and Rotated BRIEF) keypoints are detected in each image.
3. **Image Stitching**: The images are stitched using OpenCV's Stitcher class.
4. **Save and Display Panorama**: The final panorama is saved in the `outputs` folder.

### Running the Script

To run the **panorama creation** script, use the following command:

```bash
python stitching.py <image1> <image2> ...
```

Example:

```bash
python stitching.py key1 key2 key3
```

Where `key1`, `key2`, etc., are the image files located in the `assets` folder. The resulting panorama will be saved in the `outputs` folder as `panorama1.jpeg`.

---

## Folder Structure

```
├── __pycache__
├── assets
│   ├── coins_image1.jpeg
│   ├── coins_image2.jpeg
│   └── ...
├── results
│   ├── coin_detection1.jpeg
│   ├── coin_detection2.jpeg
│   └── panoroma1.jpeg
├── README.md
├── coins.py
├── environment.yml
├── pano_window.py
├── stitching.py
```

## Visual Results

### Task 1: Coin Detection and Segmentation

The following are the results from coin detection and segmentation:

- **Coins Detection 1**: Detected coins in the first image
  ![Coins Detection 1](./results/coin_detection1.jpeg)

- **Coins Detection 2**: Detected coins in the second image
  ![Coins Detection 2](./results/coin_detection2.jpeg)

### Task 2: Panorama Creation

The following is the final panorama created from the input images:

- **Panorama 1**: The stitched panorama from multiple images
  ![Panorama 1](./results/panoroma1.jpeg)

---

## Conclusion

This project demonstrates a basic script for detecting and segmenting coins and stitching images to create a panorama. The methods used include the Hough Circle Transform for coin detection and watershed segmentation for coin segmentation. For panorama creation, ORB keypoints and OpenCV's Stitcher class were used to combine images into a seamless panorama.
