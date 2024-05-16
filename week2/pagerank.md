# PageRank

Task: Write an AI to rank web pages by importance

The PageRank Algorithm measures a site as important if:
- If it is linked to by other important websites;
- Links from less important websites have their links weighted less

## Random Surfer Model 
- Starts with a random webpage and randomly chooses links to follow. 
- Multiple links on the same page are treated as a single link
- Links from a page to itself are ignored
- The PageRank can be described as the probability that a random surger is on that page at any given time.
- This can be interpretted as a markov chain, where each page represents a stage and each page has a transition model that chooses among its links at random. Each time step represents visiting the next page.
- However, if a page only has one link, and the destination only links back to the source (a two page island), then the other pages will have a probability on 0 (they are never visited).
- To account for this, can introduce a damping factor (d, usualy 0.85). With probability d, the random surver will chose from one of the links on the page; however, with probability 1-d, a surfer will choose any page in the corpuse at random (including the current page)

## Iterative algorithm

$PR(p)$ is the page rank of $p$

There are 2 ways that a random surfer could end up on $p$:
1. With probability (1-d) the surfer chose the page at random
2. With probability (d), the surfer followed a link on page $i$ to $p$

To express 1 mathematically, there is a uniform probability distribution across all the pages that they will be randomly chosen, and so it is $\frac{1-d}{N}$ where $N$ is the total number of pages in the corpus.

For the second condition:
- Need to consider each page $i$ thank links to $p$
- For each $i$, NumLinks(i) is the number of links to that page;
- Each $i$ that links to $p$ has its own Pr(i), representing the probability that we are on page $i$ at any time
- We travel to any of i's links with equal probability, we divide Pr(i) by NumLinks(i) to get the probability that (i) we were on page $i$ and chose link $p$:

$PR(p) = \frac{1-d}{N} + d \sum_i \frac{PR(i)}{NumLinks(i)}$

Note:
D is the damping factor
N is the number of pages in the corpus
i is the collection of all pages that link to p
numlinks(i) is the number of links on page i

## Starting values

We assume that the PageRank of every page is 1/N (equally likely to be on any page). We then use the above forumlua to calculate a new PageRank value for each page, based on the previous values. We then keep repeating until the PageRank values converge.

## Task

1. Implement an algorithm to calculate the PageRank by sampling pages from a Markov Chain random surfer;
2. Implement an algorithm to iteratively apply the PageRank formula
