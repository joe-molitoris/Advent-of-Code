# Advent of Code
# Day 4

rm(list=ls())

data <- readLines("./Day-4/Input.txt")

# Solution 1
findOverlap <- function(x){
  assignments <- unlist(strsplit(x, ","))
  track1 <- as.numeric(unlist(strsplit(assignments[1], "-")))
  track2 <- as.numeric(unlist(strsplit(assignments[2], "-")))  
  
  if (min(track1)<=min(track2) & max(track1)>=max(track2)){
    return(T)
  }
  else if (min(track2)<=min(track1) & max(track2)>=max(track1)){
    return(T)
  } 
  return(F)
}

sum(sapply(data, FUN=findOverlap))

# Solution 2

findAnyOverlap <- function(x){
  assignments <- unlist(strsplit(x, ","))
  track1 <- as.numeric(unlist(strsplit(assignments[1], "-")))
  track2 <- as.numeric(unlist(strsplit(assignments[2], "-")))  

  return(length(intersect(seq(min(track1), max(track1)),
                      seq(min(track2), max(track2))))>0)
}

sum(sapply(data, FUN=findAnyOverlap))

       