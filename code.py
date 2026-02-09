Okay, let's see. The problem is to take an integer a between 0 and 35 and output some number. The examples show that when input is 3, output is 8. And for 10, it's 1024. Hmm. Wait, what's the pattern here?

Let me think... 3 gives 8. Oh, 2^3 is 8. Oh right! And 10 would be 2^10 which is 1024. That's exactly the second example. So maybe the problem is to compute 2 raised to the power of a?

Wait, but why the input range up to 35? Because 2^35 is a pretty big number. But in Python, integers can ha