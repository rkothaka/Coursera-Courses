# What is Apache Spark?

**Apache Spark**
- Big Data analytics engine
- Uses RAM memory
- Generally faster than Hadoop (especially for iterative work)
- Attaches to number of cluster management systems
- Requires distributed data stores

**Spark Concepts**
- Driver sends jobs to executors
- Jobs are divided into stages
- Data is partitioned with task running per partition
- Resilient Distributed Dataset (RDD)

Apache Spark is an open-source, powerful, and versatile data processing engine designed for efficient distributed data processing and analytics. It provides a unified platform for batch processing, interactive queries, machine learning, and streaming data analysis.

For a new data engineer, gaining a solid understanding of Apache Spark is essential. Here are some of the most important things to know about Apache Spark:

**Benefits:**

- **Speed:** Spark's in-memory processing enables significantly faster data processing compared to disk-based processing in Hadoop's MapReduce.
- **Versatility:** Spark supports batch processing, interactive queries, machine learning, and streaming data processing in a unified platform.
- **Ease of Use:** Spark's APIs are more intuitive and developer-friendly, making it easier for newcomers to get started.
- **Advanced Analytics:** Spark's MLlib library offers machine learning capabilities, allowing data engineers to perform advanced analytics tasks.
- **Real-time Processing:** Spark Streaming enables real-time data processing, making it suitable for use cases requiring quick insights from streaming data.

**Drawbacks:**

- **Memory Requirement:** Spark's in-memory processing can demand substantial memory resources, which might lead to higher infrastructure costs.
- **Learning Curve:** While more user-friendly than MapReduce, Spark still requires a learning curve, especially for more complex tasks.
- **Compatibility:** Spark is relatively newer than Hadoop, so certain legacy systems might be more compatible with Hadoop-based solutions.

https://learn.microsoft.com/en-us/training/modules/use-apache-spark-azure-databricks/02-understand-spark
