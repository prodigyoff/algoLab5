**Algorithm description:**  
1. Looking for prefixes that are suffixes at the same time and writing them into ```prefix_list```  
2. Iterating through our text, comparing it to pattern using individual index for both of them and using ```prefix_list``` to skip useless comparisons.
3. Whenever ```pattern_counter``` reaches length of our pattern, we write the result into ```result``` list.  
4. Repeating steps 2 and 3 untill we reach the end of the text and returning ```result``` as an answer.  
**Overall time complexity:  O(n + m)**, where **n** stands for complexity of algorithm and **m** for complexity of searching proper prefixes, **n** - length of text, **m** - length of pattern.  
**Space complexity: O(m)** because we are using additional list to store information about proper prefixes, **m** - length of pattern.  
# KMP algorithm  
**To run my code:**  
• Download/clone this repository  
• Write your data into ```kmp.in```  
• Use command in folder which contains main.py: ```python3 main.py``` (could be "py" or "python" depending on your python version, also you can change inputs in kmp.in) and check results in command line or in kmp.out  
• To launch unittests using console type: ```python3 -m unittest test_kmp.py``` (in the same folder as step before)  
