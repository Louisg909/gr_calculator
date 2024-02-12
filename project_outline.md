# Project Outline
## Scope



---
## Most basic process:
1. Equation is inputted
2. Equation is parsed with elements and operators
3. Algebraic simplification is done **Breakdown of how this could be done bellow**
4. Values and variables are put in from the saved variables
5. Check for elements that have some form of saved values. If none, then return this
6. Do operations between these elements and the still-algebraic elements, creating new elements if need be.
7. Return equation, as well as the definitinos of any new elements created (Defined elements can have algebraic properties inside them. If an element is undefined and has to interact with an element that is defined, the unkown properties of the element, such as size, can be automatically worked out)


### Equation input


### Parsing


### Algebraic Simplification


### Value inputting
Input objects where they can be put in? Objects don't have to *look* like Einstein Notation... something to keep in mind... just needs to be something that is readable to the computer. Only worry about the properties and relations - don't need to think of anything else


### Checking elements
This can be done prehaps with a simple booleon showing whether it has internals or not?


### Opprations between elements
Right... this is where complexities start going in. need to work out how to do this in complement with the design of the objects being used.


### Returning the equation in a readable format, and showing definitions of new elements.

