# Problem Statement
We create an array of points  P[n] in a two dimensional plane using the following random number generator:
s[0]=290797


s[n+1]=(s[n] * s[n]) mod 50515093


P[n]=(s[2n],s[2n+1])

Let d(k)  be the shortest distance of any two (distinct) points among P[0],...,P[k - 1].
E.g. d(14) = 546446.466846479

Find d(2000000). Give your answer rounded to 9 places after the decimal point.

#Answer
1336.449400464
