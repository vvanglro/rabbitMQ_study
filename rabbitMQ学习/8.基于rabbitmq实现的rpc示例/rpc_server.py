# -*- coding: utf-8 -*-
# @Time    : 2021/2/9 13:55
# @Author  : wanghao
# @File    : rpc_server.py
# @Software: PyCharm
import pika

credentials = pika.PlainCredentials("admin", "admin")
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.56.101', credentials=credentials))
channel = connection.channel()

# 服务端监听名叫rpc_queue的任务队列
channel.queue_declare(queue='rpc_queue')


def on_request(ch, method, props, body):
    n = int(body)
    print(n)

    response = n + 100
    # props.reply_to 要放结果的队列
    # props.correlation_id 任务ID
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 设置任务处理的顺序 谁空闲谁处理
channel.basic_qos(prefetch_count=1)
# 监听任务队列 一但有任务则执行on_request函数
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

channel.start_consuming()