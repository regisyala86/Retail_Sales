# Databricks notebook source
# MAGIC %md
# MAGIC ##Step 1 Upload the CSV into Databricks

# COMMAND ----------

# DBTITLE 1,Import Pandas Library
import pandas as pd

# COMMAND ----------

# DBTITLE 1,Load Dataset
df = pd.read_csv("/Workspace/Users/regisyala86@gmail.com/Kitokoss/1772719928300_retail_sales_dataset.csv")

# COMMAND ----------

# DBTITLE 1,Preview Dataset
df.head()

# COMMAND ----------

# MAGIC %md
# MAGIC ##Step 2 Review the Dataset

# COMMAND ----------

# DBTITLE 1,Check Structure
df.info()

# COMMAND ----------

# DBTITLE 1,Check Data Types
df.dtypes

# COMMAND ----------

# DBTITLE 1,Summary Statistics
df.describe()

# COMMAND ----------

# DBTITLE 1,Check for missing Values
df.isnull().sum()

# COMMAND ----------

# DBTITLE 1,Check for Duplicated Rows
df.duplicated().sum()

# COMMAND ----------

# DBTITLE 1,View Unique Categories
df['Product Category'].unique()

# COMMAND ----------

# MAGIC %md
# MAGIC ##Step 3 Clean and Prepare the Data

# COMMAND ----------

# DBTITLE 1,Remove Null Values
df = df.dropna()

# COMMAND ----------

# DBTITLE 1,Remove Duplicates
df = df.drop_duplicates()

# COMMAND ----------

# DBTITLE 1,Convert Date Column
df['Date'] = pd.to_datetime(df['Date'])

# COMMAND ----------

# DBTITLE 1,Create Extra Time Columns
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month_name()
df['Day'] = df['Date'].dt.day

# COMMAND ----------

# DBTITLE 1,Create Age Groups
bins = [0, 18, 30, 45, 60, 100]
labels = ['Teen', 'Young Adult', 'Adult', 'Middle Age', 'Senior']

df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Step 4 — Save as Databricks Table

# COMMAND ----------

# DBTITLE 1,Convert Pandas → Spark DataFrame
spark_df = spark.createDataFrame(df)

# COMMAND ----------

# DBTITLE 1,Save as table
spark_df.write.mode("overwrite").saveAsTable("retail_sales_data")

# COMMAND ----------

# DBTITLE 1,Display Table
display(spark.sql("SELECT * FROM retail_sales_data"))
