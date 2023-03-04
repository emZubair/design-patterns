import time
from queue import Queue


def task(name: str, work_queue: Queue):
    if work_queue.empty():
        print(f"The task {name} has nothing to do")
        return

    while not work_queue.empty():
        limit = work_queue.get()
        total = 0
        print(f"The task '{name}' is running...")
        time.sleep(limit)
        yield

        print(f"Task {name}, {total=}")


def main():
    work_queue = Queue()

    for work in [5, 4, 3, 9, 2, 7, 6]:
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