import pika
import sys


conn_params = pika.ConnectionParameters('localhost', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue=sys.argv[1], durable=sys.argv[2])


def exchange(name):
    for line in sys.stdin:
        channel.basic_publish(exchange='',
                              routing_key=name,
                              body=line,
                              properties=pika.BasicProperties(delivery_mode=2))


if __name__ == '__main__':
    exchange(sys.argv[1])


connection.close()
