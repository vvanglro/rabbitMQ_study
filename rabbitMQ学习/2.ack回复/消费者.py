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
channel.queue_declare(queue='Hulkq2')


def callback(ch, method, properties, body):
    print(" 消费者接收到了任务 %r" % body)
    # int('aaa')
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 手动回复服务端已经将消息消费 服务端收到消息后将此条消息更改已消费状态


channel.basic_consume(queue='Hulkq2',
                      auto_ack=False,
                      on_message_callback=callback)

channel.start_consuming()