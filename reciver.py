import pika
import traceback
import sys
import logging

conn_params = pika.ConnectionParameters('localhost', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='queue', durable=True)


logging.basicConfig(level='DEBUG',
                    filename='mylog.log')
logger = logging.getLogger()

print("Waiting for messages. To exit press CTRL+C")


def callback(ch, method, properties, body):
    logger.warning(f'We get string: {body}')
    print(body)


channel.basic_consume('first-queue', callback)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
except Exception:
    channel.stop_consuming()
    traceback.print_exc(file=sys.stdout)
