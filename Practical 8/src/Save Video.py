# Python program to save a
# video using OpenCV
import cv2

video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Error reading video file")

frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)

result = cv2.VideoWriter('../data/saved_vid.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)

while (True):
    ret, frame = video.read()

    if ret:

        # Write the frame into the
        # file 'filename.avi'
        result.write(frame)

        # Display the frame
        # saved in the file
        cv2.imshow('Frame', frame)

        # Press S on keyboard
        # to stop the process
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

    # Break the loop
    else:
        break

# When everything done, release
# the video capture and video
# write objects
video.release()
result.release()

# Closes all the frames
cv2.destroyAllWindows()

print("The video was successfully saved")
