
- Storage and compute platform
- Runs as service  on public cloud
- Uses Snowflake SQL

Big Data Storage
Shared Everything
Shared Disk - Computation is done on number of separate nodes and they all share shared disk. Computation on a node can be paused as they wait for another node completing its process.
Shared Nothing - Each computation node has its own storage

Snowflake Hybrid approach
Persistent data in shared storage
Each processing node stores data locally

# Detailed View Inside Snowflake

Snowflake is a cloud-based data warehousing platform that plays a crucial role in modern data engineering and analytics. It is designed to address the challenges of traditional on-premises data warehousing by providing a scalable, flexible, and fully managed cloud solution. Data engineers often work with Snowflake to design, build, and maintain data pipelines and warehouses.

1. **Cloud-Native Data Warehousing:** Snowflake is a cloud-based, fully managed data warehousing platform that offers scalability and flexibility without the need for on-premises infrastructure.
    
2. **Data Integration and ETL:** Data engineers can easily integrate data from various sources into Snowflake and set up data pipelines for ingestion, transformation, and loading.
    
3. **Data Security and Compliance:** Snowflake prioritizes data security and compliance, providing encryption, access controls, audit logs, and masking features to protect sensitive data.
    
4. **Scalability and Concurrency:** Snowflake's architecture allows for high concurrency and the ability to scale resources up or down as needed to handle varying workloads.
    
5. **SQL-Based Querying and Performance Optimization:** Data engineers can use standard SQL for querying and analytics, benefiting from automatic query optimization and caching mechanisms to enhance performance.

Snowflake Layers
Cloud service, Compute, Storage

Storage
- Fully managed by Snowflake
- Optimized columnar format
- Always compressed and encrypted
- Only accessible through Snowflake SQL

Compute - Virtual Warehouses
- Cluster of nodes allocated by Snowflake from a cloud provider
- Resources are isolated between warehouses
- Can scale horizontally or vertically
- Auto-stop and auto-resume
- Standard and Snowpark

Cloud Service
- Interface with other layers
- Security
- Query optimization

# Working with Warehouses

Warehouses in Snowflake provide a flexible and efficient way to manage computational resources, optimize query performance, and control costs. They empower organizations to handle a wide range of workloads, from ad-hoc analysis to data loading and production reporting, while ensuring scalability, isolation, and cost-effectiveness. Understanding how to effectively use and manage warehouses is crucial for harnessing the full power of Snowflake's cloud-based data warehousing platform.

