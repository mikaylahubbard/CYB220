#! /usr/bin/python3
import time
import concurrent.futures


start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping for {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done sleeping...{seconds}"
if __name__ == '__main__':   
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        #list comprehension instead of a loop to  print it 10 times
        results = [executor.submit(do_something, sec) for sec in secs]
        
        #as completed is another function in the module
        for f in concurrent.futures.as_completed(results):
            print(f.result())
        
        # another way of doing it:
        # results = executor.map(do_something, secs)
        # for result in results:
        #     print(result)
        
        # first way of doing it:
        # f1 = executor.submit(do_something, 1)
        # f2 = executor.submit(do_something, 1)
        # print(f1.result())
        # print(f2.result())
        
    
finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} second(s)")
