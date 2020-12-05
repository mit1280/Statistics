#!/bin/python3

import math
import os
import random
import re
import sys


class Multiset:
    l=[]
    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.l.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if val in self.l:
            self.l.remove(val)

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        if val in self.l:
            return True
        return False
    
    def __len__(self):
        return len(self.l)

    
if __name__ == '__main__':  
    m=Multiset()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "add":
            m.add(params[0])
        elif shape_name == "query":
            p=m.__contains__(params[0])
            fptr.write("%s\n" % p)
        elif shape_name == "remove":
            m.remove(params[0])
        elif shape_name == "size":
            p=m.__len__()
            fptr.write("%s\n" % p)
        else:
            raise ValueError("invalid shape type")
    fptr.close()
