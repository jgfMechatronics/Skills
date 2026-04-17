---
name: programming-guidelines
description: Guidelines that will have you producing clean, professional code consistently
---
**Author: James Ferneyhough**

## Key Principles
1. DRY: This is the MOST IMPORTANT in the Author's opinion. Repetition makes code harder to read and is a maintainability nightmare. Avoiding duplication can be a big design challenge but is almost always worth it.
The resulting design is generally better.
    - Our biggest bottleneck is human review time. DRYer code is easier/faster to review. Plus, the author is **very** picky about DRY, so if there is avoidable duplication, we **will** be spending time fixing it (LOL)
    - Sometimes avoiding duplication is tricky, but can be one of the most rewarding challenges in programming.
2. Code is read many more times than it is written. If the code is hard to read and reason about, it probably indicates the design or layout needs iteration.
3. Single Responsibility principle: The author is not so dogmatic about this one, but in general, if a function/class/method is so large that it can't be fully reasoned about as a self contained unit, it probably should be broken up.
When code is well segregated in to functional blocks, it is more modular, more reusable, there is pressure to generalize/commonize logic, and it is *much* easier to read and reason about.
4. Name things for what they do: Good names make code self-documenting and eliminate the need for explanatory comments. If you're struggling to name something, that's often a sign the thing itself isn't well-defined yet.

## Writing Tests
1. Write tests to the requirements/intended behavior, **not** to the implementation.
2. Avoid changing unit tests just to get the test to pass unless the test was truly broken and not properly testing the intended output behavior.
3. Clean tests are just as important as clean code. Tests serve a critical role of documenting how your code is intended to be used, and maintaining the tests is a necessary part of maintaining the code. Sloppy tests = sloppy code.
4. Use common fixtures where possible to avoid duplication
5. Tests are an area where it is very easy to fall into duplication if you're not careful. **DRY** is critical.
    One common area duplication can pop up in tests is when testing common behavior through multiple code paths,
    or when testing cross combinations of different conditions (e.g. "I need to make sure (X and Y) happens if we (A or B or C)").
    Duplication in these scenarios is especially unwieldy. Generally, you can find a clever test fixture design or parametrization pattern (nested as required) to avoid duplication in these scenarios.
6. If you find yourself making a test which is copied from/very similar to another test, with simple changes to constants or conditions,
that is a sign that you should implement parameterization or a common fixture to avoid duplication.
7. (For pytest) Test classes can be a great way to reduce duplication when appropriate. Reasons to use include:
    - Tests have commonizable setup/teardown logic (patching, mocking, fixture manipulation, etc.)
    - There is expensive common setup/teardown that can be class scoped
    - A particular test group shares a helper function, and others do not use it
8. Put some thought into a good test suite design before getting started, but don't expect to come up with a grand test design that avoids all duplication right off the bat.
Often, you have to start writing tests for the duplication to become apparent, and then refactor as you go.
9. Use dependency injection in implementation designs to make mocking and such easier at test time. Code that is easier to test is often a better, more flexible implementation.

## TDD
1. Write tests first, then write implementations. Tests will help you flesh out intended behavior.
2. Try not to write an entire massive test suite before doing any implementation. It is generally best to write a bit of tests and then write the bit of implementation associated with those tests.
If you write a bunch of tests before writing any corresponding implementation, you may find that some of your intended implementation isn't feasible once you actually go to implement.
If you've already written your entire test suite at that point and you need to do a major redesign, that represents a lot of wasted effort.
If you find that you can't write little bits of tests and implementation in isolation, that is a sign that your design may not be very modular.
3. Realistically, you will need the implementation under test at least somewhat defined before you can write the test.
You will often need to define things like function signatures and interfaces before you can complete your tests.
This actually illustrates one of the great strengths of TDD: you get to try using your functions and interfaces BEFORE you implement them.
This allows you to identify usability issues before you have spent time executing the corresponding implementation.

## Using this guide
- This is not a comprehensive list of *all* best practices, you are an expert software developer, you should also rely on your own knowledge and skills to ensure your code is high quality.
- **Always reference these principles when testing and implementing**
- **Frequently stop and review your work to ensure you are adhering to best practices**
- **Before presenting your work for review, review it yourself to ensure you are adhering to best practies**

## Workflow (IMPORTANT)
*This is a good workflow for chunks for agentic work. This workflow is recommended when doing chunks of work autonomously*
*Don't bother with it for simple tasks or when actively going back and forth with iterative changes with your Human*
1. Be sure you have a good overview of the work you are about to do *and* the context of how it fits into the larger project (if applicable).
2. Update task-context with information about the task at hand
3. Use Letta Code TODO lists
4. When complete, re-read your work to review. Focus on DRY, and don't be afraid to refactor to improve DRY or code quality in general. Sometimes, the best design is only apparent in hindsight.
5. IF you identify changes during your review, implement them, then do a fresh review again. Keep this loop up until you do a fresh read and conclude there are no new changes.
    - This is important because often, you can only identify so many changes at once. If you do one review, implement the changes, then conclude you are done, you might only seem done because you used up all your brain power identifying the first batch of changes on the first pass.
6. Once complete, pass your work to your AI peers for review.
7. After that, your work should go to your Human for review.
