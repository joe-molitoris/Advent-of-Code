# Advent of Code
# Day 5

rm(list=ls())
data <- readLines("./Day-5/Input1.txt")
data <- 
  sapply(
    data,
    FUN= function(x){strsplit(x, ",")}
  )

names(data) <- seq(1,9)

directions <- readLines("./Day-5/Input2.txt")
directions <- gsub("move ", "", directions)
directions <- gsub(" from ", ",", directions)
directions <- gsub(" to ", ",", directions)

# Solution 1
for (d in directions){
  directionStep <- unlist(strsplit(d, ","))
  quantity <- as.numeric(directionStep[1])
  from <- directionStep[2]
  to <- directionStep[3]
  
  fromData <- data[from][[1]][
    length(data[from][[1]]) : (length(data[from][[1]]) - (quantity-1))
  ]
  
  data[to][[1]] <- c(
    data[to][[1]],
    fromData
  )
  data[from][[1]] <-
    data[from][[1]][1:(length(data[from][[1]])-quantity)]
  }

finalMessage <- paste0(
  sapply(data, FUN= function(x){x[length(x)]}),
  collapse = ""
)

# Solution 2
data <- readLines("./Day-5/Input1.txt")
data <- 
  sapply(
    data,
    FUN= function(x){strsplit(x, ",")}
  )

names(data) <- seq(1,9)

for (d in directions){
  directionStep <- unlist(strsplit(d, ","))
  quantity <- as.numeric(directionStep[1])
  from <- directionStep[2]
  to <- directionStep[3]
  
  fromData <- data[from][[1]][
    (length(data[from][[1]]) - (quantity-1)) : length(data[from][[1]])
  ]
  
  data[to][[1]] <- c(
    data[to][[1]],
    fromData
  )
  data[from][[1]] <-
    data[from][[1]][1:(length(data[from][[1]])-quantity)]
}

finalMessage <- paste0(
  sapply(data, FUN= function(x){x[length(x)]}),
  collapse = ""
)

finalMessage

