# Guía Rápida de Kafka

## Gestión de Topics

### Listar Topics

Para listar todos los topics disponibles en Kafka, ejecuta el siguiente comando:

```sh
docker exec -it kafka-kafka1-1 kafka-topics --list --bootstrap-server kafka1:9092
```

### Crear un Topic Simple

Para crear un topic básico en Kafka con una única partición y sin replicación:
```sh
docker exec -it kafka-kafka1-1 kafka-topics --create --topic simple-topic --bootstrap-server kafka-kafka1-1:9092 --partitions 1 --replication-factor 1
```

### Crear un Topic con Particiones y Réplicas

Para crear un topic en Kafka con múltiples particiones y réplicas:

```sh
docker exec -it kafka-kafka1-1 kafka-topics --create --topic replicated-topic --bootstrap-server kafka-kafka1-1:9092 --partitions 3 --replication-factor 3
```
## Operaciones con Mensajes

### Escribir en un Topic (Producer)

Para enviar mensajes a un topic de Kafka:

```sh
docker exec -it kafka-kafka-1 kafka-console-producer --broker-list localhost:9092 --topic test-topic
```

### Leer desde un Topic (Consumer)

Para consumir mensajes de un topic en Kafka desde el inicio:

```sh
docker exec -it kafka-kafka-1 kafka-console-consumer --bootstrap-server localhost:9092 --topic test-topic --from-beginning
```

## Cliente Kafka en Python

### Instalar Librerías de Kafka para Python

Para instalar las bibliotecas necesarias de Kafka en Python:

```sh
pip install kafka-python
pip install confluent-kafka
```


### Ejecutar el Producer

Para iniciar el script del productor en Kafka:

```sh
python producer.py
```

### Ejecutar el Consumer

Para iniciar el script del consumidor en Kafka:

```sh
python consumer.py
```


## Notas

- Asegúrate de que Kafka esté en ejecución antes de ejecutar estos comandos.
- Ajusta los nombres de `bootstrap-server` y los contenedores según tu configuración.
- Los scripts de Python (`producer.py` y `consumer.py`) deben estar configurados correctamente para coincidir con los nombres de los topics utilizados.

