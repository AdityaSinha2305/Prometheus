import psutil
import os
import time

def increase_memory_usage():
    # Get current memory usage
    current_memory = psutil.virtual_memory().percent

    # Print current memory usage
    print("Current Memory Usage: {}%".format(current_memory))

    # Check if memory usage is less than 85%
    if current_memory < 70:
        # Allocate memory until it reaches 85%
        memory_to_allocate = psutil.virtual_memory().total * 0.01  # 1% of total memory
        memory_list = []
        while True:
            memory_list.append(bytearray(int(memory_to_allocate)))
            current_memory = psutil.virtual_memory().percent
            print("Current Memory Usage: {}%".format(current_memory))
            if current_memory >= 85:
                break
            time.sleep(3)
            memory_to_allocate *= 2  # Double the memory allocation each time
    else:
        print(f"Memory usage is already at 85% or more, stopping.")

if __name__ == "__main__":
    increase_memory_usage()
