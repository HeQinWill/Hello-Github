- 【干货】用Git在Visual Studio Code内进行版本控制[指导] - SDK.CN - 中国领先的开发者服务平台 https://www.sdk.cn/news/4041

- vscode中使用git - 简书 http://www.jianshu.com/p/e9dd2849cfb0

- vscode集成git bash - 104gogo - SegmentFault https://segmentfault.com/a/1190000008185938

- git commit命令的使用与git默认编辑器的修改 - longxiaowu的专栏 - 博客频道 - CSDN.NET http://blog.csdn.net/longxiaowu/article/details/24017181

> 1、Git commit
此时是进入GUN nano编辑器。在这里可以添加你的commit imformation 然后ctrl+o,回车保存，再ctrl+x退出。
因为对Nano编辑器很不熟悉，在这里我想将默认编辑器改为vim。打开.git/config文件，在core中添加 editor=vim即可。
或者运行命令 git config –global core.editor vim 修改更加方便。
2、git commit -a
把所有add了的文件都加入commit，然后进入编辑器编辑commit信息。
3、git commit -m  “commit imformation”
直接在后面添加commit 信息然后提交commit，与gitcommit相比快捷方便，但是就是commit信息格式无法控制
4、git commit --amend 
修改最后一次commit的信息。

- 在vscode中使用Git - manasXX - 博客园 http://www.cnblogs.com/ashidamana/p/6122619.html

- Visual Studio Code 使用Git进行版本控制 - 玄魂 - 博客园 http://www.cnblogs.com/xuanhun/p/6019038.html?utm_source=tuicool&utm_medium=referral