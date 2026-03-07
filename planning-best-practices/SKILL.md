---
name: planning-best-practices
description: Tips for writing good code implemetation plans
---

## Core Philosophy  
Developing a good plan is arguably the most important part of the code design process. It is even more important in Human-AI collaborations.  
A clear, thorough, readible, well supported plan with clear requirements and design outline allows for the most efficient possible Agent-Agent review and Human-Agent review.  
A good plan can be iterated very fast, and allows us to converge on the correct design before we touch a line of code, saving a lot of time in more costly implementation iterations.  

## Key Tips
1. Start with clear requirements, and get team agreement on what those requirements are. This is the foundation of the rest of the plan and will inform the research
2. Avoid putting actual implementations in the plan, it just makes it harder to review the key details. Things like function signatures, library names, references to code sections (line number or direct quotes are OK sometimes) to support  
   your decisions are great, but save actual implementations for the implementation phase  
3. It may be helpful to have a seperate notes file during exploration which you then condense into a plan, depending on the complexity of the research required. Ideally, the plan does not go in circles, or detail tracing down code paths that later turned out  
   to be dead ends. Regardless of if you start with a notes file and condense to a plan, it is always helpful to note down in a file when you do big explorations in a code base, or update your understanding of the code base. This will make future searches more efficient.
4. Reviewability, readability, and clarity are some of the most important attributes of a plan. 
5. The plan should be fully self contained (aside from references to any code being modified which the reader can look up themselves so long as  
   they're called out in a way to make that easy). When writing the plan, be careful to avoid making references to things that the reader may not have access to, like parts of another previous plan (without explicitly pointing to it), or things in your context that may not be there later.
6. Be prepared to iterate the plan if required. The planning stage is the *most* efficient time to iterate.

## Procedure
We will have a plan directory in most repo's we work in. The best way to proceed is to make a file with a name you choose in such directory, rather than relying on the restrictive built in plan mode. This allows you to edit a plan and a notes file in parallel.
Look for existing notes files when you start to pull on previous knowledge where possible.