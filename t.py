import time
import argparse

# Parse arguments
parser = argparse.ArgumentParser('RGB test')
parser.add_argument("-ch0","--ch0", type=int, help="red", default = 0)
parser.add_argument("-ch1","--ch1", type=int, help="red", default = 0)
parser.add_argument("-ch2","--ch2", type=int, help="green", default = 0)
parser.add_argument("-ch3","--ch3", type=int, help="blue", default = 0)
parser.add_argument("-c", "--complete", type=str, help="all color component in one", default = "  ")
args = parser.parse_args()

ch0 = args.ch0
ch1 = args.ch1
ch2 = args.ch2
ch3 = args.ch3

print("Channel 0: " + str(ch0))
print("Channel 1: " + str(ch1))
print("Channel 2: " + str(ch2))
print("Channel 3: " + str(ch3))
    