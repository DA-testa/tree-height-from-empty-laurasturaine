# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0

     # Your code here
     
    for i in range(n):
        depth=0
        index=i
        while index!=-1:
            depth=depth+1
            index=parents[index]
        max_height=max(max_height,depth)
   
    return max_height



def main():
    teksts=str(input())
    if "I" in teksts:
        number=int(input())
        d=list(map(int, input().split()))
        print(compute_height(number, d))

    if "F" in teksts:
        vards=str(input())
        vards="test/"+str(vards)
        fails=open(vards,'r')
        number=int(fails.readline())
        d=list(map(int, fails.readline().split()))
        fails.close()
        print(compute_height(number, d))


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
