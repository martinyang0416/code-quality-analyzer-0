<think>
Okay, let's see. The problem is to compute the last two digits of 5 raised to the power of n, where n can be really big, like up to 2e18. Hmm. Oh right, calculating 5^n directly isn't feasible because the number would be way too large. So I need a smart way to find the last two digits without computing the entire number.

Wait, but wait. Let's think about powers of 5. Let's compute some small examples.

5^1 is 5, last two digits 05. But the example for n=2 is 25. 5^2 is 25, so last two d