
# Pencil Sketch Converter using OpenCV

## 🎯 Project Overview
This Python script converts a regular image into a **realistic pencil sketch** using OpenCV. It applies grayscale conversion, image inversion, Gaussian blur, and blending techniques to simulate a hand-drawn pencil effect.

## 🛠 Features
- Converts any `.jpg`/`.png` image into a pencil sketch.
- Includes contrast adjustment using gamma correction.
- User-friendly and customizable.
- Works with local image paths.

## 🖥 Requirements
- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)

### Install dependencies:
```bash
pip install opencv-python numpy
```

## 🚀 How to Use

1. **Prepare your input image** and place it in the same folder or specify the full path.

2. **Run the script:**
```bash
python Sketch.py
```

3. **Edit the following line** in the script to point to your image file:
```python
image = cv2.imread("input.jpg")  # Replace with your image path
```

4. **Output:** A new image file named `pencil_sketch.jpg` will be saved in the same directory.

## 📁 Output
- File: `pencil_sketch.jpg`
- Format: Grayscale image mimicking a pencil sketch

## 💡 Customization
You can change:
- **Blur strength:** Adjust the Gaussian kernel size `(21, 21)` and `sigmaX`.
- **Gamma value:** Modify `gamma=0.9` for darker or lighter output.
