# -*- coding: utf-8 -*-
# @Time    : 2021/2/9 11:31
# @Author  : wanghao
# @File    : rpc_client.py
# @Software: PyCharm
import pika
import uuid

class FibonacciRpcClient(object):

    def __init__(self):
        credentials = pika.PlainCredentials("admin", "admin")
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.56.101', credentials=credentials))
        self.channel = self.connection.channel()

        # 不指定queue名字,rabbitmq会随机分配一个消息队列名字(用于接收结果)
        # exclusive=True会在使用此queue的消息订阅端断开后,自动将queue删除
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        # 监听消息队列中是否有值返回, 如果有值则执行 on_response函数（一旦有结果, 则执行on_response）
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())

        # 客户端给服务端发送任务： 任务id = corr_id  任务内容 = '30'  用于接收结果的队列名称
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue', # 服务端接收任务的队列名称
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,  # 用于接收结果的队列
                correlation_id=self.corr_id,  # 任务id
            ),
            body=str(n))

        while self.response is None:
            self.connection.process_data_events()

        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()

response = fibonacci_rpc.call(40)
print('返回结果:', response)
