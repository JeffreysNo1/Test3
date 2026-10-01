# Student Grade Book
# Build a grade book that stores student names and scores in a dictionary. Your program calculates the class average, finds the top and bottom scorer, and lets the user look up any student's grade.

# What you need to use
# ------------------------------------------------------------------------
# 1.  dictionary      →  store at least 5 student name-score pairs
# 2.  for loop        →  to calculate the class average
# 3.  max() min()     →  to find the top and bottom scorer
# 4.  .get()          →  to look up a student by name
# 5.  input()         →  to let the user search for a student
# ------------------------------------------------------------------------

# What you'll be marked on
# ------------------------------------------------------------------------
# 1.  Dictionary created with at least 5 student name-score pairs  →   5 marks
# 2.  A loop correctly calculates and prints the class average      →  10 marks
# 3.  Highest and lowest scores and students identified             →  10 marks
# 4.  .get() used to look up student — friendly message if missing  →  10 marks
# 5.  Program runs without any errors                               →   5 marks
# ========================================================================
# Total  →  40 marks
# ========================================================================

# How to submit 🚀
# Push your completed code to a public GitHub repository and paste the
# repo link in the box below. Make sure your repo is public and your
# code runs correctly before submitting.
dictOG={"Ahmed":65,"Jamal":37,"Aahil":92,"Shourya":98,"Shayaan":51}
total=0
for score in dictOG.values():
    total+=score
avg=total/len(dictOG)
print("The class average is",avg)
highest=max(dictOG.values())
lowest=min(dictOG.values())
TopScorer=max(dictOG,key=dictOG.get)
BottomScorer=min(dictOG,key=dictOG.get)
print("The TopScorer:",TopScorer,"-",highest)
print("The BottomScorer:",BottomScorer,"-",lowest)
name=input("Enter a student name to look up:")
score=dictOG.get(name)
if score==None:
    print(name,"scored",score)
else:
    print("Student not found")