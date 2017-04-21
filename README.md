# BlackJack-RoyalMatch-Simulator
Simulates odds and return on investment for the Royal Match bonus bet in BlackJack

## Introduction

I was at a casino playing BlackJack and noticed they had a bonus side bet you could make.

Royal Match betting 1 unit.

Hand is: | Payout |
--- | ---
 Suited | Pay 3:1
 Suited K & Q | Pay 10:1
 Unsuited: | Lose bet

I wanted to know the odds and return on investment for this bonus game so I wrote this to simulate hands.

## Outcome

After simulating 10MM hands:

Result | % occurance
-- | --
Match | 23.2%
Royal Match | 0.3%
Unmatched | 76.5%

Your return comes out to -3.78% giving the house the advantage.

I've since found that [WizardOfOdds.com](https://wizardofodds.com/games/blackjack/appendix/8/) solved this mathematically showing the odds as being within one thousandth of a pecent.

![Results](https://github.com/CampHof/BlackJack-RoyalMatch-Simulator/blob/master/Results.jpg "Results")

## Other Stuff

Uses [pyDealer](https://github.com/Trebek/pydealer) to do the heavy lifting regarding the deck of cards.

I was surprised at how many trials it took for the odds and ROI to stablize.  I thought I was going to be able to get away with running only 10k trials but even at 1MM hands played, there was still a small amount of movement.  At 10MM trials the numbers stablized and were then validated against WizardOfOdds.com's math.

The code is set to print to a text file since printing to the console would crash at 10MM trials.
