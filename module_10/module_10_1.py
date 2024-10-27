from time import sleep
import threading


def write_words(word_count, file_name):
    with open(file_name, "w", encoding='utf-8') as fn:
        for number in range(word_count):
            fn.write(f"Какое-то слово №{number}\n")
            sleep(0.1)
    return print(f"Завершилась запись в файл {file_name}")


write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

thread = threading.Thread(target=write_words(10, "example5.txt"))
thread_0 = threading.Thread(target=write_words(30, "example6.txt"))
thread_1 = threading.Thread(target=write_words(200, "example7.txt"))
thread_2 = threading.Thread(target=write_words(100, "example8.txt"))
thread.start()
thread_0.start()
thread_1.start()
thread_2.start()
thread.join()
thread_0.join()
thread_1.join()
thread_2.join()

