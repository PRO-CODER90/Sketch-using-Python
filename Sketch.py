import cv2
import numpy as np
import os

def adjust_gamma(image, gamma=1.0):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in range(256)], dtype="uint8")
    return cv2.LUT(image, table)

def convert_to_sketch(input_path, output_folder=None, output_name="pencil_sketch.jpg", 
                    show_result=True, darkness_factor=1.3):
    """
    Convert image to pencil sketch and save to specified location
    
    Parameters:
    - input_path: Path to input image
    - output_folder: Folder to save sketch (None saves to current directory)
    - output_name: Name for output file
    - show_result: Whether to display the result
    - darkness_factor: Controls sketch darkness (1.0-2.0)
    """
    # Load image
    image = cv2.imread(input_path)
    
    # Check if image loaded properly
    if image is None:
        print(f"Error: Could not load image from {input_path}")
        return False
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert and blur
    inverted = 255 - gray
    blurred = cv2.GaussianBlur(inverted, (21, 21), sigmaX=3, sigmaY=3)
    inverted_blurred = 255 - blurred
    
    # Create sketch
    sketch = cv2.divide(gray, inverted_blurred, scale=256.0)
    
    # Apply darkness adjustment
    sketch_float = sketch.astype(np.float32) / 255.0
    darkened = np.clip(sketch_float * darkness_factor, 0, 1)
    final_sketch = (darkened * 255).astype(np.uint8)
    final_sketch = adjust_gamma(final_sketch, gamma=0.9)
    
    # Determine output path
    if output_folder:
        os.makedirs(output_folder, exist_ok=True)
        output_path = os.path.join(output_folder, output_name)
    else:
        output_path = output_name
    
    # Save image
    cv2.imwrite(output_path, final_sketch)
    print(f"Sketch saved to: {output_path}")
    
    # Show result if requested
    if show_result:
        cv2.imshow("Pencil Sketch", final_sketch)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    return True

# Example usage:
input_image = r"F:\My Projects\Sketch-Python\BG 6.jpg" # Path for your Image 
output_directory = r"F:\My Projects\Sketch-Python\Sketches" # path to save your Sketch or Leave it blank to save in current folder
output_filename = "Sketch.jpg"

# Convert and save with darkness adjustment
success = convert_to_sketch(
    input_path=input_image,
    output_folder=output_directory,
    output_name=output_filename,
    show_result=True,
    darkness_factor= 1.5  # Darker sketch
)

if not success:
    print("Conversion failed. Please check the input image path.")
