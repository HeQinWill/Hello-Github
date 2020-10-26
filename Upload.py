import os
import time

localtime = time.strftime("%Y%m%dT%H%M", time.localtime())
os.system('/usr/bin/git add /root/qinGitHub/Hello-Github')
os.system(f'/usr/bin/git commit -m autoUpload_{localtime}')
os.system('/usr/bin/git push')
