

import cv2
import os
import argparse
import sys

# Define and parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument('--imgdir', help='Folder to save images in (will be created if it doesn\'t exist already',
                   default='image')
parser.add_argument('--resolution', help='Desired camera resolution in WxH.',
                   default='1920x1080')

args = parser.parse_args()
dirname = args.imgdir
if not 'x' in args.resolution:
    print('Please specify resolution as WxH. (example: 1920x1080)')
    sys.exit()
imW = int(args.resolution.split('x')[0])
imH = int(args.resolution.split('x')[1])

# Create output directory if it doesn't already exist
cwd = os.getcwd()
dirpath = os.path.join(cwd,dirname)
if not os.path.exists(dirpath):
    os.makedirs(dirpath)

# If images already exist in directory, increment image number so existing images aren't overwritten
# Example: if 'image-0.jpg' through 'image-10.jpg' already exist, imnum will be incremented to 11
basename = dirname
imnum = 1
img_exists = True

while img_exists:
    imname = dirname + '-' + str(imnum) + '.jpg'
    impath = os.path.join(dirpath, imname)
    if os.path.exists(impath):
        imnum = imnum + 1
    else:
        img_exists = False

# Initialize webcam
cap = cv2.VideoCapture(0)
ret = cap.set(3, imW)
ret = cap.set(4, imH)

# Initialize display window
winname = 'Press \"p\" to take a picture and Press \"q\" to exit!'
cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
cv2.moveWindow(winname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

print('Press p to take a picture. Pictures will automatically be saved in the %s folder.' % dirname)
print('Press q to quit.')

while True:
    hasFrame, frame = cap.read()
    cv2.putText(frame, f'Images Taken: {imnum - 1}', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow(winname,frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('p'):
        #Take a picture!
        filename = dirname + '_' + str(imnum) + '.jpg'
        savepath = os.path.join(dirpath, filename)
        cv2.imwrite(savepath, frame)
        print('Picture taken and saved as %s' % filename)
        imnum = imnum + 1

cv2.destroyAllWindows()
cap.release()