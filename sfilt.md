# sfilt.py
_Joshua Chan_

_Pseudo-code for implementing a simple spam filter in Python based on Bayes' Theorem_

## Algorithms

### Bayesian Implementation

The main purpose for this program is to practice implementing Bayes Theorem in a programming language, so as such I'll be using it to filter the messages.

To keep things simple, we'll limit the scope of the project by:
+ looking only at message bodies (not extra meta information like email addresses or hosts)
+ tokenizing by words and not phrases

__Bayes Theorem__


__Conditions__

A word will be considered spam if the words contained in the message are found more often in spam messages than non-spam messages.

__Algorithm__

1. tokenize word
2. initialize tally of total spam and not-spam probs
2. for each word in token  
    a. find probabilities that it's spam/not-spam from trained model
    b. multiply its prob that it is spam by the current total spam
    c. multiply its not-spam prob by current total not-spam prob
3. prob_is_spam = spam/(spam + not-spam)



---

## Class Diagrams

### Message

TODO

### SpamFilter

TODO

---
