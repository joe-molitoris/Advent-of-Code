# Advent of Code
# Day 2

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome 
# of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

rm(list=ls())
data <- readLines("./Day-2/input.txt")

# Solution 1
# Follow stategy guide
resultDict <- c("A X" = 1+3,
                "A Y" = 2+6,
                "A Z" = 3+0,
                "B X" = 1+0,
                "B Y" = 2+3,
                "B Z" = 3+6,
                "C X" = 1+6,
                "C Y" = 2+0,
                "C Z" = 3+3
)

results <- sapply(data, FUN=function(x){resultDict[x]})
sum(results)

# Solution 2
# "Anyway, the second column says how the round needs to end: 
# X means you need to lose, Y means you need to end the round in a draw, 
# and Z means you need to win. Good luck!"

resultDict2 <- c("A X" = 3+0,
                "A Y" = 1+3,
                "A Z" = 2+6,
                "B X" = 1+0,
                "B Y" = 2+3,
                "B Z" = 3+6,
                "C X" = 2+0,
                "C Y" = 3+3,
                "C Z" = 1+6
)

results2 <- sapply(data, FUN=function(x){resultDict2[x]})
sum(results2)

