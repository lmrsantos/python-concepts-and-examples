import re

text = "this is my phone: 999-555-7777"

# SEARCH
match = re.search("phone", text)
print (f'===> SEARCH the first occurence: {match}')

print (f'search(phone): {match}')
print (f'span(): {match.span()}')
print (f'start(): {match.start()}')
print (f'end(): {match.end()}')

text1 = "this is the phone 1 and that is the phone 2"

# FINDALL
matches = re.findall("phone", text1)

print (f'\n==> FINDALL bring all occurrencies: {matches}')

print (matches)
print ("\n==> FINDITER to iteration. Printing below the re.match object, match.group(), match.span()")
for match in re.finditer("phone", text1):
    print(f'match: {match}')
    print (f'group: {match.group()}')
    print (f'span: {match.span()}')

## using patterns
text = "this is my phone: 999-555-7777"
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print (f'\n==> using PATTERNS: {phone.group()}')

## COMPILE to create a pattern to be reused
## parentesis means the numbers of groups that the pattern has. In the example below it has 3 groups
print (f'\n==> creating a patter with COMPILE and stores in a variable: {phone.group()}')
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
result = re.search(phone_pattern, text)
print (f'- group(): {result.group()}')
print (f'- group(1): {result.group(1)}')

# WILD CARD . considers any character
print (f'\n===> WILD CARD ".": {re.findall(".at", "The cats is the hat sat went splat")}')

# OR "|"
print (f'\n===> using OR "|": {re.findall(r"cat|dog", "The cat is close to the dog")}')

# STARTS WITH "^" and ENDS WITH "$"
match_start = re.findall(r'^\d', '2 is a number')
match_end = re.findall(r'\d$', 'The number is 2')

print (f"\n===> SEARCH IN THE ENTIRE TEXT - starts with '^': {match_start}")
print (f"\n===> SEARCH IN THE ENTIRE TEXT - ends with '$': {match_end}")

# Search for numbers \d+
match = re.findall(r'\d+', "the numeber 22398562 is gt the number 212846")
print (f"\n===> Using \d+ makes re finds the whole number and bring the correct result: {match}")

# Search for workds
pattern = re.compile(r'\w+')
animals = "dog cat bird dog elefant tiger"
match = re.findall(pattern, animals)
print (f"\n===> Using \w+ to find all words in the string: {match}")

# Remove numbers
text = "the numeber 22398562 is gt the number 212846"
print (f'\n===> The string is: {text}')
pattern = re.compile(r'[^\d]+')
match = re.findall(pattern, text)
print (f"\n===> Using [^\d]+ to remove all numbers in the string: {match}")

# Remove words
pattern = re.compile(r'[\d]+')
print (pattern)
match = re.findall(pattern, text)
print (f"\n===> Using [\d]+ to find all words in the string: {match}")

# Remove ponctuations

text = "This is a text! There are some ponctuations. How can I remove them?"
pattern = re.compile (r'[^!.? ]+')
clean = re.findall(pattern, text)
print (f'\n===> This is the clean text w/t ponctuations. Using ^!.? ]+: {" ".join(clean)}')


