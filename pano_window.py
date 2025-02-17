import matplotlib.pyplot as plt
import cv2

class PanoWindow:
    def __init__(self, images_with_keypoints, panorama):
        self.images_with_keypoints = images_with_keypoints
        self.panorama = panorama

    def display_images(self):
        # Calculate the number of images to display (keypoints + panorama)
        total_images = len(self.images_with_keypoints) + 1  # Include panorama as well
        
        # Create a figure to display images
        fig, axes = plt.subplots(1, total_images, figsize=(15, 5))

        # Ensure axes is always iterable (even when there is only one subplot)
        if total_images == 1:
            axes = [axes]
        
        # Display the keypoint images
        for i, img in enumerate(self.images_with_keypoints):
            axes[i].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            axes[i].axis('off')
        
        # Display the panorama
        axes[-1].imshow(cv2.cvtColor(self.panorama, cv2.COLOR_BGR2RGB))
        axes[-1].axis('off')

        # Add a message to close the window
        plt.figtext(0.5, 0.01, "Press 'x' to close the window", ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
        
        # Define the close event for the window
        def close_window(event):
            if event.key == 'x':
                plt.close()
        
        fig.canvas.mpl_connect('key_press_event', close_window)
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()
