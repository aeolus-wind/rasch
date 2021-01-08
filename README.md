Implements the Rasch method for dichotomous data.
This is the most basic version where all students take all
test questions and they can either be correct or incorrect.
For each student there is a parameter theta

   - for larger theta, the student is more skilled
For each question there is a parameter delta
   - for larger delta the question is more difficult  
   
For the optimization, it uses the Joint Maximum Likelihood estimator
This is a classic method using the Newton-Raphson method.
I referenced Invariant Measurement

Future additions may include 
  - partial credit 
  - categories (questions are grouped)
  - more than two responses
  - missing responses
  - metrics to check goodness of fit