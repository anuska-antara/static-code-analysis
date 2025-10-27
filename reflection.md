1.	Which issues were the easiest to fix, and which were the hardest? Why?
The easiest issues to fix were the missing encoding and mutable default argument problems because they required only minor code changes (with open(..., encoding="utf-8") and replacing logs=[] with None).
The hardest issue was adding input validation because it required thinking about possible invalid cases, deciding how to handle them, and ensuring it didn’t affect normal program flow.

2.	Did the static analysis tools report any false positives? If so, describe one example. 
No major false positives were observed. Most warnings were valid and useful. However, tools like Pylint and Flake8 flagged missing docstrings and function naming style issues that didn’t break the code — these were stylistic suggestions rather than actual problems.

3.	How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices. 
I would integrate Pylint, Flake8, and Bandit into a Continuous Integration (CI) pipeline so that code quality and security checks run automatically whenever changes are pushed.
During development, I’d also run these tools locally to catch issues early before committing the code.

4.	What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
After applying the fixes, the code became:
•	More secure (removed eval() and added safe file handling).
•	More reliable (handled missing files and invalid inputs).
•	More readable (consistent naming and proper docstrings).
•	Easier to maintain due to reduced hidden bugs and clear structure.
Overall, the program now behaves predictably even with incorrect inputs.