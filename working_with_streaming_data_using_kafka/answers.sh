bin/kafka-topics.sh --create --topics weather --bootstrap-server localhost:9092

bin/kafka-console-producer.sh --topic weather --bootstrap-server localhost:9092

bin/kafka-console-consumer.sh --topic weather --from-beginning --bootsrap-server localhost:9092
