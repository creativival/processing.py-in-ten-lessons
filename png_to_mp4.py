import sys
import cv2

VIDEO_FILE_NAME = 'spirograph.mp4'
VIDEO_SIZE = [1000, 1000]
MIN_FRAME = 360
MAX_FRAME = 540

# encoder(for mp4)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# output file name, encoder, fps, size(fit to image size)
video = cv2.VideoWriter(
    'output_videos/' + VIDEO_FILE_NAME,
    fourcc,
    20.0,
    (VIDEO_SIZE[0], VIDEO_SIZE[1])
)

if not video.isOpened():
    print("can't be opened")
    sys.exit()

for i in range(MIN_FRAME, MAX_FRAME + 1):
    num = '{0:06d}'.format(i)
    file_name = 'frames/{}.png'.format(num)
    img = cv2.imread(file_name)

    # can't read image, escape
    if img is None:
        print("can't read")
        break

    # add
    video.write(img)
    print(i)

video.release()
print('written')
