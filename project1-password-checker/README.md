# Password Strength Checker

A Python script that evaluates password strength (ranging from weak 
to strong) based on character length and variety, and suggests 
improvements.

## Skills Shown
- String handling and iteration
- Boolean logic
- List building for dynamic feedback

## How It Works
The script checks for:
- Minimum length (8+ characters)
- Uppercase letters
- Digits
- Special symbols

## Example
```
Enter your Password: CONFIDENCEZACHARIAS
Password Strength: Medium
Suggestions:
-Add Digits
-Add Special Character
```

## Design Decisions
I classified a password as "Medium" if it meets the minimum length 
requirement (8+ characters) but is missing one or more character types 
(uppercase, digit, or symbol), rather than using a graduated scoring 
system that weights each missing type differently. This means, for 
example, a 20-character password with only uppercase letters is rated 
the same as an 8-character password missing just one character type — 
a simplification I made deliberately, matching the project's focus on 
core string-handling and conditional logic rather than a weighted 
algorithm. A future iteration could assign partial credit per 
criterion, or flag common/leaked passwords using a wordlist check.

