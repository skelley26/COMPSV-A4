# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# 10. Remove by Value
# Remove the first occurrence of a given value from a sequence.
# Input: [10, 20, 30, 20], Remove 20
# Output: [10, 30, 20]



input = [10, 20, 30, 20] #input the values
duplicate_values = set(input) #turn it into a set which removes any duplicates by default
print(duplicate_values) #print what's left
list = list(duplicate_values) #turn it into a list (cleans it up)

