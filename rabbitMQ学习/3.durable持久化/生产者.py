# -*- coding: utf-8 -*-
# @Time    : 2021/2/8 13:56
# @Author  : wanghao
# @File    : 生产者.py
# @Software: PyCharm

import pika

# 无密码的连接方式
# connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.56.101'))

# 有密码的连接方式
credentials = pika.PlainCredentials("admin","admin")
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.56.101',credentials=credentials))
channel = connection.channel()
# 声明一个队列(创建一个队列)-支持持久化
channel.queue_declare(queue='Hulkq3',durable=True)

channel.basic_publish(exchange='',
                      routing_key='Hulkq3',  # 消息队列名称
                      body='msg22288888',
                      properties=pika.BasicProperties( delivery_mode=2 ) # 把消息也持久化
                      )

connection.close()