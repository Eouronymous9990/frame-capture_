import cv2
import os

def save_frames(v_path, f_folder):
    if not os.path.exists(f_folder):
        os.makedirs(f_folder)

    cap = cv2.VideoCapture(v_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        path = f"frame_{frame_count}.jpg"
        final_path = os.path.join(f_folder, path)
        cv2.imwrite(final_path, frame)

    cap.release()


farmes = r"C:\Users\zbook 17 g3\Downloads\test___.mp4"
folder = r"C:\Users\zbook 17 g3\Downloads\New folder (2)"
save_frames(farmes, folder)



