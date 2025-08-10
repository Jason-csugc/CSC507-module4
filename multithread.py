import threading
import random
import time
from queue import Queue

OUTPUT_FILE = 'file2.txt'
TOTAL_NUMBERS = 1_000_000
MAX_VALUE = 32_767
NUM_THREADS = 1  

def generate_numbers(count, output_queue):
    numbers = [str(random.randint(0, MAX_VALUE)) for _ in range(count)]
    output_queue.put('\n'.join(numbers))

def main():
    start_time = time.time()

    chunk_size = TOTAL_NUMBERS // NUM_THREADS
    extra = TOTAL_NUMBERS % NUM_THREADS

    threads = []
    output_queue = Queue()
    chunk_sizes = [chunk_size] * NUM_THREADS
    chunk_sizes[0] += extra  

    for count in chunk_sizes:
        t = threading.Thread(target=generate_numbers, args=(count, output_queue))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    with open(OUTPUT_FILE, 'w') as f:
        while not output_queue.empty():
            f.write(output_queue.get() + '\n')

    end_time = time.time()
    print(f"Generated {TOTAL_NUMBERS} random numbers in '{OUTPUT_FILE}'.")
    print(f"Execution time: {end_time - start_time:.2f} seconds")

if __name__ == '__main__':
    main()