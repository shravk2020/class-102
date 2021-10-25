import cv2
import dropbox
import time
import random

startTime = time.time()

def takeSnapShot():
    videoCapture = cv2.VideoCapture(0)
    result = True

    randNum = random.randint(0,100)

    while(result):
        ret, frame = videoCapture.read()
        imageName = 'Snapshot' + str(randNum) + '.png'
        cv2.imwrite(imageName, frame)

        startTime = time.time()
        result = False
    return(imageName)
    print('Snapshot taken')
    videoCapture.release()
    cv2.destroyAllWindows()

def upload_file(image):
    access_token = 'lJ3mGSaOnVgAAAAAAAAAAb9G0vmmMAu_iKUQdbBLhp-hIOGoASyeF9wmtCXbEOhV'
    dbx = dropbox.Dropbox(access_token)
    imgFile = image
    file_to = '/class102/' + str(imgFile)

    with open(imgFile, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print('file uploaded')
def main():
    while(True):
        if(time.time() - startTime >= 5):
            name = takeSnapShot()
            upload_file(name)
main()