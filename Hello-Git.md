cd C:\Git
git	init
git status
git	add Hello Git.md
git	rm	--cached
git	commit	-m	'first	commit'
git	log
git	branch
git	branch	a
git	checkout	a
git	checkout	-b	a
git	merge	a
git	branch	-d
git	branch	-d	a
git	branch	-D
git	branch	-D	a
git	tag
git	tag	v1.0
git	checkout	v1.0

我是没明白设置vim编辑器的作用是什么，尝试设置成vs code又不知设置的是否正确

- Windows的cmd中cd指令无法转换路径怎么办_百度经验 http://jingyan.baidu.com/article/656db918ec8211e381249ce8.html
- git中手动删除的文件如何在git中删除 - LBJ - 博客频道 - CSDN.NET http://blog.csdn.net/xiaoyuanzhiying/article/details/44085135
- Git如何永久删除文件(包括历史记录) - shines77 - 博客园 http://www.cnblogs.com/shines77/p/3460274.html
# 强力推荐
- git学习笔记 - 简书 http://www.jianshu.com/p/e2a15d01284c

将用户名下的gitconfig
>[core]
>	editor = Code
删除

- 用git commit提交版本时没有加-m,会进入vim,如何写入提交说明然后退出 - YChLu的回答 - SegmentFault https://segmentfault.com/q/1010000005979356/a-1020000005980392
>按i然后写入，写入后按esc键，然后输入:wq

- Commit message 和 Change log 编写指南 - 阮一峰的网络日志 http://www.ruanyifeng.com/blog/2016/01/commit_message_change_log.html
- 写出好的 commit message · Ruby China http://ruby-china.org/topics/15737