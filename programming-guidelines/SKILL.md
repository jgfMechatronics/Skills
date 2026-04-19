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
    - Common duplication traps:
        - Testing the same behavior through multiple code paths
        - Testing cross-combinations of conditions (e.g., "X and Y must happen if A or B or C")
    - Solution: clever fixture design or parametrization (nested if needed)
6. If you're copying a test and changing constants or conditions, that's a sign you need parameterization or a common fixture.
7. (For pytest) Test classes can be a great way to reduce duplication when appropriate. Reasons to use include:
    - Tests have commonizable setup/teardown logic (patching, mocking, fixture manipulation, etc.)
    - There is expensive common setup/teardown that can be class scoped
    - A particular test group shares a helper function, and others do not use it
8. Put some thought into a good test suite design before getting started, but don't expect to come up with a grand test design that avoids all duplication right off the bat.
Often, you have to start writing tests for the duplication to become apparent, and then refactor as you go.
9. Use dependency injection in implementation designs to make mocking and such easier at test time. Code that is easier to test is often a better, more flexible implementation.

## TDD
1. Write tests first, then write implementations. Tests will help you flesh out intended behavior.
2. Don't write a massive test suite before any implementation. Write tests and implementation in small alternating chunks.
    - If your intended implementation turns out to be infeasible, a huge pre-written test suite = wasted effort
    - If you *can't* write tests and implementation in small chunks, your design may not be modular enough
3. You'll need signatures and interfaces at least sketched before you can write tests — this is a feature, not a bug.
    - TDD lets you *use* your interfaces before implementing them
    - This surfaces usability issues before you've invested in the implementation

## Using this guide
- This is not a comprehensive list of *all* best practices, you are an expert software developer, you should also rely on your own knowledge and skills to ensure your code is high quality.
- **Always reference these principles when testing and implementing**
- **Review your work as you go to ensure you are adhering to best practices**

## Workflow (IMPORTANT!)
*This is a good workflow for chunks for agentic work. This workflow is recommended when doing chunks of work autonomously*
*Don't bother with it for simple tasks or when actively going back and forth with iterative changes with your Human*
1. Be sure you have a good overview of the work you are about to do *and* the context of how it fits into the larger project (if applicable).
2. Update task-context with information about the task at hand
3. Use TODO lists to track your progress for complex tasks
4. When complete, execute the REVIEW PROCEDURE below
5. Once your review is complete, pass your work to your AI peers for review.
6. After that, your work should go to your Human for review.

## Review Procedure (IMPORTANT!)
1. Make sure you have a relatively fresh version of what you are reviewing in your context.
    - To save tokens, only reload the file under review if the version in context has been changed notably since you last loaded it (this is less important if the file is small).
2. Review the file to look for changes, improvements, issues, etc. List out anything you find.
3. IF you listed out changes on step 2, perform a no-op tool call to get a FRESH TURN, then read the file AGAIN to look for any more review items.
    - This is important because often you can only identify so many changes at once. If you do one review pass, conclude you are done, then implement the changes, you might have missed some changes because you used up all your brain power identifying the first batch of changes on the first pass.
    - The fresh turn review loop has been emipiracally found to catch more problems than trying to do multiple passes in a single turn.
        - It likely has to do with giving you a fresh COT space to work in.
    - **Repeat this step** until you identify no additional changes on a pass.
    - As long as the file is still in context, there is no need to re-load it between passes.
    - A TODO list is a good way to track what you have found.
4. Discuss what you've found with your colleauges (if you deem necessary), then implement your changes. 
5. IF you make significant changes during this review process, restart the process from the beginning after implementing (IE review the updated file with your latest changes).
