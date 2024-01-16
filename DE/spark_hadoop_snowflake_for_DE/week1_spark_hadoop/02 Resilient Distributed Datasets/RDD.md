- Abstraction of data and tasks partitioned across nodes
- Transformations (lazy)
- Actions (return computations)
- Grouped into stages

# What are RDDs?

Resilient Distributed Datasets (RDDs) are a fundamental data structure in the Apache Spark framework, designed to facilitate distributed data processing across clusters. RDDs serve as the foundational building blocks for Spark applications, enabling fault-tolerant, parallelized data processing in a distributed computing environment.

Key characteristics of RDDs include:

1. **Resilience:** RDDs are "resilient" because they can recover from node failures. Through lineage information, Spark can recreate lost data partitions by recomputing them from the original data and transformations.
    
2. **Distributed:** RDDs are distributed across multiple nodes in a Spark cluster, allowing for parallel processing of data. Each RDD is divided into partitions, with each partition residing on a separate node.
    
3. **Immutable:** RDDs are immutable, meaning their content cannot be changed once created. Instead, transformations applied to RDDs produce new RDDs, preserving data integrity.
    
4. **In-Memory Processing:** RDDs are stored in memory, enabling faster data access and computation compared to traditional disk-based storage. This in-memory processing contributes to Spark's speed advantage.
    
5. **Transformation and Action Operations:** RDDs support two types of operations: transformations (e.g., map, filter, reduceByKey), which create new RDDs from existing ones, and actions (e.g., count, collect, saveAsTextFile), which trigger computations and return results.
    
6. **Data Partitioning:** RDDs allow users to control data partitioning, which can optimize data locality and enhance processing efficiency.

Other Resources:
https://www.databricks.com/glossary/what-is-rdd
https://www.youtube.com/watch?v=Ofk7G3GD9jk - A Tale of Three Apache Spark APIs: RDDs, DataFrames, and Datasets

Properties of RDDs:
1. Distributed Data Abstraction
2. Resilient and Immutable
3. Compile-time Type-safe
4. Unstructured/Structured Data: Text(logs, tweets, articles, social)
5. Lazy

Why use RDDs?
- Offer control and flexibility
- Low-level API
- Type-safe
- Encourage how-to

When to use RDDs?
- Low-level API & control of dataset
- Dealing with unstructured data (media streams or texts)
- Manipulate data with lambda functions than DSL
- Don't care about schema or structure of data
- Sacrifice optimization, performance, & inefficiencies

What's the problem?
- Express how-to solution, and not what-to
- Not optimized by Spark
- Slow for non-JVM languages like Python
- Inadvertent inefficiencies 


https://www.databricks.com/blog/2016/07/14/a-tale-of-three-apache-spark-apis-rdds-dataframes-and-datasets.html

