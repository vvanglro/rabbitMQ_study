# -*- coding: utf-8 -*-
# @Time    : 2021/2/8 14:49
# @Author  : wanghao
# @File    : 消费者.py
# @Software: PyCharm
import pika

# 有密码的连接方式
credentials = pika.PlainCredentials("admin","admin")
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.56.101',credentials=credentials))
channel = connection.channel()

# 声明一个队列（创建一个队列）
channel.queue_declare(queue='Hulkq1')


def callback(ch, method, properties, body):
    print(" 消费者接收到了任务 %r" % body)


channel.basic_qos(prefetch_count=1)  # 设置这个 可以在多个消费者时谁闲置谁去消费
channel.basic_consume(queue='Hulkq1',
                      auto_ack=False,  # 取消自动回复
                      on_message_callback=callback)

channel.start_consuming()