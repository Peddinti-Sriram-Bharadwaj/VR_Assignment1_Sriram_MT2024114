import cv2
import sys
from pano_window import PanoWindow

class ImageLoader:
    """Responsible for loading and resizing images."""
    
    def __init__(self, image_paths, resize_factor=0.4):
        self.image_paths = image_paths
        self.resize_factor = resize_factor
        self.images = []

    def load_images(self):
        """Loads and resizes the images from the provided paths."""
        for path in self.image_paths:
            img = cv2.imread(path)
            if img is None:
                print(f"Error reading image {path}")
                continue
            img_resized = cv2.resize(img, (0, 0), fx=self.resize_factor, fy=self.resize_factor)
            self.images.append(img_resized)

        if not self.images:
            print("No valid images were loaded.")
            sys.exit(1)
        
        print(f"Loaded {len(self.images)} images.")

class ImageStitcher:
    """Responsible for stitching images together into a panorama."""
    
    def __init__(self, images):
        self.images = images

    def stitch_images(self):
        """Stitches the images using OpenCV's Stitcher."""
        stitcher = cv2.Stitcher_create()
        status, panorama = stitcher.stitch(self.images)
        
        if status != cv2.Stitcher_OK:
            print("Stitching failed!")
            return None
        print("Stitching successful!")
        return panorama

class PanoramaSaver:
    """Handles saving the stitched panorama."""
    
    def __init__(self, panorama, save_path='./assets/panorama.jpeg'):
        self.panorama = panorama
        self.save_path = save_path

    def save(self):
        """Saves the stitched panorama to a file."""
        cv2.imwrite(self.save_path, self.panorama)
        print(f"Panorama saved as '{self.save_path}'.")

class StitchingApp:
    """Main application that coordinates the stitching process."""
    
    def __init__(self, image_paths):
        self.image_paths = image_paths

    def run(self):
        # Load images
        loader = ImageLoader(self.image_paths)
        loader.load_images()

        # Stitch images
        stitcher = ImageStitcher(loader.images)
        panorama = stitcher.stitch_images()
        if panorama is None:
            return

        # Save panorama
        saver = PanoramaSaver(panorama)
        saver.save()

        # Display images
        pano_window = PanoWindow(loader.images, panorama)
        pano_window.display_images()

def main():
    # Collect image paths from command line arguments
    if len(sys.argv) < 2:
        print("Usage: python stitching.py <image1> <image2> ...")
        sys.exit(1)

    image_paths = [f"./assets/{name}.jpeg" for name in sys.argv[1:]]
    
    # Run the application
    app = StitchingApp(image_paths)
    app.run()

if __name__ == "__main__":
    main()
