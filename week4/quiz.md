# CS50 - Introduction to AI with Python

## Week 4 - Learning

### Quiz

1. Categorise the following: A social network's AI uses existing tagged photos of people identify when those people appear in new photos

Options:

- This is an example of supervised learning
- This is an example of reinforcement learning
- This is an example of unsupervised learning
- This is not an example of machine learning

Answer: Supervised learning

2. Imagine a regression AI that makes the following predictions for the following 5 data points. What is the total L2 loss across all of these data points?

The true output is 2 and the AI predicted 4.
The true output is 4 and the AI predicted 5.
The true output is 4 and the AI predicted 3.
The true output is 5 and the AI predicted 2.
The true output is 6 and the AI predicted 5.

Answer
$(2-4)^2 + (4-5)^2 + (4-3)^2 + (5-2)^2 + (6-5)^2$
= $4 + 1 + 1 + 9 + 1$
= $16$

3. If Hypothesis 1 has a lower L1 loss and a lower L2 loss than Hypothesis 2 on a set of training data, why might Hypothesis 2 still be a preferable hypothesis?

Hypothesis 1 might be the result of regularization.
Hypothesis 1 might be the result of overfitting.
Hypothesis 1 might be the result of loss.
Hypothesis 1 might be the result of cross-validation.
Hypothesis 1 might be the result of regression.

Answer:
H1 might be the result of overfitting.

4. In the $\epsilon$-greedy approach to action selection in reinforcement learning, which of the following values of $\epsilon$ makes the approach identical to a purely greedy approach?

ε = 0
ε = 0.25
ε = 0.5
ε = 0.75
ε = 1

Answer: ε = 0
