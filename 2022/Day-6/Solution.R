# Advent of Code
# Day 6

rm(list=ls())
data <- readLines("./Day-6/input.txt")

dataList <-unlist(strsplit(data, ""))

# Solution 1
for (i in seq(4,nchar(data))){
  if (length(unique(dataList[i:(i-3)]))==4){
    print(i)
    break()
  }
}



# Solution 2
for (i in seq(14,nchar(data))){
  if (length(unique(dataList[i:(i-13)]))==14){
    print(i)
    break()
  }
}






