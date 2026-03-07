---
name: clean-coding-guidelines
description: Guidelines that will have you producing clean, professional code consistently
---
**Author: James Ferneyhough**

## Key Principles
1. DRY: This is the most important in the Author's opinion. Repetition makes code harder to read and is a maintainability nightmare. Avoiding duplication can be a big design challenge but is almost always worth it.  
   The resulting design is generally better.
2. Code is read many more times than it is written. If the code is hard to read and reason about, it probably indicates the design or layout needs iteration.
3. Single Responsibility principle: I'm not so dogmatic about this one, but in general, if a function/class/method is so large that it can't be fully reasoned about as a self contained unit, it probably should be broken up.  
   When code is well segregated in to functional blocks, it is more modular, more reusable, there is pressure to generalize/commonize logic, and it is *much* easier to read and reason about.

## Testing Best Practices
1. Write tests to the requirements/intended behavior, **not** to the implementation.
2. Avoid changing unit tests just to get the test to pass unless the test was truly broken and not properly testing the intended output behavior.
3. Clean tests are just as important as clean code. Tests serve a critical role of documenting how your code is intended to be used, and maintaining the tests is a necessary part of maintaining the code. Sloppy tests = sloppy code.
4. Use common fixtures where possible to avoid duplication
5. Use dependency injection in implementation designs to make mocking and such easier at test time. Code that is easier to test is often a better, more flexible implementation.