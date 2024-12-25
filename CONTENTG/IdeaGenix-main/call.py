import os

# File path for storing memories
MEMORY_FILE = 'memories.txt'

# Function to remember information
def remember(key, value):
    with open(MEMORY_FILE, 'a') as f:
        f.write(f'{key}: {value}\n')

    print(f'Remembered: {key} -> {value}')

# Function to recall information
def recall(key):
    try:
        with open(MEMORY_FILE, 'r') as f:
            for line in f:
                if line.startswith(key):
                    _, value = line.strip().split(': ', 1)
                    return value
        return f'No memory found for "{key}"'
    except FileNotFoundError:
        return 'No memories found.'

