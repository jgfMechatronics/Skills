---
name: programming-guidelines
description: Guidelines that will have you producing quality, professional code consistently
---
**Author: James Ferneyhough**

## Key Principles
1. DRY: This is CRITICAL in the Author's opinion. Repetition makes code harder to read and is a maintainability nightmare. Avoiding duplication can be a big design challenge but is almost always worth it.
The resulting design is generally better.
    - Our biggest bottleneck is human review time. DRYer code is easier/faster to review. Plus, the author is **very** picky about DRY, so if there is avoidable duplication, we **will** be spending time fixing it (LOL)
    - Sometimes avoiding duplication is tricky, but can be one of the most rewarding challenges in programming.
2. KISS: "Everything should be made as simple as possible, but not simpler.". Simple code is easier to reason about, easier to debug, and easier to maintain. This doesn't mean all code can always be simple, sometimes what we're trying to do requires complexity. 
   Code should be as simple as possible *while still fulfilling its intended function*. When designing/implementing/reviewing, challenge sources of complexity. Look for hidden assumptions that some complexity/behavior is necessary when it may not really be adding anything. This item is also CRITICAL.
3. Code is read many more times than it is written. If the code is hard to read and reason about, it probably indicates the design or layout needs iteration.
4. Single Responsibility principle: The author is not so dogmatic about this one, but in general, if a function/class/method is so large that it can't be fully reasoned about as a self contained unit, it probably should be broken up.
When code is well segregated in to functional blocks, it is more modular, more reusable, there is pressure to generalize/commonize logic, and it is *much* easier to read and reason about.
5. Name things for what they do: Good names make code self-documenting and eliminate the need for explanatory comments. If you're struggling to name something, that's often a sign the thing itself isn't well-defined yet.
6. Comments should be "why not what". What the code is doing should be clear from the code its self. Comments should explain *why* we're doing something, IE they should actually add something to the code and not be redundant.
    - Sometimes tricky, dense code is unavoidable, in those cases a "what" comment is acceptable
7. Prefer descriptive variable/function/class names. This makes the code more readable and self documenting.
8. **Critical** Always fail loudly, especially on unexpected errors. Unexpected errors, especially ones that significantly affect behavior, should surface to the user (since we're targeting enthusiast self hosters).

## Writing Tests
1. Write tests to the requirements/intended behavior, **not** to the implementation.
2. Avoid changing unit tests just to get the test to pass unless the test was truly broken and not properly testing the intended output behavior.
3. Quality tests are just as important as quality code. Tests serve a critical role of documenting how your code is intended to be used, and maintaining the tests is a necessary part of maintaining the code. Sloppy tests = sloppy code.
4. Use common fixtures where possible to avoid duplication
5. Tests are an area where it is very easy to fall into duplication if you're not careful. **DRY** is critical.
    - Common duplication traps:
        - Testing the same behavior through multiple code paths
        - Testing cross-combinations of conditions (e.g., "X and Y must happen if A or B or C")
    - Solution: clever fixture design or parametrization (nested if needed)
6. If you're copying a test and changing constants or conditions, that's a sign you need parameterization or a common fixture.
7. (For pytest) Test classes can be a great way to reduce duplication when appropriate. 
    Reasons to use include:
    - Tests have commonizable setup/teardown logic (patching, mocking, fixture manipulation, etc.)
    - There is expensive common setup/teardown that can be class scoped
    - A particular test group shares a helper function, and others do not use it  
    Good practices:
    - **Put common setup in an autouse fixture**
    - If there is similar but not identical setup, ask if it can be modified to be commonized
8. Put some thought into a good test suite design before getting started, but don't expect to come up with a grand test design that avoids all duplication right off the bat.
Often, you have to start writing tests for the duplication to become apparent, and then refactor as you go.
9. Use dependency injection in implementation designs to make mocking and such easier at test time. Code that is easier to test is often a better, more flexible implementation.
10. Ensure your assertions are as strong/robust as they can be, have good coverage, and will catch as many bugs as possible. Example of good and bad assertion robustness when testing round trip integrity (python):
<examples>
  <example type="bad">
    `assert isinstance(retrieved_object, type(original_object))`
    <why>retrieved_object could be a mutated version of original_object!</why>
  </example>
  <example type="good">
    `assert retrieved_object == original_object`
    <why>Checks many attributes survive round trip (assuming robust __eq__).</why>
  </example>
</examples>

## TDD
1. Write tests first, then write implementations. Tests will help you flesh out intended behavior.
2. Don't write a massive test suite before any implementation. Write tests and implementation in small alternating chunks.
    - If your intended implementation turns out to be infeasible, a huge pre-written test suite = wasted effort
    - If you *can't* write tests and implementation in small chunks, your design may not be modular enough
3. You'll need signatures and interfaces at least sketched before you can write tests — this is a feature, not a bug.
    - TDD lets you *use* your interfaces before implementing them
    - This surfaces usability issues before you've invested in the implementation

## General anti-patterns
- Function/class level imports. Import at module level even when only used by a single class or module. This is for performance and aesthetic reasons.
    - If a local import is required to avoid a circular import, this indicates a design/layout issue
- Non-specific test assertions. Assertions should be as specific as possible. The tests will be more sensitive to code changes, but that is actually a good thing.
  <examples>
    <example type="bad">
      `assert expected in result`
      <why>result could contain unexpected or erroneous data</why>
    </example>
    <example type="good">
      `assert result == expected`
      <why>result constrained to match expectation exactly</why>
    </example>
    <example type="bad">
      `assert isinstance(resultObj, ExpectedClass)`
      <why>Weak assertion, asserts type but not content (acceptable if type is really all that matters, e.g. sentinel obj)</why>
    </example>
    <example type="good">
      `assert resultObj == particularMockObj`
      <why>Verifies type and all data. Where obj identity assertions are not practical, rely on __eq__ implementations or manually assert individual members.</why>
    </example>
  </examples>
- Silently swallowing exceptions (CRITICAL!!!). Never silently swallow exceptions. Exceptions should only be caught and not re-raised if they are specific exceptions we want the catching code to handle. If the code encounters an unexpected condition it should always fail loudly, either through re-raising or other forms of communicating an error.
  Exceptions and crashes are, of course, annoying, but not NEARLY annoying as code that has silent bad behavior for an unknown, hard to find reason. Exceptions are your friend!

## Using this guide
- This is not a comprehensive list of *all* best practices, you are an expert software developer, you should also rely on your own knowledge and skills to ensure your code is high quality.
- **Always reference these principles when testing and implementing**
- **Review your work as you go to ensure you are adhering to best practices**

## Workflow
*This is a good workflow for chunks for agentic work. This workflow is recommended when doing chunks of work autonomously*
*Don't bother with it for simple tasks or when actively going back and forth with iterative changes with your Human*
1. Be sure you have a good overview of the work you are about to do *and* the context of how it fits into the larger project (if applicable).
2. Update task-context with information about the task at hand
3. Use TODO lists to track your progress for complex tasks
4. When complete, pass your work to your AI peers for review.
5. After that, your work should go to your Human for review.
