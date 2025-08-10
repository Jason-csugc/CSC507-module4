import random
import time

OUTPUT_FILE = 'file2.txt'
TOTAL_NUMBERS = 1_000_000
MAX_VALUE = 32_767

def main():
    start_time = time.time()
    with open(OUTPUT_FILE, 'w') as file:
        for _ in range(TOTAL_NUMBERS):
            file.write(str(random.randint(0, 32767)) + '\n') # range mimics bash $RANDOM range
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Generated {TOTAL_NUMBERS} random numbers in '{OUTPUT_FILE}'.")
    print(f"Execution time: {elapsed:.2f} seconds")

if __name__ == '__main__':
    main()
 # type: ignore