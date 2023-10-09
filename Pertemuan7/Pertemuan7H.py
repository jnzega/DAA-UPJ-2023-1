# Matching substring in String

test_str = "Gfg is good website"
test_list = ["Gfg", "site", "CS", "Geeks", "Tutorial"]
print("The original string is: " + test_list)
print("The original list is: " + str(test_list))
res = [sub for sub in test_list if sub in test_str]
print("The list of found substrings: " + str(res))