FROM openjdk:11-jdk-slim



RUN apt-get update && apt-get install -y python3-pip

RUN pip3 install pyspark mysql-connector-python avro-python3

COPY . /mysql-connector-java-8.0.13.jar /opt/spark/jars/

COPY . /spark-avro_2.12-3.4.0.jar /opt/spark/jars/

COPY . /app

WORKDIR /app

CMD ["/bin/bash", "/spark_submit.sh"]
# CMD [ "spark-submit","--master","local[*]","--jars","/opt/spark/jars/mysql-connector-java-8.0.13.jar;/opt/spark/jars/spark-avro_2.12-3.4.0.jar","app.py ","--ngrams","3" ]
# CMD [ "spark-submit","--master","local[*]","app.py --ngrams 3","--ngrams","3" ]
