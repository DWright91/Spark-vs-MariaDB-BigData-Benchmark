################################################################################
## wordcountSparkTest.py                                                      ##
################################################################################

# Open Command Prompt
# Navigate to directory D:/wikipedia-dataset
# Run command: spark-submit wordcountSparkTest.py

from pyspark import SparkContext, SparkConf
from collections import Counter
import time

# Start the timer
start = time.time()

# set up Spark context
conf = (SparkConf().setMaster("local")
                    .setAppName("word-count")
                    .set("spark.executor.memory", "10g")) # can set to 1tb.
sc = SparkContext(conf = conf)

# read in the file
# filename = "D:\wikipedia-dataset\enwiki-20230101-pages-meta-history1.xml-p1p857"
# filename = "input.txt"
# filename = "enwiki-20230101-pages-meta-history1.xml-p1p857"
filename = "wikipedia-subset.xml"
text_file = sc.textFile(filename)

# split the text into words
words = text_file.flatMap(lambda line: line.lower().split())

# count the occurrences of each word
word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# sort the words by count
sorted_words = word_counts.takeOrdered(word_counts.count(), lambda x: -x[1])

# print("List of words in dataset:")

# print the words and their counts
# for word, count in sorted_words:
#     print(f"{word}: {count}")

# print the top three words and their counts
for x in range(3):
    print(f"{sorted_words[x]}")

# get the three most common words
# top_words = word_counts.takeOrdered(3, lambda x: -x[1])

# assign the top words as keywords
# keywords = [word[0] for word in top_words]

# print(f"The top three keywords are: {keywords}")
sc.stop()

# Stop the timer
end = time.time()

# Print the time taken
print(f"Total time taken: {end - start}")
