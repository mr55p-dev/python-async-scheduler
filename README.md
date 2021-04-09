# python-async-scheduler
A small scheduler which is intended to run asynchronously alongside a WSGI.
Jobs can be implemented with the Job class and these are run in the context of a target function, specified at the scheduler level.

## Setup
1) ```pip install light-async-scheduler``` to install the package.
2) ```from async_scheduler import Scheduler``` to get the scheduler.
3) ```scheduler = Scheduler(target_coroutine_or_function)``` configures the function the scheduler will use.
4) ```scheduler.start()```

This project is a work in progress and so any issues or features to add would be happily appreciated!
You can find this project [here](https://github.com/mr55p-dev/python-async-scheduler).
