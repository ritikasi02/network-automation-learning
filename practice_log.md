# Python Practice Log

Daily drill tracker for network-automation interview prep. **Newest entries at the bottom.**
The coach reads this file to pick the next topic and the right difficulty, then appends one
line per session at the end of the Log table.

## Weak spots to re-drill (aim for ~1 in every 3 sessions)
1. **Reference vs value** — list & dict aliasing & mutation (`b = a` shares the object; use `.copy()` to duplicate)
2. **OOP mental model** — `self` is the *instance*, not the data; a class bundles state (`self.data`) + behavior (methods); `a` and `b` are independent instances
3. **Container element model & `len`** — `add(x)` adds `x` as one element; `len` counts the container you hand it (list → items, string → chars)
4. **Precise vocabulary** — "pure vs side-effecting"; "data enters a function via parameters, bound at call time"

## Breadth topics to rotate through
- comprehensions (list / dict / set)
- enumerate / zip / sorted(key=) / lambda
- collections: Counter, defaultdict
- slicing & negative indexing
- `*args` / `**kwargs` & the mutable-default-arg trap
- generators / yield / iterators
- dict iteration (`.items` / `.keys` / `.values` / `.get`)
- raising & custom exceptions, `finally` / `else`
- truthiness / ternary / f-strings
- hashmap-counting pattern
- two-pointer pattern
- set-dedup / set algebra

## Difficulty ladder
`easy` → `easy-medium` → `medium` → `medium-hard` → `hard`. Go one notch up after a clean pass; hold level after a partial; drop a notch after a fail.

## Log
| Date | Topic | Difficulty | Result | Remember this |
|------|-------|-----------|--------|---------------|
