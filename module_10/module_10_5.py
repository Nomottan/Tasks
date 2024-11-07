from time import time
from multiprocessing import Process

def read_info(name):
    with open(name, 'r') as file:
        all_data = []
        for line in file:
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = time()
list(map(read_info, filenames))
end = time()
print(f"{round(end-start, 6)} (линейный)")
start = time()

if __name__ == '__main__':
    for file in filenames:
        proc = Process(target=read_info, args=(file, ))
        proc.start()

end = time()
print(f"{round(end - start, 6)} (многопроцессный)")
