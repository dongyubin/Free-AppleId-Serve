# 微软 Windows 使用 Shadowsocks 设置教程

## 第一步 下载

下载任意一个软件压缩包，下载后解压至任意目录安装。

| Shadowsocks下载地址                                          | 推荐版本                                                     | XP版本                                                       | 历史版本                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1、下载：【[最新版 Shadowsocks-4.1.7.1](https://github.com/shadowsocks/shadowsocks-windows/releases/download/4.1.7.1/Shadowsocks-4.1.7.1.zip)】 | 【[推荐 Shadowsocks-4.0.10](https://github.com/shadowsocks/shadowsocks-windows/releases/download/4.0.10/Shadowsocks-4.0.10.zip) 】 | 【[XP系统 Shadowsocks-3.2](https://github.com/shadowsocks/shadowsocks-windows/releases/download/3.2/Shadowsocks-3.2.zip)】 | 【[历史版本](https://github.com/shadowsocks/shadowsocks-windows/releases)】 |

2、安装过程中 若提示.NET framework过低，则需要下载.NET framework软件[点击下载](https://www.microsoft.com/zh-CN/download/details.aspx?id=53344)，重新打开运行即可。

注：需要安装 [.NET Framework 4.6.2 ](https://dotnet.microsoft.com/download/dotnet-framework/net472)和 Microsoft [Visual C++ 2015 Redistributable (x86)](https://www.microsoft.com/en-us/download/details.aspx?id=53840)（一般已默认安装不需再次安装）。

## 第二步 使用教程

1、下载后解压文件，打开EXE文件安装后，右键单击左下角任务栏的 Shadowsocks【小飞机图标】进行配置。

2、在 【服务器】 菜单添加服务器节点。【服务器节点获取】详见：[SS/ShadowsocksR 服务器节点 点击获取](https://shadowsockshelp.github.io/Shadowsocks/ss.html)

3、选择 【启用系统代理】来启用系统代理。注：请禁用浏览器里的代理插件，或把它们设置为使用系统代理。

4、然后可以打开 [www.google.com](www.google.com) 进行测试。

> 注：若游览器无法打开 google.com 等网页，可能是你的游览器有插件或者设置了代理，可以尝试更换游览器测试一下。

![Windows Shadowsocks](https://shadowsockshelp.github.io/Shadowsocks/img/windows1.PNG)

## 最后 其他设置说明

### 一、服务器节点添加说明，目前主要有三种配置节点信息的方法，可以根据你的习惯和需要选择

方法一、从剪切板导入URL【推荐】每次复制SS链接，点击从剪切板导入URL即可配置服务器

1、首先复制SS地址二维码链接

2、然后右键单击右下角的软件，点击“服务器”－“从剪切板导入URL”

3、程序自动识别SS地址并导入服务器节点信息，最后启用系统代理即可使用

![img](https://shadowsockshelp.github.io/Shadowsocks/img/windows2.PNG)

方法二、扫二维码配置【推荐】 通过扫描屏幕上的二维码，自动配置，推荐

1、首先网页上或者是聊天窗口打开节点的二维码图片

2、然后右键单击右下角的软件，点击“服务器”－“扫描屏幕上的二维码”

3、程序自动识别二维码并导入服务器节点信息，最后启用系统代理即可使用

![img](https://shadowsockshelp.github.io/Shadowsocks/img/windows3.png)

方法三、手动编辑服务器配置 添加服务器，并逐一配置相关节点信息

1、右键单击右下角的软件，点击“服务器”－“编辑服务器”

2、逐一输入节点服务器【地址（域名或者IP地址）、端口、密码】，选择加密方式后确定

3、保存服务器节点信息，最后启用系统代理即可使用

### 二、系统代理模式 - 全局模式/PAC模式

1、全局模式：你可能会遇到一些网站打不开，仍然无法访问，这个你可以试试选择【系统代理模式-全局模式】，这样使全部流量经过节点服务器。

2、PAC模式【推荐】：选择PAC模式，PAC文件网址列表走节点服务器，国内网址则走你自己使用的网络流量。

3、关于PAC更新，你可以直接从 [GFWList](https://github.com/gfwlist/gfwlist) （由第三方维护）更新 PAC 文件，或者你可以手动编辑本地pac文件。需要更新PAC：依次操作：PAC ->从GFW List更新PAC （等待更新完毕后）->使用本地PAC->启动系统代理。

![img](https://shadowsockshelp.github.io/Shadowsocks/img/Windows4.jpg)

### 三、其他

1. 服务器自动切换

   - 负载均衡：随机选择服务器


   - 高可用：根据延迟和丢包率自动选择服务器


   - 累计丢包率：通过定时 ping 来测速和选择。如果要使用本功能，请打开菜单里的统计可用性。


   - 也可以实现 IStrategy 接口来自定义切换规则，然后给我们发一个 pull request。


2. UDP：对于 UDP，请使用 SocksCap 或 ProxyCap 强制你想使用的程序走代理。

3. 多实例：如果想使用其它工具如 SwitchyOmega 管理多个服务器，可以启动多个 Shadowsocks。 为了避免配置产生冲突，把 Shadowsocks 复制到一个新目录里，并给它设置一个新的本地端口。

4. 插件：若想通过插件来连接服务器，请到编辑服务器界面填入插件程序（相对路径或绝对路径）

> 注意： 在启用插件后，正向代理会被停用。