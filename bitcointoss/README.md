# bitcointoss

Solution for the bitcoin toss problem:

https://open.kattis.com/problems/bitcointoss

The solution relies on searching from top to bottom for a value of n, and from bottom up for a value of p. There are additional optimizations to ensure that the program does not run over the 2s limit.

To test run:

```
cat bitcoin-01.in | python3 bitcoin_toss.py
```