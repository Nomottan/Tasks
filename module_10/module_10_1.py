import time
import threading


def write_words(word_count, file_name):
    with open(file_name, "w", encoding='utf-8') as fn:
        for number in range(word_count):
            fn.write(f"Какое-то слово №{number}\n")
            time.sleep(0.1)
    return print(f"Завершилась запись в файл {file_name}")


startes_at = time.time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
ended_at = time.time()
print(f'Работа потоков {round(ended_at - startes_at, 4)}')

startes_at = time.time()
threads = [
    threading.Thread(target=write_words, args=(10, "example5.txt", )),
    threading.Thread(target=write_words, args=(30, "example6.txt", )),
    threading.Thread(target=write_words, args=(300, "example7.txt", )),
    threading.Thread(target=write_words, args=(100, "example8.txt", ))
    ]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

ended_at = time.time()
print(f'Работа потоков {round(ended_at - startes_at, 4)}')
