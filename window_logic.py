import cv2
import matplotlib.pyplot as plt
import sys
from coins import CoinDetector

def show_results(image_name):
    image_path = f"./assets/{image_name}.jpeg"
    detector = CoinDetector(image_path)
    result_image, mask, sure_bg, sure_fg, markers, coin_count = detector.process()
    
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    fig.suptitle(f'Coins Detected: {coin_count}', fontsize=16, fontweight='bold')
    
    axes[0, 0].imshow(cv2.cvtColor(detector.image, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title("Original Image")
    
    axes[0, 1].imshow(detector.gray, cmap='gray')
    axes[0, 1].set_title("Grayscale Image")
    
    axes[0, 2].imshow(mask, cmap='gray')
    axes[0, 2].set_title("Detected Coins Mask")
    
    axes[1, 0].imshow(sure_bg, cmap='gray')
    axes[1, 0].set_title("Sure Background")
    
    axes[1, 1].imshow(sure_fg, cmap='gray')
    axes[1, 1].set_title("Sure Foreground")
    
    axes[1, 2].imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
    axes[1, 2].set_title(f"Final Result (Coins: {coin_count})")
    
    for ax in axes.flat:
        ax.axis('off')
    
    plt.figtext(0.5, 0.01, "Press 'x' to close the window", ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
    
    def close_window(event):
        if event.key == 'x':
            plt.close()
    
    fig.canvas.mpl_connect('key_press_event', close_window)
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python window_logic.py <image_name>")
        sys.exit(1)
    show_results(sys.argv[1])
