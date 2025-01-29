from confluent_kafka import Consumer, KafkaError
import json
import csv

# Configura el consumer
conf = {
    'bootstrap.servers': 'localhost:29092',  # Usa el puerto correcto
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  # Lee desde el principio del topic
}

consumer = Consumer(conf)

# Suscribe al topic
consumer.subscribe(['replicated-topic'])

# Archivo CSV de salida
csv_file = 'partidos.csv'
fieldnames = ['id', 'timestamp', 'equipo_local', 'equipo_visitante']

# Abre el archivo CSV para escribir
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Escribe la cabecera del CSV

    try:
        while True:
            # Lee un mensaje
            msg = consumer.poll(timeout=1.0)  # Espera hasta 1 segundo por un mensaje

            if msg is None:
                continue  # No hay mensajes, sigue esperando
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # Fin de la partición, no es un error
                    print(f"Fin de la partición {msg.partition()} en el offset {msg.offset()}")
                else:
                    print(f"Error al recibir el mensaje: {msg.error()}")
                continue

            # Decodifica el mensaje
            partido = json.loads(msg.value().decode('utf-8'))
            print(f"Mensaje recibido: {partido}")

            # Escribe el mensaje en el archivo CSV
            writer.writerow(partido)
            file.flush()  # Asegúrate de que los datos se escriban en el archivo

    except KeyboardInterrupt:
        print("Consumer detenido manualmente")
    finally:
        # Cierra el consumer
        consumer.close()