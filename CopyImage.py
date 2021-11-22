import shutil

def CopyImg(path):
    dest = 'C:\\Users\\Asus\\PycharmProject\\PycharmTest\\Project\\ImagesAttendance'
    shutil.copy(path, dest)

# CopyImg(path,name)