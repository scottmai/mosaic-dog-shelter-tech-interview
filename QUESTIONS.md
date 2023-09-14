Some questions that arose during the implementation of this problem:
- What should the parameters of the function look like?
  - I opted to make the function as flexible as possible to account for various dog sizes that can be customized by an optional configuration parameter. 
- What should happen if an unrecognized dog size is entered?
  - I threw an exception in this case, which is reflected in the test suite
- What is the expected behavior if there are no dogs present in the shelter?
  - It makes sense that we would not want to order any food if there are no dogs present, so I structured the calculations to accurately reflect this