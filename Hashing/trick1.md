# 🧠 Observations

## Observation 1

Operations can only remove:

- Exactly **2** equal elements
- Exactly **3** equal elements

Different numbers can **never** be removed together.

Therefore,

> Every distinct number can be solved **independently**.

---

## Observation 2

First compute the frequency of every number.

Example

```text
1 5 5 1 1 8 8 10 10
```

Frequency map

```text
1  -> 3
5  -> 2
8  -> 2
10 -> 2
```

Now solve each frequency separately.

---

## Observation 3 (Impossible Case)

If any number appears only once,

```text
frequency == 1
```

it can never be removed because the allowed operations are only:

- Remove 2 equal numbers
- Remove 3 equal numbers

Hence

```text
Answer = -1
```

---

## Observation 4

For every frequency **f ≥ 2**, a valid solution always exists.

Reason:

Every integer greater than or equal to 2 can be represented using only

```text
2's and 3's
```

Examples

```text
2 = 2

3 = 3

4 = 2+2

5 = 3+2

6 = 3+3

7 = 3+2+2

8 = 3+3+2

9 = 3+3+3
```

---

## Observation 5

To minimize operations,

we should remove **3 elements whenever possible** because

```text
1 operation removes more elements.
```

Therefore,

maximize the number of groups of size 3.

---

## Observation 6

For a frequency **f**

### If

```text
f % 3 == 0
```

Use only groups of 3.

Operations

```text
f / 3
```

Example

```text
6 -> 3+3

9 -> 3+3+3
```

---

### If

```text
f % 3 == 2
```

Use one group of 2.

Operations

```text
f//3 + 1
```

Example

```text
5 -> 3+2

8 -> 3+3+2

11 -> 3+3+3+2
```

---

### If

```text
f % 3 == 1
```

One group of 3 leaves one element,

which is invalid.

So,

convert one previous group of 3 into two groups of 2.

Example

```text
7

3+3+1 ❌

↓

3+2+2 ✅
```

Example

```text
10

3+3+3+1 ❌

↓

3+3+2+2 ✅
```

Operations are still

```text
f//3 + 1
```

---

## Final Formula

If

```text
frequency == 1
```

return

```text
-1
```

Else

```text
operations = ceil(frequency / 3)
```

which can be written as

```python
operations = frequency // 3

if frequency % 3 != 0:
    operations += 1
```

---

# Pattern

```text
Frequency

↓

Solve each frequency independently

↓

If frequency == 1

    Impossible

Else

    Answer += ceil(frequency / 3)
```

---

# Time Complexity

- Frequency Map → **O(N)**
- Traverse Frequencies → **O(U)** (`U` = unique elements)

Overall

```text
O(N)
```

Space

```text
O(U)
```

---

# Interview Insight ⭐

The biggest observation is:

> The answer depends **only on the frequency** of each distinct number, **not on their positions**.



## different question 
# 🧠 Pattern: Maximum Number of Times String `t` Can Be Formed From String `s`

## Problem

Given two strings

```text
s
t
```

Find the **maximum number of times** we can construct `t` using characters from `s`.

Each character can be used only once.

---

## Example 1

```text
s = "abcbacbbac"

t = "abc"
```

Frequency

```text
s

a -> 3
b -> 4
c -> 3
```

Need

```text
a -> 1
b -> 1
c -> 1
```

Answer

```text
min(3/1,4/1,3/1)

=

3
```

---

## Example 2

```text
s = "abcbacbbac"

t = "abbc"
```

Need

```text
a ->1

b ->2

c ->1
```

Answer

```text
a

3/1 = 3

b

4/2 = 2

c

3/1 = 3

Answer = 2
```

---

## Example 3

```text
s = "abcbacbbac"

t = "abcp"
```

Need

```text
p ->1
```

But

```text
p

0
```

Therefore

```text
Answer = 0
```

---

# 🧠 Observation 1

Order of characters **does not matter.**

Only the **frequency** of each character matters.

---

# 🧠 Observation 2

Store frequencies.

```text
Frequency(s)

Frequency(t)
```

---

# 🧠 Observation 3

Every character of **t** acts like a constraint.

Example

```text
Need

b ->2
```

If

```text
s

b ->5
```

Then

```text
Maximum possible copies

=

5//2

=

2
```

---

# 🧠 Observation 4

Every character gives its own limit.

Example

```text
a

3 copies

b

2 copies

c

5 copies
```

Overall answer

```text
min(3,2,5)

=

2
```

The **minimum** decides the answer because that character finishes first.

It is called the **Limiting Resource Principle**.

---

# 🧠 Observation 5

Formula

For every character present in **t**

```text
possibleCopies

=

frequencyS[ch]

//

frequencyT[ch]
```

Final Answer

```text
minimum of all possibleCopies
```

---

# Pattern

```text
Count Frequency of s

↓

Count Frequency of t

↓

For every character in t

answer

=

min(

frequencyS[ch] // frequencyT[ch]

)

↓

Return answer
```

---

# Why Floor Division?

Suppose

```text
Need

b ->2

Have

b ->5
```

We can make

```text
5//2

=

2
```

copies.

Not

```text
2.5
```

because half a string cannot be formed.

---

# Interview Recognition

Whenever you hear

> Maximum number of times

or

> Construct string

or

> Build word

or

> Form target from source

Immediately think

```text
Frequency Counting

+

Minimum Ratio
```

---

# Similar Problems

- Ransom Note
- Valid Anagram
- Maximum Number of Balloons
- Word Formation
- Magazine Problems
- Character Rearrangement
- Construct String Problems

---

# Complexity

Building frequencies

```text
O(|S|+|T|)
```

Traversing target map

```text
O(Unique Characters)
```

Overall

```text
O(|S|+|T|)
```

Space

```text
O(Alphabet Size)
```

---

# ⭐ Golden Observation

The answer is **never decided by the character with the highest frequency.**

It is always decided by the character that **runs out first**.

Mathematically,

```text
Answer

=

min(

frequencyS[ch]

//

frequencyT[ch]

)
```

This "minimum ratio" pattern appears in many interview questions.