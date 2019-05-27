import pika

RABBIT_QUEUE_NAME = ''   #queue  name

rabbitConnection = pika.BlockingConnection(pika.URLParameters(' ') )  #enter url

rabbitchannel = rabbitConnection.channel()

method_frame, header_frame, body = rabbitchannel.basic_get(RABBIT_QUEUE_NAME, auto_ack=False)

print(method_frame)   #method object, gives the message count in it
