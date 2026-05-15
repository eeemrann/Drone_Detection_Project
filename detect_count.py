
from ultralytics import YOLO
import cv2
import argparse

def detect_and_count(model_path, image_path, output_path="output.jpg", conf=0.25):
    model = YOLO(model_path)
    results = model(image_path, conf=conf)

    img = cv2.imread(image_path)

    human_count = 0
    car_count = 0

    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        score = float(box.conf[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        if cls_id == 0:
            label = f"Human {score:.2f}"
            color = (0, 255, 0)
            human_count += 1
        else:
            label = f"Car {score:.2f}"
            color = (0, 0, 255)
            car_count += 1

        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(img, label, (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv2.putText(img, f"Humans: {human_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.putText(img, f"Cars: {car_count}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.imwrite(output_path, img)
    print(f"Humans: {human_count}, Cars: {car_count}")
    print(f"Saved output to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, help="Path to YOLO model")
    parser.add_argument("--image", required=True, help="Path to input image")
    parser.add_argument("--output", default="output.jpg", help="Path to save output image")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold")
    args = parser.parse_args()

    detect_and_count(args.model, args.image, args.output, args.conf)
