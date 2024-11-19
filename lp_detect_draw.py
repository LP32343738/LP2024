import os
import cv2
import argparse

# Define the colors for the bounding boxes
COLORS = {
    "unreadable": (0, 0, 255),  # Red
    "readable": (0, 255, 0)     # Green
}

def draw_bounding_boxes(image_folder, label_folder, output_folder):
    # Create the output directory (if it doesn't exist)
    os.makedirs(output_folder, exist_ok=True)

    # Parse labels and draw bounding boxes
    for label_file in os.listdir(label_folder):
        if label_file.endswith('.txt'):
            # Corresponding image file
            image_file = os.path.splitext(label_file)[0] + ".jpg"  # Assuming images are in JPG format
            image_path = os.path.join(image_folder, image_file)
            label_path = os.path.join(label_folder, label_file)

            # Ensure the image exists
            if not os.path.exists(image_path):
                print(f"Image {image_file} not found, skipping...")
                continue

            # Load the image
            image = cv2.imread(image_path)
            if image is None:
                print(f"Failed to load {image_file}, skipping...")
                continue

            # Read the label file
            with open(label_path, "r") as file:
                for line in file.readlines():
                    # Parse each line in the label file, format: class x1 y1 x2 y2 x3 y3 x4 y4
                    parts = line.strip().split()
                    if len(parts) < 9:
                        print(f"Invalid label format in {label_file}, skipping line...")
                        continue

                    cls = parts[0]  # Class
                    points = list(map(int, parts[1:]))  # Bounding box coordinates (4 points)

                    # Determine if the class is "unreadable"
                    if cls == "_":
                        color = COLORS["unreadable"]  # Red bounding box
                        label_text = "_"
                    else:
                        color = COLORS["readable"]  # Green bounding box
                        label_text = cls  # Use the license plate number as the label

                    # Draw the bounding box (connect the 4 points)
                    pts = [(points[i], points[i + 1]) for i in range(0, len(points), 2)]
                    for j in range(len(pts)):
                        cv2.line(image, pts[j], pts[(j + 1) % len(pts)], color, 2)

                    # Annotate the class label
                    cv2.putText(image, label_text, (pts[0][0], pts[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

            # Save the processed image
            output_path = os.path.join(output_folder, image_file)
            cv2.imwrite(output_path, image)
            print(f"Processed and saved: {output_path}")

if __name__ == "__main__":
    # Define command-line arguments
    parser = argparse.ArgumentParser(description="Draw bounding boxes on images based on label files.")
    parser.add_argument("--image_folder", type=str, default="D:/LP2024/LP2024/LPD/train/images",
                        help="Path to the folder containing images. Default: 'D:/LP2024/LP2024/LPD/train/images'")
    parser.add_argument("--label_folder", type=str, default="D:/LP2024/LP2024/LPD/train/labels",
                        help="Path to the folder containing label files. Default: 'D:/LP2024/LP2024/LPD/train/labels'")
    parser.add_argument("--output_folder", type=str, default="D:/LP2024/LP2024/LPD/train/output_images",
                        help="Path to the folder to save output images. Default: 'D:/LP2024/LP2024/LPD/train/output_images'")

    # Parse the arguments
    args = parser.parse_args()

    # Call the main function with the provided arguments
    draw_bounding_boxes(args.image_folder, args.label_folder, args.output_folder)
