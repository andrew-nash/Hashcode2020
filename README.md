# Hashcode 2020 Qualification Round Submission
##  24,641,287 Points
### UCC Team Demons

## Approach
The question states, given a collection of libraries, we need to to determine an optimal ordered subset from this collection, in order to maximise the total score obtained. Each library has a registration period before it can begin contributing a score, and no more than one library can be registering at any one time. See the full question here.


The main idea behind our approach is, given the list of currently available libraries and the amount of time remaining, we calculate for every library an average score per unit time that this library would provide, should it be the one we choose next. The average is caculated over the time from the current moment in time (start of the registration process) to the end of the entire time window. The average is weighted, in order to penalise long registration times, by making the average $\frac{\text{score}}{\text{penalty}\(\text{registration time}}\)+\(\text{time remaining} - \text{registration time}\)$.

The default penalty that we used was 2, which we varied for multiple submissions, taking the maximum score for each. Hence, the included script may not achieve the exact score quoted above initially, without some variation in the penalty value. (I believe that some of the values we used included 1.25, 1.5, 3, 2.5, etc).

Included are the output files that obtained the exact score.

Note that this script is particularly slow to run on test case D, up to potentially a few minutes. Will look into improving this.



