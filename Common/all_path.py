import os
# 将脚本中所需要到的路径准备配置好
path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]    # 根目录
excel_path = os.path.join(path, 'TestData', 'interface.xlsx')            # 测试数据路径
config_path = os.path.join(path, 'Config', 'config.ini')                 # 配置文件路径
# log_path = os.path.join(path, 'Log\\')                                   # 日志文件路径 本地运行
# yaml_path = os.path.join(path, 'TestData\\')                             # 存储数据路径 本地运行
log_path = os.path.join(path, 'Outputs', 'log')                                   # 日志文件路径 jenkins运行
yaml_path = os.path.join(path, 'TestData')                             # 存储数据路径 jenkins运行
