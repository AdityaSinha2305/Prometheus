import multiprocessing
import time
import psutil

def cpu_intensive_task():
    while True:
        result = 1 + 1

if __name__ == "__main__":
   
    num_cores = multiprocessing.cpu_count()
   
    processes = []
    for _ in range(num_cores):
        process = multiprocessing.Process(target=cpu_intensive_task)
        process.start()
        processes.append(process)

    try:
        while True:
            cpu_utilization = psutil.cpu_percent()
            print(f"Current CPU Utilization: {cpu_utilization}%")
            time.sleep(1)

    except KeyboardInterrupt:
        for process in processes:
            process.terminate()
            process.join()