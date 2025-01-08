import os

def is_connected():
    """检测网络连接"""
    response = os.system('ping -n 1 www.baidu.com')
    if response == 0:
        print("网络连通")
        return True
    else:
        print("无网络连接")
        return False

def open_with_shortcut(shortcut_path):
    """通过快捷方式打开应用程序"""
    if os.path.exists(shortcut_path):
        try:
            os.startfile(shortcut_path)
            print(f"成功打开 {shortcut_path}")
        except Exception as e:
            print(f"无法打开快捷方式 {shortcut_path}: {e}")
    else:
        print(f"路径 {shortcut_path} 不存在，跳过此应用。")

if __name__ == "__main__":
    # 检测网络连接
    network_connected = is_connected()
    
    # 定义应用程序的快捷方式路径
    apps_to_open = [
        r'C:\Apps\QuickStart\QQ.lnk',
        r'C:\Apps\QuickStart\WeChat.lnk',
        r'C:\Apps\QuickStart\cloudmusic.lnk',
        r'C:\Apps\QuickStart\Todo.lnk'  # 微软的待办清单快捷方式
    ]
    
    # 如果有网络，打开QQ、微信、网易云音乐
    if network_connected:
        for app in apps_to_open[:3]:  # 前三个是需要网络的应用
            open_with_shortcut(app)
    
    # 无论有无网络，都打开微软的待办清单
    open_with_shortcut(apps_to_open[3])  # 第四个是待办清单