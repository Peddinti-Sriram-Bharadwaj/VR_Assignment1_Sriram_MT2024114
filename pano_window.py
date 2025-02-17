import cv2
import matplotlib.pyplot as plt

class ImageWindow:
    def __init__(self, images, keypoints, panorama):
        self.images = images
        self.keypoints = keypoints
        self.panorama = panorama
        self.fig, self.axs = plt.subplots(2, 3, figsize=(15, 10))  # 2x3 grid
        self.display_images()

    def display_images(self):
        for i, img in enumerate(self.images):
            self.axs[0, i].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            self.axs[0, i].set_title(f"Image {i+1}")
            self.axs[0, i].axis('off')

        # Draw keypoints on images
        for i, (img, kp) in enumerate(zip(self.images, self.keypoints)):
            img_with_kp = cv2.drawKeypoints(img, kp, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
            self.axs[1, i].imshow(cv2.cvtColor(img_with_kp, cv2.COLOR_BGR2RGB))
            self.axs[1, i].set_title(f"Keypoints {i+1}")
            self.axs[1, i].axis('off')

        # Display panorama
        self.axs[1, 2].imshow(cv2.cvtColor(self.panorama, cv2.COLOR_BGR2RGB))
        self.axs[1, 2].set_title("Panorama")
        self.axs[1, 2].axis('off')

        self.fig.canvas.mpl_connect('key_press_event', self.on_key)
        plt.tight_layout()
        plt.show()

    def on_key(self, event):
        if event.key == 'x':
            plt.close(self.fig)
