from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)
x = 0
for file_list in drive.ListFile():
  print('Received %s files from Files.list()' % len(file_list)) # <= 10
  for file1 in file_list:
      if '.jpg' in file1['title']:
          file6 = drive.CreateFile({'id': file1['id']})
          file6.GetContentFile('images' + str(x) + '.jpg')
          x += 1
