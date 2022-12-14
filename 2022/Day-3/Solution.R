# Advent of Code
# Day 3


rm(list=ls())
data <- readLines("./Day-3/Input.txt")

# Solution 1
# Find sum of priorities for shared item types in two rucksack compartments
priorities <- seq(1,52)
names(priorities) <- c(letters, LETTERS)


findShared <- function(x){
  nChars <- nchar(x)/2
  compart1 <- unlist(strsplit(x, ""))[1:nChars]
  compart2 <- unlist(strsplit(x, ""))[(nChars+1):nchar(x)]
  
  sharedChar <- c()
  for (i in compart1){
    if (i %in% compart2){
      sharedChar <- c(sharedChar, i)
    }
  }
  
  result <- unique(sharedChar)
  return(result)
}

results <- sapply(data, FUN=findShared)
results <- sapply(results, FUN=function(x){priorities[x]})
sum(results)

# Solution 2

result <- c()
for (i in seq(1,298, 3)){
  compart1 <- unlist(strsplit(data[i], ""))
  compart2 <- unlist(strsplit(data[i+1], ""))
  compart3 <- unlist(strsplit(data[i+2], ""))
  
  sharedChar <- c()
  for (i in compart1){
    if (i %in% compart2 & i %in% compart3){
      sharedChar <- c(sharedChar, i)
    }
  }
  
  sharedChar <- unique(sharedChar)  
  result <- c(result, sharedChar)
}

result <- sapply(result, FUN=function(x){priorities[x]})
sum(result)
