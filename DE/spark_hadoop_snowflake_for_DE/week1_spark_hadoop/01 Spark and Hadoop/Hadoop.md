**Big Data**
- Data too big for single machine
- Distributed data storage
- Distributed data processing

**Big Data Platforms**
- Hadoop
- Spark
- Snowflake - distributed storage solutions, but it's evolving to also include data processing solutions.
- Databricks - began more on processing side, but also involves storage

# What is Apache Hadoop?

Apache Hadoop is an open-source framework designed for distributed storage and processing of large volumes of data across clusters of commodity hardware. It offers a scalable solution to handle big data by distributing data across multiple nodes and enabling parallel processing. At its core, Hadoop consists of two main components: Hadoop Distributed File System (HDFS) for storage and Hadoop MapReduce for processing.

**Apache Hadoop**
- Platform for processing big data
- Implementation of MapReduce programming model
- Distributes work across multiple machines (nodes)
- Writes intermediate data to disk

Here are some of the most important things for a new data engineer to learn about Apache Hadoop:

**Benefits:**

- **Scalability:** Hadoop's distributed storage (HDFS) and processing (MapReduce) architecture make it suitable for handling vast amounts of data across clusters of commodity hardware.
- **Batch Processing:** Hadoop excels in batch processing scenarios, where large datasets are processed sequentially using MapReduce jobs.
- **Ecosystem:** Hadoop offers a rich ecosystem of tools, including Hive for querying, Pig for data processing, and more, making it versatile for various data-related tasks.
- **Data Resilience:** HDFS's data replication ensures data redundancy and fault tolerance, safeguarding against node failures.
- **Cost-Effectiveness:** Hadoop's open-source nature and ability to run on commodity hardware can offer cost-effective solutions for storing and processing large datasets.

**Drawbacks:**

- **Latency:** Hadoop's batch processing nature can result in higher latencies for real-time processing needs.
- **Complexity:** Setting up, configuring, and managing a Hadoop cluster can be complex and require specialized skills.
- **Programming Model:** MapReduce's programming model can be intricate, and developing applications might require more effort compared to newer alternatives.



