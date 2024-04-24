# Knights and Knaves puzzle

## Premise

In a Knights and Knaves puzzle, the following information is given: Each character is either a knight or a knave. A knight will always tell the truth: if knight states a sentence, then that sentence is true. Conversely, a knave will always lie: if a knave states a sentence, then that sentence is false.

## Objective

Given a set of sentences spoken by each of the characters, determine, for each character, whether the character is a knight or a knave.

For example, given a simple puzzle with just a single character, A. A says "I am both a knight and a knave".

We note that A cannot be both a knight and a knave, it can be either but not both. So, we can conclude that A is a knave.

## Task

Determine how to represent these puzzles using propositional logic such that an AI running a model-checking algorithm could solve these puzzles for us.

## Model-checking algorithm

To determine wither KB $\models a$ (answering the question, can we conclude that $a$ is true based on our KB):
1. Enumerate all possible models
2. If, in every model where KB is true, $a$ is true as well, then KB entails $a$ (KB $\models a$)

> Example
> P: It is a Tuesday. Q: it is raining. R: Harry will go for a run.
> KB: (P $\land \neg Q) \to R$ (P and not Q imply R)
> KB: P $neg Q$ (P is true, Q is false)

Enumerate all possible models:

|P|Q|R|KB|
|-----|-----|-----|-----|
|false|false|false||
|false|false|true||
|false|true|false||
|false|true|true||
|true|false|false||
|true|false|true||
|true|true|false||
|true|true|true||

Then go through every model and check whether it is true given our KB.

As we know P is true, we can say that the KB is false in all mdoels where P is not true. We also know that Q is false, so KB is false in all models where Q is true.

|P|Q|R|KB|
|-----|-----|-----|-----|
|false|false|false|false|
|false|false|true|false|
|false|true|false|false|
|false|true|true|false|
|true|false|false||
|true|false|true||
|true|true|false|false|
|true|true|true|false|

We are left with two models. In both, P is True and Q is false. In one model, R is true; and, in the other, R is false. Due to (P $\land \neg Q) \to R$ being in our KB, we note that in the case where P is true and Q is false, R must be true.

|P|Q|R|KB|
|-----|-----|-----|-----|
|false|false|false|false|
|false|false|true|false|
|false|true|false|false|
|false|true|true|false|
|true|false|false|false|
|true|false|true|true|
|true|true|false|false|
|true|true|true|false|

There is only one model where our KB is true and, we see that R is also true in this model. If R is true in all models where the KB is true, then KB $\models$ R.

## How to proceed
Need to complete knowledge0..knowledge 3, which need to contain the knowledge needed to deduce the solutions to puzzles 0...3 respectively.

Add knowledge to the knowledge bases 0....3 to solve:

**Puzzle 1**
Contains a single character, A. A says "I am both a knight and a knave"

**Puzzle 2**
Two characters, A and B.
A says "We are both knaves"
B says nothing

**Puzzle 3**
Has two characters, A and B
A says "We are the same kind"
B says "We are of different kinds"

**Puzzle 4**
Has three characters, A, B and C
A says either "I am a knight" or "I am a knave", but you don't know which
B says "A said 'I am a knave'"
B then says "C is a knave"
C says "A is a knight"

In each puzzle:
- each character is either a knight or a knave. 
- Every sentence spoken by a knight is true;
- Every sentence spoken by a knave is false


