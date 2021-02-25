# -*- coding: utf-8 -*-
# @Time    : 2021/2/8 16:19
# @Author  : wanghao
# @File    : 生产者_发布者.py
# @Software: PyCharm
import pika

# 有密码的连接方式
credentials = pika.PlainCredentials("admin","admin")
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.56.101',credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='m2', exchange_type='direct')

channel.basic_publish(exchange='m2',
                      routing_key='sb',  # 给队列名称发消息
                      body='ssss')

connection.close()