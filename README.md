# intensity-scope

Analyzes grayscale images to report pixel percentage within user-defined intensity ranges.

## What it does

This project processes a static grayscale image, calculates the percentage of pixels that fall within a specified intensity range (0-255), and saves a visual output. The visual output is the original image with the pixels within the defined range highlighted in green.

Instead of interactive GUI trackbars (which are not supported in a headless environment), the script iterates through a predefined set of intensity threshold pairs, demonstrating how different ranges affect the calculated percentage and the masked image.

## How to run it

1.  **Install dependencies:**
    Make sure you have `pip` installed. Then run:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the script:**
    ```bash
    python main.py
    ```

The script will:
*   Generate a sample grayscale image (`generated_test_image.png`) in the `output/` directory.
*   Process this image using several predefined minimum and maximum intensity thresholds.
*   For each threshold pair, it will print the calculated pixel percentage to the console.
*   Save two output files for each threshold pair in the `output/` directory:
    *   `result_XX_minYY_maxZZ.png`: The original image with pixels in the specified range highlighted in green.
    *   `mask_XX_minYY_maxZZ.png`: A binary mask showing exactly which pixels were selected.

The script runs completely non-interactively and does not open any windows or require user input.