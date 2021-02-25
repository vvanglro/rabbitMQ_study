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

# exchange='m1' exchange(秘书)的名称
# exchange_type='direct' 秘书的工作方式将消息发送给特定的队列
channel.exchange_declare(exchange='m2', exchange_type='direct')

# 不指定queue名字,rabbitmq会随机分配一个名字
# exclusive=True会在使用此queue的消息订阅端断开后,自动将queue删除
result = channel.queue_declare(queue='',exclusive=True)
queue_name = result.method.queue


# 让exchange和queue进行绑定 routing_key='alex' routing_key='sb'只接收队列名称关键字为alex和sb的消息
channel.queue_bind(exchange='m2',queue=queue_name, routing_key='alex')
channel.queue_bind(exchange='m2',queue=queue_name, routing_key='sb')

def callback(ch, method, properties, body):
    print(" 消费者接收到了任务 %r" % body)

channel.basic_consume(queue=queue_name,
                      auto_ack=False,  # 取消自动回复
                      on_message_callback=callback)

channel.start_consuming()