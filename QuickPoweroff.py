import subprocess
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def shutdown():
    if 1:
        result = subprocess.call(['shutdown', '/s', '/t', '0'])


if __name__ == "__main__":
    if is_admin():
        shutdown()
    else:
        print("请以管理员身份运行此脚本。")