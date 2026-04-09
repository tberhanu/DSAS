"""Regex
• Matches anything except newline
a|b → one character: a OR b

Identifiers:
\d → digit
\D → not digit
\w → alphanumeric + underscore
\W → non‑alphanumeric
\s → whitespace (space, tab, newline)
\S → non‑whitespace
\n → newline
\t → tab
\b → word boundary
\B → not word boundary

Examples:
\bcat\b → matches "cat"
cat\b → matches "cat" at end of word
1\d+\b → matches "123"

Quantifiers:
{3}     → exactly 3 times
{3,4}   → 3 to 4 times
{3,}    → 3 or more times
{,3}    → up to 3 times
(*, +, ? are exceptions)

Sets:
[a,b,c] → a OR b OR c
[a-z]   → any lowercase letter
[A-Z]   → any uppercase letter
[^a-z]  → NOT a lowercase letter
^ inside set → negation

Escaped examples:
[a\-z]     → literal '-' inside set
[(+*?)]    → literal (, +, *, ?
"""
import re

pattern = "phone"
pattern2 = r"\d+"
pattern3 = r"^k$"     # start at ^, end at $
####################### re.search #######################################

# Search → returns the first match
match = re.search(pattern, "text")
match.span()      # (start_index, end_index) — zero‑indexed, end not inclusive
match.start()
match.group()     # actual matched string
########################## re.findall ####################################

# Find all → returns list of all matches
matches = re.findall(pattern, "text")

######################### re.finditer #####################################

# Finditer → returns iterator of match objects
for match in re.finditer(pattern, "text"):
    print(match.span(), match.group())

######################### re.compile #####################################
# Compiled regex object (efficient for repeated use)
compiled_pattern = re.compile(r"\bcat\b")

matches = compiled_pattern.findall("text")
match_iterator = compiled_pattern.finditer("text")

for match in match_iterator:
    print(match.group(), match.start(), match.end())
