# Idea 3 - K-means Clustering of Image Feature Vectors

## Motivation

_Turi Create_ was a bust, but they mention something at the end of their [guide](https://apple.github.io/turicreate/docs/userguide/image_similarity/) that motivates the following idea.
They list the 3 steps that explain how their image similarity model works:

1. Obtain a pre-trained CNN classifier and rip out the last layer

2. Run our images through this modified CNN classifier, this gives us our feature vectors!

3. Now, we can create (in their case) a nearest neighbors model using the output of step 2.

i.e. Let's do transfer learning and just tweak step 3 so that we solve the problem we set out to solve.

## The Work

