from confluent_kafka import Producer
import json

# Configura el productor
conf = {
    'bootstrap.servers': 'localhost:29092',  # Usa el puerto correcto
    'client.id': 'python-producer'
}

producer = Producer(conf)

# Función para manejar la confirmación de entrega
def delivery_report(err, msg):
    if err is not None:
        print(f"Error al enviar el mensaje: {err}")
    else:
        print(f"Mensaje enviado con éxito: {msg.topic()} [{msg.partition()}] @ {msg.offset()}")

# Cargar el archivo JSON
with open('partidos.json', 'r') as file:
    partidos = json.load(file)

# Enviar cada mensaje del JSON
try:
    for partido in partidos:
        # Envía el mensaje
        producer.produce(
            topic='replicated-topic',
            value=json.dumps(partido).encode('utf-8'),  # Convierte el diccionario a JSON
            callback=delivery_report
        )
        producer.flush()  # Espera a que el mensaje se envíe antes de continuar
except Exception as e:
    print(f"Error al enviar el mensaje: {e}")
finally:
    producer.flush()  # Asegúrate de que todos los mensajes se envíen antes de cerrar