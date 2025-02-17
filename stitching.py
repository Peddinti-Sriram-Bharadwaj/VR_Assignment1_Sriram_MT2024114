import cv2
import numpy as np
import sys
from pano_window import ImageWindow

class ImageStitcher:
    def __init__(self, *images):
        self.images = [cv2.imread(f"./assets/{img}.jpeg") for img in images]
        self.sift = cv2.SIFT_create()  # SIFT keypoint detector
        self.matcher = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

    def detect_keypoints(self):
        keypoints = []
        descriptors = []
        for img in self.images:
            kp, des = self.sift.detectAndCompute(img, None)
            keypoints.append(kp)
            descriptors.append(des)
        return keypoints, descriptors

    def match_keypoints(self, descriptors):
        matches = []
        for i in range(len(descriptors) - 1):
            match = self.matcher.match(descriptors[i], descriptors[i+1])
            matches.append(match)
        return matches

    def stitch_images(self, keypoints, descriptors, matches):
        img1, img2 = self.images[0], self.images[1]
        kp1, kp2 = keypoints[0], keypoints[1]
        des1, des2 = descriptors[0], descriptors[1]
        
        # Get the matched points
        pts1 = np.float32([kp1[m.queryIdx].pt for m in matches[0]]).reshape(-1, 1, 2)
        pts2 = np.float32([kp2[m.trainIdx].pt for m in matches[0]]).reshape(-1, 1, 2)
        
        # Find homography matrix
        M, _ = cv2.findHomography(pts2, pts1, cv2.RANSAC)
        
        # Stitch images
        result = cv2.warpPerspective(img2, M, (img1.shape[1] + img2.shape[1], img1.shape[0]))
        result[0:img1.shape[0], 0:img1.shape[1]] = img1
        return result

def main():
    if len(sys.argv) < 3:
        print("Please provide image names like 'img1' 'img2'.")
        sys.exit(1)

    images = sys.argv[1:]
    stitcher = ImageStitcher(*images)
    keypoints, descriptors = stitcher.detect_keypoints()
    matches = stitcher.match_keypoints(descriptors)
    panorama = stitcher.stitch_images(keypoints, descriptors, matches)

    # Save the panorama
    cv2.imwrite('./output/panorama.jpeg', panorama)
    print("Panorama saved as 'panorama.jpeg'.")

    # Display images and panorama in the window
    window = ImageWindow([cv2.imread(f"./assets/{img}.jpeg") for img in images], keypoints, panorama)

if __name__ == "__main__":
    main()
