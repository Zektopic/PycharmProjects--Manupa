#!/bin/python3

import os

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    n = len(topic)
    max_topics = 0
    teams_count = 0

    # Convert strings to integers for faster bitwise operations
    ints = [int(t, 2) for t in topic]

    for i in range(n):
        for j in range(i + 1, n):
            # Bitwise OR and count the 1s
            topics_known = (ints[i] | ints[j]).bit_count()

            if topics_known > max_topics:
                max_topics = topics_known
                teams_count = 1
            elif topics_known == max_topics:
                teams_count += 1

    return [max_topics, teams_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
