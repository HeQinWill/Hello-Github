import os
import time

localtime = time.strftime("%Y%m%dT%H%M", time.localtime())
os.system('git add /root/qinGitHub/Hello-Github')
os.system(f'git commit -m autoUpload_{localtime}')
os.system('git push')
