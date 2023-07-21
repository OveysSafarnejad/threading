# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.

import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(1)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    # The x thread would be a non-daemon thread if we don't pass daemon=True.
    # So the main program should wait for non-daemon threads.
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : before sleep")

    # The program will switch to the x thread because the main thread is going
    # to be blocked
    # time.sleep(2)

    logging.info("Main    : wait for the thread to finish")

    # To tell on thread to wait
    # for another thread to finish, you call.join().If you uncomment that line,
    # the main thread will pause and wait for the thread x to complete running.
    x.join()
    logging.info("Main    : all done")
    logging.info("Main    :" + 100 * "-")

# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.- #
# Use threadpool context manager
# It will automatically call the join() to wait for finishing all threads.


import concurrent.futures

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))
