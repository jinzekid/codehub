# Author: Jason Lu

# 需求:
#
# 1.主机分组
# 2.主机信息配置文件用configparser解析
# 3.可批量执行命令、发送文件，结果实时返回，执行格式如下
#   3.1 batch_run  -h h1,h2,h3   -g web_clusters,db_servers    -cmd  "df -h"　
#   3.2 batch_scp   -h h1,h2,h3   -g web_clusters,db_servers  -action put  -local test.py  -remote /tmp/　
# 4.主机用户名密码、端口可以不同
# 5.执行远程命令使用paramiko模块
# 6.批量命令需使用multiprocessing并发







