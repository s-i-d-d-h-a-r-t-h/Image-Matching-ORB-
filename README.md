# Image-Matching-ORB-

## ORB
ORB detector stands for Oriented Fast and Rotated Brief, this is free of cost algorithm, the benefit of this algorithm is that it does not require GPU it can compute on normal CPU.
ORB is basically the combination of two algorithms involved FAST and BRIEF where FAST stands for Features from Accelerated Segments Test whereas BRIEF stands for Binary Robust Independent Elementary Features.

This algorithm works on Key point matching, Key point is distinctive regions in an image like the intensity variations.

## Brute Force Matcher
Brute Force Matcher is used for matching the features of the first image with another image.
It takes one descriptor of first image and matches to all the descriptors of the second image and then it goes to the second descriptor of first image and matches to all the descriptor of the second image and so on.
