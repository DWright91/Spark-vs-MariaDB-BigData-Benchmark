# Spark vs. MariaDB Big-Data Wordcount Benchmark

Purpose: use big-data analysis techniques and implement a program to determine efficiency of Spark vs. MariaDB. 

1). Select three distinct keywords that most properly define and frequently appear within a large dataset.

2). Search within your big dataset how many times your selected words appear.

3). Count how long it took to run and complete the benchmark task using Spark compared to MariaDB.

----------------------------------------------------------------------------------------
Results: Spark was approx. 14 times faster than MariaDB.

    16.8 MB subset:
	    MariaDB ~ 100 seconds
	    Spark ~ 7 seconds

    36 GB subset:
	    MariaDB = 14+ hours
	    Spark = 1.5 hours

