from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)