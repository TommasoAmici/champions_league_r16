#[OC] Probabilities for Each Round of 16 match-up in the Champions League
Hi /r/soccer,

To calculate the probabilities I wrote a little program in Python that simulates a draw. The results are based on around 670,000 simulations.

I was inspired by [this post](https://www.reddit.com/r/soccer/comments/7hw8ir/occurrent_probabilities_for_each_r16_matchup/) by /u/Semperty, where he calculated the actual permutations of each possible match up.

I think this can be easily adapted to the Europa League round of 32, but I'll have to check whether the rules are the same. In that case, I will make a post for that too.

**Table**

Teams | Man United | PSG | Roma | Barcelona | Liverpool | Man City | Besiktas | Tottenham
---|---|---|----|----|----|----|----|----
**Basel** | - | 11.2% | 15.8% | 14.7% | 15.8% | 15.4% | 11.2% | 15.8%
**Bayern** | 14.8% | - | 15.3% | 13.8% | 15.3% | 14.8% | 10.7% | 15.2%
**Chelsea** | - | 28.5% | - | 43.0% | - | - | 28.5% | -
**Juventus** | 18.4% | 12.8% | - | - | 18.9% | 18.3% | 12.7% | 18.9%
**Sevilla** | 18.4% | 12.7% | 18.9% | - | - | 18.3% | 12.8% | 18.9%
**Shaktar** | 15.4% | 11.2% | 15.9% | 14.7% | 15.9% | - | 11.2% | 15.9%
**Porto** | 14.8% | 10.8% | 15.2% | 13.8% | 15.3% | 14.9% | - | 15.2%
**Real Madrid** | 18.3% | 12.8% | 18.9% | - | 18.9% | 18.3% | 12.8% | -

If you're interested in looking at the source code, it's on my [Github.](https://github.com/TommasoAmici/champions_league_r16)