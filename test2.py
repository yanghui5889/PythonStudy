import multiprocessing as mp
import os

def do():
    print("pid is : %s ..." % os.getpid())

if __name__ == '__main__':
    print("parent id is : %s ..." % os.getpid())
    p = mp.Process(target=do, args=())
    p.start()