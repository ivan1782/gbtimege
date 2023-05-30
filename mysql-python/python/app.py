# import mysql.connector
# from mysql.connector import Error
import sys
import argparse
from pyspark.sql import SparkSession

print(" INICIO PYSPARK V 1.0")
arguments = sys.argv
user = arguments[1]
passwordmysql = arguments[2]
dbmysql = arguments[3]
tablemysql = arguments[4]
csvfile = arguments[5]
newcolnames =  arguments[6].split(",")


def renameCols(df, old_columns, new_columns):
    for old_col,new_col in zip(old_columns,new_columns):
        df = df.withColumnRenamed(old_col,new_col)
    return df


spark = SparkSession.builder \
           .appName('SparkByExamples.com') \
           .config("spark.jars", "mysql-connector-java-8.0.13.jar") \
           .config("spark.jars.packages", "org.apache.spark:spark-avro_2.12:3.4.0")\
           .getOrCreate()

print(" **************** READING CSV  PYSPARK ********************")

df_csv = spark.read.csv(csvfile,header=False)

df_csv_reame = renameCols(df_csv,df_csv.columns,newcolnames)

df_csv_reame.show(10)


print(" **************** WRITING MYSQL  PYSPARK ********************")

df_csv_reame.write \
  .format("jdbc") \
  .option("driver","com.mysql.cj.jdbc.Driver") \
  .option("url", "jdbc:mysql://servidor_mysql:3306/{}".format(dbmysql)) \
  .option("dbtable", tablemysql) \
  .option("user", user) \
  .option("password", passwordmysql) \
  .option("truncate", "true") \
  .mode("overwrite") \
  .save()

print(" **************** READING MYSQL  PYSPARK ********************")

df = spark.read \
  .format("jdbc") \
  .option("driver","com.mysql.cj.jdbc.Driver") \
  .option("url", "jdbc:mysql://servidor_mysql:3306/{}".format(dbmysql)) \
  .option("dbtable", tablemysql) \
  .option("user", user) \
  .option("password", passwordmysql) \
  .load()

df.show()


print(" ############################# BACKUP WRITING #############################")


df_csv_reame.write.format("com.databricks.spark.avro") \
      .mode("overwrite") \
      .save("jobs.avro")

print(" ############################# BACKUP READING  #############################")


df_avro = spark.read.format("com.databricks.spark.avro").load("jobs.avro")

df_avro.show(10)







# try:



#     connection = mysql.connector.connect(host='servidor_mysql',
#                                          database='db',
#                                          user='user',
#                                          password='password')
#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)

# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")