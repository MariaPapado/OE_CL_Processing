import cv2
import os

# Paths
img_path = './bhe_data/images/18066132_84.tif'
label_path = './bhe_data/labels/18066132_84.txt'  # same name as image, YOLO format

# Load image
img = cv2.imread(img_path)
h, w = img.shape[:2]

# Read YOLO labels
with open(label_path, 'r') as f:
    for line in f:
        cls, x_center, y_center, box_w, box_h = map(float, line.strip().split())
        # Convert to pixel coords
        x1 = int((x_center - box_w / 2) * w)
        y1 = int((y_center - box_h / 2) * h)
        x2 = int((x_center + box_w / 2) * w)
        y2 = int((y_center + box_h / 2) * h)
        # Draw rectangle
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, str(int(cls)), (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 1)

print(img.shape)
cv2.imwrite('check_whole.png', img[:,:,[2,1,0]])
# Show image
#cv2.imshow('YOLO Boxes', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()