#Part 1
- An atomic operation is an operation that appears to the user(s) to appear instantaneously, making it immune to parallelism issues like race conditions.
- A mutex is a system-wide/multi-process lock.
- A semaphore is a mutex which allows access to at least one thread.
- A critical section is a section which only allows one thread of a process to run at a time, pausing all other threads invoked by the process to prevent them from interfering with the thread running the critical section.
