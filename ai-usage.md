I used AI, specifically Google's Gemini LLM chat bot, to help me out with debugging 
and pointing out a problem.

I went looking on the web for the longest palindrome, which I copy and pasted into 
my test case. What I had failed to realize is that the string contained an em dash 
rather than a dash, breaking my utility function that I wrote. A quick paste of the 
traceback presented me with feedback that the string contained an em dash, not a 
dash. I face palmed and then replaced it with a dash.

I was also helped with the correct usage of the `assertRaises` method in my test 
case. Originally I was calling the palindrome method, but what I needed to do is 
pass in the method and arguments separately.