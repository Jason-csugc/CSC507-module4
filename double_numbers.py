import time
import os

INPUT_FILE = 'file1.txt'

def all_memory():
    with open(INPUT_FILE, 'r') as file:
        content = file.read()

    lines = content.splitlines()

    with open('all_memory.txt', 'w') as out:
        for line in lines:
            out.write(str(int(line) * 2) + '\n')


def each_line():
    with open('each_line.txt', 'w') as out:
        with open(INPUT_FILE, 'r') as file:
            for line in file:
                out.write(str(int(line) * 2) + '\n')

def split_memory():
       file_size = os.path.getsize(INPUT_FILE)

       with open('split_memory.txt', 'w') as out:
        with open(INPUT_FILE, 'r') as file:
            content1 = file.read(int(file_size/2))
            content2 = file.read()

        for line in content1.splitlines():
            out.write(str(int(line) * 2) + '\n')
        for line in content2.splitlines():
            out.write(str(int(line) * 2) + '\n')


 

def timer(func, name):
    start_time = time.time()
    func()
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Executed: {name}")
    print(f"Execution time: {elapsed:.2f} seconds")

def main():
    timer(all_memory, "In Memory")
    timer(each_line, "Each Row")
    timer(split_memory, "Split")


if __name__ == '__main__':
    main()