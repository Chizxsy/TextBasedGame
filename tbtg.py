#text based semi-romantic adventure game
import sys
import random
import time
from rich.console import Console
from rich import print

console = Console()

text_file = open("text.txt", "r")

list = []

def filesort():
    for line in text_file:
        line = line.strip()
        list.append(line)
    text_file.close()

filesort()

def type(list):
    for letter in list:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(0.02)
    print("\n")

type(str(list[0]))
