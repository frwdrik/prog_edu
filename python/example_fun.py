#!/usr/bin/env python

"""Reas a file and returns the number of lines, words,
   and characters
"""

os.chdir('/home/frwdrik//Documents/Programming/python')
infile = open('word_count.tst', 'r')
lines = infile.read().split("\n")
line_count = len(lines)

word_count = 0
char_count = 0

for line in lines:
    words = line.split()
    word_count += len(words)

    char_count += len(line)

print("File has {0} lines, {1} words, {2} characters".format\
      (line_count, word_count, char_count))
