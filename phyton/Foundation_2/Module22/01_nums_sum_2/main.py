import os

num_file = open('numbers.txt', 'r')
numbers_sum = sum(map(int,num_file.read().split()))
num_file.close()
ans_file = open('answer.txt', 'w')
ans_file.write(str(numbers_sum)+'\n')
ans_file.close()
