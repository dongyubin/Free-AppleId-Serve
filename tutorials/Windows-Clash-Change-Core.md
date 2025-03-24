# Clash for Windows 修改内核为最新的mihomo内核

[Clash for Windows 下载地址](https://pan.quark.cn/s/b591ae08d08b)

在网上找到的教程最高只支持 mi­homo v1.16.0 版内核，最新的都会提示错误： **无法连接到 Clash core 核心** ，原因是 Clash Meta 更新改名为 mi­homo 后路径变了，这种情况创建一个链接就可以正常使用了

[kayaladream/Clash-Core-Change](https://github.com/kayaladream/Clash-Core-Change)：**一键切换mihomo内核**

## 下载内核

打开最新的 mi­homo 的项目下载地址：[https://github.com/MetaCubeX/mihomo/releases](https://github.com/MetaCubeX/mihomo/releases)，这里我选择的是最新的 v1.18.3 版本

![mi­homo下载](https://picgo.leginn.top/img/2024/04/13/CFW_h.webp)

## 替换

1. 下载完毕后解压压缩包
    ![解压压缩包](https://picgo.leginn.top/img/2024/04/13/CFW_h1.webp)
  
2. 打开CFW安装目录的 `resources\static\files\win\x64`，将默认的 `clash-win64.exe` 备份，这个是默认的Clash Premium内核，这里我重命名为 `clash-win64_old.exe` ，将第一步解压的mihomo内核程序复制进来， 并重命名为 `clash-win64.exe`，这样就替换完毕了
   ![clash-win64.exe](https://picgo.leginn.top/img/2024/04/13/CFW_h2.webp)

3. 打开CFW，如果没有意外的话应该是提示： **无法连接到 Clash core 核心**
   ![无法连接到 Clash core 核心](https://picgo.leginn.top/img/2024/04/13/CFW_h5.webp)



### 解决无法连接到核心

1. 退出CFW，打开自带的文件资源管理器，在地址栏输入 `%USERPROFILE%/.config/mihomo` 进入文件夹

   ![img](https://picgo.leginn.top/img/2024/04/13/CFW_h6.webp)

2. 进入文件夹后返回上一层，然后把 `mihomo` 文件夹删除掉
   ![img](https://picgo.leginn.top/img/2024/04/13/CFW_h4.webp)

3. 打开 **powershell** ，执行以下命令，执行完成后会提示 **创建的符号链接**
   ```cmd
   cmd /c mklink /d "%USERPROFILE%\.config\mihomo" "%USERPROFILE%\.config\clash"
   ```
   ![powershell创建的符号链接](https://picgo.leginn.top/img/2024/04/13/CFW_h6.webp)

4. 重新打开CFW，Clash内核这显示 **UnKnown** 就是替换完毕啦
   ![Clash内核](https://picgo.leginn.top/img/2024/04/13/CFW_h7.webp)