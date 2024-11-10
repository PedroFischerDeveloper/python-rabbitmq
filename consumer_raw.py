import pika 

def call_back(cd, method, properties, body):
    print(body)

connection_parameters = pika.ConnectionParameters(
    host='localhost',
    port=5672,  
    credentials=pika.PlainCredentials(
        username='guest',
        password='guest'
    )
)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.queue_declare(
    queue="data_queue",
    durable=True
)

channel.basic_consume(
    queue="data_queue",
    auto_ack=True,
    on_message_callback=call_back
)

print(f'Listen RabbitMQ on port 5672')

channel.start_consuming()
