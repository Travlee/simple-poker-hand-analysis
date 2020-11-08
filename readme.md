# Simple Poker Hand Analysis
Write a simple app that can take two 5-card poker hands, classify each hand, and determine which hand would win. For this problem suits are ignored, so a flush will not be possible.

### Each card can be represented by a single character:
- A for ace
- K for king
- Q for queen
- J for jack
- T for ten
- 2-9 for the remaining
- * for a wild card (max of 1 per hand)

### Hand classifications are as follows (highest to lowest):
- four-of-a-kind (4 cards of the same value: AAAA5)
- full house (3 of one, and 2 of another: KKKQQ)
- straight (all 5 in sequential order: 6789T)
- three-of-a-kind (3 cards of the same value: KKK23)
- two pair (AA33J)
- pair (44KQA)
- high card (nothing else: A267J)

### Comparison rules:
- When comparing two pair hands, compare the highest pair first, then the next pair. i.e. AA223 > KKQQT, since AA > KK. When the highest pair is a tie, move on to the next pair. i.e. AA993 > AA88K.
- Similarly, when comparing full house hands, the three-card group is compared first. AAA22 > KKKQQ.
- In the case of ties, determine a winner by comparing the next highest card in the hand. i.e. AA234 < AA235 because AAs tie, 2s tie, 3s tie, but 4 < 5.
- Straights are compared by the highest card in the hand, except for A2345, in which case the 5 is considered the highest card in the straight.

### Wild cards:
- When there is a wild card, the final hand has to be a valid 5-card poker hand (no five-of-a-kind!)

### For each comparison, display the classification, as well as indicate which hand would win (or that it's a tie). For example:
- AAAKT vs 22233: AAAKT three-of-a-kind < 22233 full house
- 2345* vs KKJJ2: 2345* straight > KKJJ2 two pair
- AAKKT vs AAKKT: AAKKT two pair == AAKKT two pair
- KKKKA vs KKKK*: KKKKA four-of-a-kind == KKKK* four-of-a-kind
