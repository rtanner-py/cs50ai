# Quiz 1

## Question 1

1. If Hermione is in the library, then Harry is in the library.
2. Hermione is in the library.
3. Ron is in the library and Ron is not in the library.
4. Harry is in the library.
5. Harry is not in the library or Hermione is in the library.
6. Ron is in the library or Hermione is in the library.

Which sentence entails which sentance?

*Answer: Sentence 2 entails sentence 5*

> **Entailment**
> if $a ⊨ b$ then in any world where $a$ is true, $b$ is also true.

We have propositions
- $a$: "Hermione is in the library"
- $b$: "Harry is not in the library" v "Hermione is in the library"

Truth tables:
|P|Q|P v Q|
|false|false|false|
|false|true|true|
|true|false|true|
|true|true|true|

## Question 2

There are other logical connectives that exist, other than the ones discussed in lecture. One of the most common is “Exclusive Or” (represented using the symbol ⊕). The expression A ⊕ B represents the sentence “A or B, but not both.” Which of the following is logically equivalent to A ⊕ B?

(A ∨ B) ∧ ¬ (A ∧ B)
(A ∧ B) ∨ ¬ (A ∨ B)
(A ∨ B) ∧ (A ∧ B)
(A ∨ B) ∧ ¬ (A ∨ B)

*Answer: (A ∨ B) ∧ ¬ (A ∧ B)*

## Question 3

Let propositional variable R be that “It is raining,” the variable C be that “It is cloudy,” and the variable S be that “It is sunny.” Which of the following a propositional logic representation of the sentence “If it is raining, then it is cloudy and not sunny.”?

*Answer: R -> (C ^ ¬S)*

## Question 4

Consider, in first-order logic, the following predicate symbols. Student(x) represents the predicate that “x is a student.” Course(x) represents the predicate that “x is a course.” Enrolled(x, y) represents the predicate that “x is enrolled in y.” Which of the following is a first-order logic translation of the sentence “There is a course that Harry and Hermione are both enrolled in.”?

∃x. Course(x) ∧ Enrolled(Harry, x) ∧ Enrolled(Hermione, x)
∀x. Course(x) ∧ Enrolled(Harry, x) ∧ Enrolled(Hermione, x)
∃x. Enrolled(Harry, x) ∧ ∃y. Enrolled(Hermione, y)
∀x. Enrolled(Harry, x) ∧ ∀y. Enrolled(Hermione, y)
∃x. Enrolled(Harry, x) ∨ Enrolled(Hermione, x)
∀x. Enrolled(Harry, x) ∨ Enrolled(Hermione, x)

*Answer: ∃x. Course(x) ∧ Enrolled(Harry, x) ∧ Enrolled(Hermione, x)*