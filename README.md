# AutoFindDuplicatedPic
本项目使用的一个库更新了，所以本项目最近重写！

找出重复图片

把图片或者含图片的文件夹放入pic文件夹内，运行程序，重复的图片会被移动到duplication文件夹内，以供挑选，选择要保留的图片。

也可以修改程序，从指定文件夹内寻找图片，移动到指定的文件夹内。

因为使用的是os.walk()，递归的寻找图片，不要把根目录作为寻找图片的文件夹。尽量复制进pic文件夹内。
