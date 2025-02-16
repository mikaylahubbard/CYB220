#! /usr/bin/python3
import multiprocessing
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print("Done sleeping...")

# do_something()    
# do_something()
# create processes
# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)
# #start the processes
# p1.start()
# p2.start()
# # this makes the processes finish before continuing on with the script
# p1.join()
# p2.join()
processes = []
if __name__ == '__main__':
    for _ in range(10):
        # start all the processes and store them so you can join after
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    
finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
