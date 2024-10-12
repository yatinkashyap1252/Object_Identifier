import cv2

# Open the camera (0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Press 'q' to quit or 'c' to capture an image.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the resulting frame
    cv2.imshow('Camera Feed', frame)

    # Wait for a key press
    key = cv2.waitKey(1) & 0xFF

    # If 'q' is pressed, exit the loop
    if key == ord('q'):
        print("Exiting...")
        break

    # If 'c' is pressed, save the current frame as an image
    if key == ord('c'):
        cv2.imwrite('captured_image.jpg', frame)
        print("Image captured and saved as 'captured_image.jpg'.")

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
