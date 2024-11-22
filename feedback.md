## remarks
  - add myenv in gitignore to not push it on remote
  - why 2 differents datasets? which one is the final one? I assumed this is Cleaned_Data.csv
  - I don't see any commit from Miro in the main branch? I read in the readme you've done code combination and testing so I guess it's OK.
  - .py file is a not very clean, too many lines in the script you did not use the OOP logic to split it into different files, not very readable but good comments. And I read in usage you tell to use notebook but this is not good practice, please create a .py main file we can execute like this "python main.py". This main script can call different others modules located in different files. Please have this in mind for future projects :smile:
  - no typing or docstrings :cry:
  - you can clean the remaining branches when the project is finished :wink:
- In general the project is good :fire: the dataset as well :fire: but there is room for improvement to build something cleaner



## Evaluation criteria

| Criteria       | Indicator                                  | Yes/No |
| -------------- | ------------------------------------------ | ------ |
| 1. Is complete | Contains a minimum of 10,000 inputs.       | [Yes]    |
|                | Contains data for all of Belgium.          | [Yes]    |
|                | No empty row present in the dataset.       | [Yes]    |
|                | Non-numeric values have been minimized.    | [No]    |
| 2. Is great    | Used threading or multiprocessing to speed up the collection. | [Yes]    |
|| Used git properly as a team | [Yes]    |
