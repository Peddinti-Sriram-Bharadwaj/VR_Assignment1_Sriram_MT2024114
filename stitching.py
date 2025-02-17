import cv2
import sys

def detect_and_draw_keypoints(image):
    # Use ORB (Oriented FAST and Rotated BRIEF) detector
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(image, None)
    
    # Draw the keypoints on the image
    image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, color=(0, 255, 0), flags=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
    
    return image_with_keypoints, keypoints

def stitch_images(image_paths):
    # Load the first image and detect keypoints
    img1 = cv2.imread(image_paths[0])
    img1_with_keypoints, keypoints1 = detect_and_draw_keypoints(img1)
    
    # Display the first image and its keypoints
    cv2.imshow("Image 1 with Keypoints", img1_with_keypoints)
    
    # Loop through the remaining images and stitch them iteratively
    for image_path in image_paths[1:]:
        img2 = cv2.imread(image_path)
        img2_with_keypoints, keypoints2 = detect_and_draw_keypoints(img2)
        
        # Display the second image and its keypoints
        cv2.imshow(f"Image {image_path} with Keypoints", img2_with_keypoints)
        
        # Stitch the two images together
        stitcher = cv2.Stitcher_create()
        status, stitched_image = stitcher.stitch([img1, img2])
        
        if status == cv2.Stitcher_OK:
            img1 = stitched_image  # Update img1 to the stitched result
        else:
            print(f"Error stitching {image_path}")
            break
    
    return img1

def main():
    # Get image names from command line arguments
    if len(sys.argv) < 2:
        print("Please provide image names as arguments.")
        return
    
    image_paths = [f"./assets/{name}.jpeg" for name in sys.argv[1:]]
    
    # Stitch images and get the panorama
    panorama = stitch_images(image_paths)
    
    # Display the final panorama
    cv2.imshow("Panorama", panorama)
    
    # Save the final panorama image
    cv2.imwrite('./assets/panorama.jpeg', panorama)
    print("Panorama saved as './assets/panorama.jpeg'")
    
    # Wait until 'x' is pressed to close the windows
    while True:
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
