import cv2
import numpy as np
import os

def generate_test_image(width=300, height=200):
    """
    Generates a synthetic grayscale image with a horizontal intensity gradient.
    Intensity ranges from 0 (left) to 255 (right).
    """
    img = np.zeros((height, width), dtype=np.uint8)
    for i in range(height):
        img[i, :] = np.linspace(0, 255, width, dtype=np.uint8)
    return img

def calculate_and_save_intensity_range(image, min_intensity, max_intensity, output_dir="output", iteration_idx=0):
    """
    Calculates the percentage of pixels within the specified intensity range
    and saves a visual representation of the masked area.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Validate intensity range
    if min_intensity > max_intensity:
        print(f"Warning: min_intensity ({min_intensity}) is greater than max_intensity ({max_intensity}). Skipping this range.")
        return

    print(f"\n--- Processing Range: Min={min_intensity}, Max={max_intensity} ---")

    # Create a binary mask for pixels within the intensity range
    # cv2.inRange is inclusive [min_intensity, max_intensity]
    mask = cv2.inRange(image, min_intensity, max_intensity)

    # Count non-zero pixels (pixels within range)
    pixel_count_in_range = cv2.countNonZero(mask)
    total_pixels = image.size

    # Calculate percentage
    percentage = (pixel_count_in_range / total_pixels) * 100 if total_pixels > 0 else 0

    print(f"Total pixels: {total_pixels}")
    print(f"Pixels in range [{min_intensity}-{max_intensity}]: {pixel_count_in_range}")
    print(f"Percentage of pixels in range: {percentage:.2f}%")

    # Create a visual output: original image with selected pixels highlighted
    # Convert grayscale image to BGR for coloring
    display_img = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # Highlight pixels within the range with green color (BGR: [0, 255, 0])
    # The mask is 255 where pixels are in range, 0 otherwise.
    # We use boolean indexing to apply the color.
    display_img[mask == 255] = [0, 255, 0]

    # Define output file names
    output_filename = os.path.join(output_dir, f"result_{iteration_idx:02d}_min{min_intensity}_max{max_intensity}.png")
    mask_filename = os.path.join(output_dir, f"mask_{iteration_idx:02d}_min{min_intensity}_max{max_intensity}.png")

    # Save the processed image and the raw mask
    cv2.imwrite(output_filename, display_img)
    cv2.imwrite(mask_filename, mask)
    print(f"Visual output saved to: {output_filename}")
    print(f"Binary mask saved to: {mask_filename}")

if __name__ == "__main__":
    print("Starting Intensity Scope project...")

    # 1. Generate a synthetic test image
    print("Generating a synthetic grayscale test image...")
    test_image = generate_test_image()
    cv2.imwrite("output/generated_test_image.png", test_image)
    print("Generated test image saved to output/generated_test_image.png")

    # 2. Define a series of intensity ranges to simulate "trackbar" adjustments
    # These represent different user-defined thresholds
    intensity_ranges = [
        (0, 50),     # Dark pixels
        (100, 150),  # Mid-range pixels
        (200, 255),  # Bright pixels
        (75, 175),   # A wider mid-range
        (0, 255),    # All pixels
        (120, 120)   # A single intensity level
    ]

    # 3. Process each defined range and save results
    for i, (min_val, max_val) in enumerate(intensity_ranges):
        calculate_and_save_intensity_range(test_image, min_val, max_val, iteration_idx=i)

    print("\nIntensity Scope project finished. Check the 'output/' directory for results.")