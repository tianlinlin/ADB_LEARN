import subprocess #导入subprocess 模块
import os
from auto_git import auto_push,file_relpath
auto_push(file_relpath(os.path.abspath(__file__)))
result = subprocess.run(
    ['args'],                 # 命令，列表或字符串（字符串需 shell=True）
                              # 以下为仅关键字参数
    stdin=None,               # 标准输入，如 subprocess.PIPE / 文件对象 / 整数文件描述符
    input=None,               # 发送到 stdin 的字节或字符串（与 text 有关）
    stdout=None,              # 标准输出重定向
    stderr=None,              # 标准错误重定向
    capture_output=False,     # 是否捕获 stdout/stderr（Python 3.7+）
    shell=False,              # 是否通过 shell 执行
    cwd=None,                 # 工作目录
    timeout=None,             # 超时秒数
    check=False,              # 返回码非 0 时抛出 CalledProcessError
    encoding=None,            # 文本模式的编码（如 'utf-8'）
    errors=None,              # 编码错误处理方式
    text=None,                # 是否返回字符串（代替 bytes），Python 3.7+
    env=None,                 # 环境变量字典
    universal_newlines=None,  # text 的旧名称，Python 3.7+ 废弃
   # **other_popen_kwargs       其他传给 Popen 的参数（如 bufsize, executable 等）
)
'''
大部分都是默认值，实际上不需要记忆，以下比较常用
timeout 超时几秒之后就自动杀死程序
check   错误时抛出异常
capture_output 这会捕获标准输出或者错误
text    返回字符串供py使用

设置 capture_output=True 相当于同时指定：
stdout=subprocess.PIPE
stderr=subprocess.PIPE

这样，子进程的输出不会打印到终端，而是保存在返回的 CompletedProcess 对象的 .stdout 和 .stderr 属性中供你使用。
'''
stdout = result.stdout #读取标准输出
stderr = result.stdout #读取错误


# 与之类似的，是Popen方法，提供了更加精细的控制流管理、可以实时处理输出，更加灵活，所以在获取日志的时候常用
result_Popen = subprocess.Popen(
    ['args'],                     # 必需：命令（列表或字符串）
    bufsize=-1,               # 缓冲区大小（0=无缓冲，1=行缓冲，正数=字节数），行缓冲可以确保实时输出
    executable=None,          # 替代程序的可执行文件路径
    stdin=None,               # 标准输入（PIPE / DEVNULL / 文件对象 / 文件描述符）
    stdout=None,              # 标准输出
    stderr=None,              # 标准错误
    preexec_fn=None,          # 在子进程执行前调用的函数（仅Unix）
    close_fds=True,           # 是否关闭除0,1,2外的所有文件描述符
    shell=False,              # 是否通过shell执行
    cwd=None,                 # 工作目录
    env=None,                 # 环境变量字典
                              # 以下为仅关键字参数（Python 3.6+）
    encoding=None,            # 文本模式使用的编码
    errors=None,              # 编解码错误处理方案
    text=None,                # True时以文本模式处理流（推荐替代universal_newlines）
)
'''
stdout=subprocess.PIPE, 
stderr=subprocess.PIPE, 与
capture_output=True 是等价的
'''
# 因为popen往往是实时输出的所以需要用迭代器
for line in result_Popen.stdin:
    print(line.rstrip()) #去除字符串末尾的空白字符（包括换行符 \n、回车符 \r、空格、制表符等）
