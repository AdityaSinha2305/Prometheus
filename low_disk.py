import psutil
import time
import os

# Function to check available disk space
def check_disk_space():
    disk_usage = psutil.disk_usage('/')
    return disk_usage.percent


# Function to create a file of specified size (in bytes)

def create_file(size):
    with open('dummy_file.txt', 'a') as f:
        f.write('a' * size)


# Set the threshold limit for disk space (in bytes)

# Set the threshold limit for disk space (in percent)
threshold_limit =  20 # 20 percent free space available

try:
    while True:
        disk_space_used = check_disk_space()
        print(f"Used disk space: {disk_space_used} %")
        free_space = 100 - disk_space_used
        print(f"Free disk space: {free_space} %")

        # Check if free space has reached the threshold limit
        if free_space < threshold_limit:
            print("Disk free space reached below 20%. Stopping execution.")
            break

        # Create a file of 1 GB to increase disk space
        create_file(500 * 1024 * 1024 )  # 500 MB


        print("----------------------------")
        time.sleep(5)  # Sleep for 5 seconds

except KeyboardInterrupt:
    print("\nExecution stopped by user.")


finally:
    # Cleanup: Remove the created file
    if os.path.exists('dummy_file.txt'):
        os.remove('dummy_file.txt')
