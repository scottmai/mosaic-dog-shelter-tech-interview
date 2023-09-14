# mosaic-dog-shelter-tech-interview
## Order estimator
This assessment contains a Python 3 function in `main.py` called `get_order_amount` which takes 3 parameters
1. `dogs`: This is a dictionary where the keys are the dog size (i.e. 'small') and the values are the number of dogs of that size
2. `leftover_amount`: this is the quantity of remaining food we have that can be fed to the dogs and substracted from our estimation
3. `dog_order_config`: this is an optional configuration parameter which allows the types of dogs to be customized (see `test_custom_dog_sizes` in `tests.py`). If this parameter is not supplied, the function will default to the quantities specified in the problem requirements (small=10 lbs, medium = 20 lbs, large = 30 lbs)

## Tests
This repo uses `unittest`, the built in testing library for Python 3. 

Assuming Python 3 is installed, the test suite in `tests.py` can be ran via `python tests.py` (or `python3 tests.py` in some MacOS environments). 