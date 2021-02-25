# -*- coding: utf-8 -*-
# @Time    : 2021/2/8 9:56
# @Author  : wanghao
# @File    : 1.消息队列.py
# @Software: PyCharm

# Python操作 RabbitMQ、Redis、Memcache、SQLAlchemy
# https://www.cnblogs.com/wupeiqi/articcles/5132791.html

# 1. 你了解的消息队列
'''
 - Queue 将数据存储当前服务器的内存
 - redis 列表
 - rabbitMQ/kafka/zeroMQ（专业做消息队列）
'''

# 2. 公司在什么情况下会使用消息队列？
'''
  任务处理：请求的数量太多了，需要把消息临时放到某个地方。
  发布订阅：一旦发布消息，所有订阅者都会收到一条相同的消息。
  
  应用场景：
        - 长轮询
        - 智能玩具调用百度AI接口时， celery + RabbitMQ
        - 生产者&消费者
'''

# 3. rabbitMQ安装
'''
  服务端：
    sudo rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
    sudo yum -y install erlang
    sudo yum -y install rabbitmq-server
    # 启动无用户密码
    sudo service rabbitmq-server start
    # 设置用户密码
    sudo rabbitmqctl add_user wupeiqi 123
    # 设置用户为administrator角色
    sudo rabbitmqctl set_user_tags wupeiqi administrator
    # 设置权限
    sudo rabbitmqctl set_permissions -p "/" root ".*" ".*" ".*"

    # 开放外部使用和端口  修改完cofig文件后记得source下立即生效不用重启
    https://blog.csdn.net/qq_36194413/article/details/85165382?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control

  客户端：
     pip install pika
'''

# 4. 快速使用
'''
    生产者消费者
        n VS 1
        n VS m
    发布订阅
        fanout, 和exchange关联的所有队列都会接收到消息。
        direct, 关键字精确匹配,exchange关联的队列都会接收到消息。
        topic,  关键字模糊匹配,exchange关联的队列都会接收到消息。


    消息队列exchange_type一共三种类型：
        1. fanout  将消息发给所有的队列
        2. direct  将消息发给指定关键字routing_key的队列
        3. topic   将消息发给模糊匹配的关键字routing_key队列
'''

# 5. exchange是什么?
'''
    消息处理的中间件，可以帮助生产者将相关信息发送到指定相关队列。

'''



# 6.RPC
'''
    前戏：
        我  ->  去哪儿  ->   首都机场票务中心

    远程过程调用
        我  ->  去哪儿    接收任务/结果     首都机场票务中心
    
    
'''