import os
import shutil
fromdir = "C:/Users/user/Downloads"
todir = "C:/Users/user/Downloadedpdf"
listofFiles = os.listdir(fromdir)
print(listofFiles)
for filename in listofFiles:
    name,extension = os.path.splitext(filename)
    print(name)
    print(extension)
    if extension == '':
        continue
    if extension in ['.pdf']:
        path1 = fromdir + '/' + filename
        path2 = todir + '/' + 'pdfFiles'
        path3 = todir + '/' + 'pdfFiles' + '/' + filename
        if os.path.exists(path2):
            shutil.move(path1, path3)
        else :
            os.makedirs(path2)
            shutil.move(path1, path3)