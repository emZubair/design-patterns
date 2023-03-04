from queue import Queue


def task(name: str, work_queue: Queue):
    if work_queue.empty():
        print(f"The task {name} has nothing to do")
        return

    while not work_queue.empty():
        limit = work_queue.get()
        print(f"Executing {limit} -- remaining:{work_queue}")
        total = 0
        print(f"The task '{name}' is running...")
        for x in range(limit):
            total += 1

        print(f"Task {name}, {total=}")


def main():
    work_queue = Queue()

    for work in [10, 12, 16, 9, 2]:
        work_queue.put(work)

    # synchronous tasks
    tasks = [(task, "One", work_queue), (task, "three", work_queue), (task, "Four", work_queue)]

    for _task, _name, _queue in tasks:
        _task(_name, _queue)


if __name__ == "__main__":
    print(f"Running {__name__}")
    main()
