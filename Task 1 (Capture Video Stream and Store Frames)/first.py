import cv2
import time
import os

# Settings
frames = []
interval = 2  # seconds between each frame (Frame Rate)
num_frames_to_capture = 10  # total number of frames to capture
save_dir = "captured_frames"

# Create folder to save frames
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Open webcam
cap = cv2.VideoCapture(0)
last_capture_time = time.time()
frame_id = 0

while frame_id < num_frames_to_capture:
    ret, frame = cap.read()
    if not ret:
        break

    # Show live video
    cv2.imshow("Capturing...", frame)

    current_time = time.time()
    if current_time - last_capture_time >= interval:
        last_capture_time = current_time

        # Control Image Quality
        resized_frame = cv2.resize(frame, (224, 224))
        frames.append(resized_frame)

        # Save frame to file
        filename = os.path.join(save_dir, f"frame_{frame_id}.jpg")
        cv2.imwrite(filename, resized_frame)
        print(f"Captured and saved: {filename}")

        frame_id += 1

    # Let user quit early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()

# Show array content summary
print(f"\nTotal Frames Captured: {len(frames)}")
for i, f in enumerate(frames):
    print(f"Frame {i} shape: {f.shape}")
