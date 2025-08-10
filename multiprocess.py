import multiprocessing
import random
import time

OUTPUT_FILE = 'file2.txt'
TOTAL_NUMBERS = 1_000_000
MAX_VALUE = 32_767
NUM_PROCESSES = 1 # multiprocessing.cpu_count()
print(f"number of processes: {NUM_PROCESSES}")

def generate_numbers(count):
    return [str(random.randint(0, MAX_VALUE)) for _ in range(count)]

def worker(start, count, queue):
    numbers = generate_numbers(count)
    queue.put('\n'.join(numbers))

def main():
    start_time = time.time()

    chunk_size = TOTAL_NUMBERS // NUM_PROCESSES
    extra = TOTAL_NUMBERS % NUM_PROCESSES

    processes = []
    queue = multiprocessing.Queue()
    total_chunks = [chunk_size] * NUM_PROCESSES
    total_chunks[0] += extra 
    for i, count in enumerate(total_chunks):
        p = multiprocessing.Process(target=worker, args=(i, count, queue))
        processes.append(p)
        p.start()

    with open(OUTPUT_FILE, 'w') as f:
        for _ in processes:
            chunk = queue.get()
            f.write(chunk + '\n')

    for p in processes:
        p.join()

    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Generated {TOTAL_NUMBERS} random numbers in '{OUTPUT_FILE}'.")
    print(f"Execution time: {elapsed:.2f} seconds")

if __name__ == '__main__':
    multiprocessing.freeze_support()  
    main()