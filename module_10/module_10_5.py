from time import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        data = file.readline()
        while data:
            data = file.readline()
            all_data.append(data[0:-1])


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = time()
list(map(read_info, filenames))
end = time()
print(f"{round(end-start, 6)} (линейный)")
start = time()

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)


end = time()
print(f"{round(end - start, 6)} (многопроцессный)")
