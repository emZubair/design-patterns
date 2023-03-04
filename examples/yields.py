"""
A yield statement turns a function into a generator.
A generator function is like any other python function, but when `yield` statement
is executed, control is returned to the caller. Control is given back to the
generator by calling `next` on it, and it has its state before the yield intact
"""

# Testing Concurrency
from queue import Queue


def task(name: str, work_queue: Queue):
    if work_queue.empty():
        print(f"The task {name} has nothing to do")
        return

    while not work_queue.empty():
        limit = work_queue.get()
        total = 0
        print(f"The task '{name}' is running...")
        for x in range(limit):
            total += 1
            yield

        print(f"Task {name}, {total=}")


def main():
    work_queue = Queue()

    for work in [10, 12, 3, 9, 2, 44, 23]:
        work_queue.put(work)

    # synchronous tasks
    tasks = [task("One", work_queue), task("three", work_queue), task("Four", work_queue)]

    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True


if __name__ == "__main__":
    print(f"Running {__name__}")
    main()
