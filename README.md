# PyMusic

解释：[pygame](http://www.pygame.org)+music, writed by [Python](https://www.python.org)

之前发布了自己写的小程序：[百度随心听](http://fm.baidu.com/)音乐播放器的一些效果图

你可以去到这里再次看看效果：

[pygame系列_百度随心听_完美的UI设计](http://www.cnblogs.com/hongten/p/hongten_pygame_pymusic.html)

这个程序的灵感来自于[百度随心听](http://fm.baidu.com/)
![Example](https://github.com/Hongten/PyMusic/blob/master/images/o_hongten_pygame_fm.png)

# 说明

       动作按钮全部是画出来的，没有用到任何图片

       用到图片的只有：背景，歌手图片，作者图片

经过一个阶段的调试，现在算是可以拿上台面和大家交流

# UI
![Example](https://github.com/Hongten/PyMusic/blob/master/images/o_hongten_pygame_pymusic1.png)

# 正在播放
![Example](https://github.com/Hongten/PyMusic/blob/master/images/o_hongten_pygame_pymusic2.png)

# 喜欢效果
![Example](https://github.com/Hongten/PyMusic/blob/master/images/o_hongten_pygame_pymusic3.png)

# 删除效果
![Example](https://github.com/Hongten/PyMusic/blob/master/images/o_hongten_pygame_pymusic4.png)

# 下一曲效果
![Example](https://github.com/Hongten/PyMusic/blob/master/images/o_hongten_pygame_pymusic5.png)

# 暂停/播放效果
![Example](https://github.com/Hongten/PyMusic/blob/master/images/o_hongten_pygame_pymusic6.png)

# 功能介绍

A.四个按钮介绍

 1.完成停止，播放音乐功能

 2.喜欢/不喜欢当前所播放的音乐

 3.删除当前所播放的音乐(物理环境下不会删除，删除的是内存中的)

 4.下一曲

 5.当鼠标经过按钮的时候，按钮颜色会变化

B.状态栏(最下面)

 1.显示所有歌曲数(AllSongs)

 2.当前播放的歌曲是第只歌曲

 3.当前音量(范围：0 - 10)

 4.音量的图形显示(这里没有用到图片，而是系统画出来的:-))

 5.我的邮箱信息：hongtenzone@foxmail.com

C.右下角

 1.当鼠标移动到黄色圆区域，会展示出我的相片和'Yes,You are Luck:)'字样

  鼠标一开的时候会自动隐藏（我想接触过android系统手机的的朋友，可能有这样的经历，在工具里面有一个地方

  当点击三下的时候，会出现android里面的一副图片....对我这里的灵感来自于这里ll）

# 思路

下面我说说我做的思路吧

我想有一部分朋友会喜欢的...:)

首先，主题功能是音乐播放，那么我们就应该实现这个音乐播放的功能

哈哈，这个灵感来自于我之前写的小游戏：

[pygame系列_小球完全弹性碰撞游戏_源码下载](http://www.cnblogs.com/hongten/p/hongten_pygame_pong.html)

在这个游戏中，我实现了音乐的播放，于是乎我就想在音乐播放上面做一些文章...

接下来是程序PyMusic的主题界面需要考虑，我个人喜欢听歌...百度音乐，百度随心听都是常去的地方..

百度随心听的界面设计简洁，很适合我的风格...所以我选择了百度随心听..

于是乎我看是看百度随心听的代码...一不小心被我大概看明白了按钮之间的逻辑....

一时间，头脑中出现了PyMusic的原型....

为什么不做一个呢？我就这样问着我自己，慢慢在脑海中呈现PyMusic的原型...

然后开始动笔，把pyMusic的原型在纸上画了出来....

画好了，就开始分析...(这个过程有一点长..)

然后把原型中的物体（按钮，图片加载..）一个一个的实现..

最后加上我的小自信..呵呵，成啦..

# 试一试

如果你也想在你的电脑上面运行该程序，你应该遵循下面的一些操作要点

[pygame系列_pygame安装](http://www.cnblogs.com/hongten/p/hongten_pygame_install.html)

在这个安装步骤里面，包含了[python(3.2.5)](http://www.python.org/ftp/python/3.2.5/python-3.2.5.msi)的安装和[pygame(1.9.2)](http://pygame.org/ftp/pygame-1.9.2a0.win32-py3.2.msi)的安装

先安装python，然后再安装pygame，这样再用你安装好的python打开PyMusic_v1.2.py文件，然后运行(F5)

Good Luck!

# 小程序的缺点

   1.歌手图片需要自己整理（240*240）

   2.歌曲需要从mp3转换到ogg格式

   3.手动添加歌手图和歌曲
   
# More Information

* Author            : Hongten
* E-mail            : [hongtenzone@foxmail.com](mailto:hongtenzone@foxmail.com)
* Home Page         : [http://www.cnblogs.com/hongten](http://www.cnblogs.com/hongten)
* Refer Skin Page   : [http://www.cnblogs.com/hongten/p/hongten_notepad_substance_skins.html](http://www.cnblogs.com/hongten/p/hongten_notepad_substance_skins.html)
* Substance URL     : [https://substance.dev.java.net/](https://substance.dev.java.net/)
