# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
    max_height = 0
    tree=[[]for i in range(n)]
    sakne=None
    for i in range(n):
        if parents[i]==-1:
            sakne=1
            else:
                tree[parents[i]].append(i)
    # Your code here
    return max_height

    defdfs(node):
        if not tree[node]:
            return 0
            else:
                heights=[dfs(child) for child in tree[node]]
                return+1max(heights)

                return dfs(root)



def main():
    n=int(input())
    parents=list(map(int,input().split()))

    print(compute_height(n,parents))
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
large input
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
