import cv2
import numpy as np
import sys

class CoinDetector:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
        self.gray = None
        self.result_image = None
        self.mask = None
        self.sure_bg = None
        self.sure_fg = None
        self.markers = None
        self.coin_count = 0

    def load_image(self):
        try:
            self.image = cv2.imread(self.image_path)
            if self.image is None:
                raise FileNotFoundError(f"Error: Unable to load image from {self.image_path}")
            self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except Exception as e:
            print(f"Exception occurred while loading image: {e}")

    def detect_coins(self):
        try:
            blurred = cv2.GaussianBlur(self.gray, (15, 15), 0)
            circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30, 
                                       param1=50, param2=30, minRadius=40, maxRadius=80)
            self.result_image = self.image.copy()
            self.mask = np.zeros_like(self.gray)
            
            if circles is not None:
                circles = np.uint16(np.around(circles))
                self.coin_count = len(circles[0])
                for i in circles[0, :]:
                    cv2.circle(self.result_image, (i[0], i[1]), i[2], (0, 255, 0), 2)
                    cv2.circle(self.mask, (i[0], i[1]), i[2], 255, -1)
        except Exception as e:
            print(f"Exception occurred during coin detection: {e}")

    def apply_segmentation(self):
        try:
            kernel = np.ones((3,3), np.uint8)
            self.sure_bg = cv2.dilate(self.mask, kernel, iterations=3)
            dist_transform = cv2.distanceTransform(self.mask, cv2.DIST_L2, 5)
            _, self.sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)
            self.sure_fg = np.uint8(self.sure_fg)
            unknown = cv2.subtract(self.sure_bg, self.sure_fg)
            _, self.markers = cv2.connectedComponents(self.sure_fg)
            self.markers = self.markers + 1
            self.markers[unknown == 255] = 0
            cv2.watershed(self.result_image, self.markers)
            self.result_image[self.markers == -1] = [0, 255, 0]
        except Exception as e:
            print(f"Exception occurred during segmentation: {e}")

    def process(self):
        self.load_image()
        self.detect_coins()
        self.apply_segmentation()
        return self.result_image, self.mask, self.sure_bg, self.sure_fg, self.markers, self.coin_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python detect_segment_coins.py <image_name>")
        sys.exit(1)
    
    image_name = sys.argv[1]
    image_path = f"./assets/{image_name}.jpeg"
    
    from window_logic import show_results
    show_results(image_name)
