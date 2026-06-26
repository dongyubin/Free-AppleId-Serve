# Windows Clash Party 使用教程

Clash Party 是一款简单易用的基于 Clash Meta（Mihomo）核心的科学上网客户端。自 Clash for Windows 删库之后，又出现了很多 Clash 客户端。但相比之下，Clash Party 是对新手很友好的客户端。

## Clash Party 特性

-  一键 Smart Core 规则覆写，基于 AI 模型自动选择最优节点
-  开箱即用，无需服务模式的 Tun
-  多种配色主题可选，UI 焕然一新
-  支持大部分 Mihomo(Clash Meta) 常用配置修改
-  内置 Smart内核 与 Mihomo(Clash Meta) 内核
-  通过 WebDAV 一键备份和恢复配置
-  强大的覆写功能，任意修订配置文件
-  深度集成 Sub-Store，轻松管理订阅

## 下载Clash Party软件

- Clash Party（原名：Mihomo Party）Github官网下载：[Releases · mihomo-party-org/mihomo-party](https://github.com/mihomo-party-org/mihomo-party/releases)
- [国内网盘下载](https://pan.baidu.com/s/1mwxXHr6ExuIxp_eWEUUB3Q?pwd=wwkj)（提取码: `wwkj`，只包含安装版）

## Clash Party导入订阅地址

1. 双击安装好的桌面图标，打开 [Clash Party](https://pan.baidu.com/s/1mwxXHr6ExuIxp_eWEUUB3Q?pwd=wwkj)
1. 在 [付费机场](https://help.wwkejishe.top/free-shadowrocket#fu-fei-ji-chang)（[备用地址](https://github.com/dongyubin/Free-AppleId-Serve#%E4%BB%98%E8%B4%B9%E6%9C%BA%E5%9C%BA%E6%8E%A8%E8%8D%90)）已经购买好套餐，复制订阅链接

> 旁边`代理`选项的意思是是否要通过代理更新订阅，因为有可能订阅的服务器被墙了。首次使用，那你肯定是没有翻墙的，就不要勾选了。

![Mihomo Party 导入订阅](https://cdn.wwkejishe.top/wp-cdn-02/2025/20250726115154384.png)

导入订阅地址

如果订阅成功，可以看到下方会出现你的订阅。蓝色为当前选中的订阅。

订阅右方有两个按钮：

⟳ 是更新按钮，点击会更新当前订阅，因为机场的服务器可能会被墙，所以需要时刻保持最新的节点订阅信息。

⁝ 是菜单按钮，点开后会出现下拉菜单：

- 编辑信息：可以编辑订阅的名称、地址、是否使用代理更新、自动更新时间以及添加覆写。一般来说设置个更新间隔就好了。
- 编辑文件：在内置的编辑器里直接编辑机场的配置文件。但不建议，因为当你更新了订阅之后，你修改的又会被还原。
- 打开文件：打开机场的配置文件。同样也不建议修改。如果需要自定义配置的话，使用`覆写`功能会更好。
- 删除：删除该订阅。

## 安装 Clash Party

下面以 Windows 为例。

双击安装包，会弹出 Windows Defender 的提示，这里点 `更多信息 > 仍要运行` 即可。

![Clash Party](https://mihomoparty.com/wp-content/uploads/2024/12/windows-defender-installing-mihomo-party.webp)Windows Defender 会阻止安装 Mihomo Party，点击仍要运行

选好安装位置后，直接点击`安装`即可。

![Clash Party安装](https://mihomoparty.com/wp-content/uploads/2024/12/install-mihomo-party.webp)安装 Mihomo Party 选择安装位置

安装完成后，首次启动记得要以管理员权限运行，右键单击，选择`以管理员身份运行`。

![以管理员身份运行Mihomo Party](https://mihomoparty.com/wp-content/uploads/2024/12/run-with-admin-auth.webp)

以管理员身份运行Mihomo Party

不然，你可能会看到下面的这个错误提示。

![首次启动 Miohomo Party 需要管理员权限](https://mihomoparty.com/wp-content/uploads/2024/12/mihomo-party-lanuch-error.webp)

首次运行，软件会有一个新手指引，帮你快速熟悉软件的功能分布，感觉还是挺好的，尤其对新手而言。

![Mihomo Party 新手引导](https://mihomoparty.com/wp-content/uploads/2024/12/mihomo-tutorial.webp)

## 开始使用

推荐使用香港节点，如果暂不使用，再点击上图中的系统代理开关，关闭即可（灰色为关闭）

![Mihomo Party 开始使用](https://cdn.wwkejishe.top/wp-cdn-02/2025/20250726115227994.png)

点击之后，所有的节点信息就会展开，选择你要使用的节点，再打开左侧的`系统代理`，就可以遨游外网了。

关于模式：

- 规则（默认）：外网走代理，国内直连。配置文件里会有对应的规则来判断当前的流量走不走代理。
- 全局：所有流量全部走代理。
- 直连：所有流量全都不走代理。

关于代理组上的几个图标的意思：

- 数字是节点数量。
- 🔍放大镜图标是筛选按钮，例如你只想看到香港的节点。
- 🎯瞄准图标是定位到当前节点。
- 速度表图标是测试所有节点的延迟。
- 箭头是展开或者折叠该代理组。

![选择节点，开启系统代理](https://mihomoparty.com/wp-content/uploads/2024/12/mihomo-party-enable-system-proxy.webp)

### 设置端口

有些应用程序需要使用特定的端口，例如 Telegram。像之前 Clash for Windows 、Clash Verge 都是默认的7890。

点击内核设置，可以设置内核版本以及端口，这里默认的也是7890。

![Mihomo Party 设置端口](https://mihomoparty.com/wp-content/uploads/2024/12/mihomo-party-set-port.webp)

## 其他设置

### TUN 模式

Mihomo Party 的一大特色就是可以一键开启 TUN模式，只要打开虚拟网卡的开关即可，无需像其他客户端一样安装服务模式。但是它会要求使用管理员权限，点击之后会自动重启软件。

![Clash Party Tun模式](https://mihomoparty.com/wp-content/uploads/2024/12/clashparty-enable-tun.avif)

TUN 模式和全局模式有一定的区别。

| 特性         | TUN 模式                       | 全局模式                   |
| ------------ | ------------------------------ | -------------------------- |
| 流量捕获范围 | 捕获所有流量，包括 TCP 和 UDP  | 捕获 TCP 流量              |
| 分流能力     | 支持，结合规则集可以选择性代理 | 不支持，所有流量均通过代理 |
| 配置难度     | 较高，需要安装虚拟网卡驱动     | 较低，直接设置代理         |
| 适用场景     | 游戏、视频客户端、办公应用     | 浏览器、轻量化的代理需求   |
| 性能要求     | 依赖系统性能和代理服务器性能   | 通常对系统和代理要求较低   |
| 权限要求     | 需要管理员权限启用虚拟网卡     | 无需额外权限               |

### WebDAV 备份

Mihomo Party 有 WebDAV 功能。

开启路径：点击左侧菜单上方的⚙️设置按钮，然后找到 WebDAV，输入地址、用户名和密码就可以备份和恢复了。

![Mihomo Party WebDAV 功能](https://mihomoparty.com/wp-content/uploads/2024/12/mihomo-party-webdav.webp)

## 特殊提示

如果操作均完全按照教程却没有网络，并且根据常见问题检查后一切正常的，可以尝试打开虚拟网卡开关（在系统代理旁边）

上述操作完成后浏览器之外的部分应用可能仍然无法走代理，如有此部分需求请尝试打开虚拟网卡开关，或自行谷歌搜索 Clash 代理UMP

## 模式介绍

![Mihomo Party 代理模式](https://cdn.wwkejishe.top/wp-cdn-02/2025/20250726115241181.png)



## 常见问题

### 解决“通常不会下载xxx.exe，请在打开前确保信任xxx.exe”

教程：https://www.bilibili.com/read/cv35877928

### 解决“Windows 已保护你的电脑，xxx阻止了无法识别的应用启动”

教程：点击“更多信息”之后，再点击“仍要运行”

### 解决“安装后双击图标打开没有反应”

教程：重启电脑