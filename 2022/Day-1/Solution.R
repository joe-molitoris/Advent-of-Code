# Advent of Code
# Day 1
data <- readLines("./Day-1/input.txt")

# Solution 1
# Elf with most calories
data <- sapply(data, FUN=function(x){as.numeric(x)})
naPositions <- which(is.na(data))

result <- c()
x <- 1
for (y in naPositions){
  result <- c(result,
              sum(data[x:(y-1)]))
  x <- y+1
}

result1 <- max(result)


# Solution 2
# Top three elves
result2 <- sum(sort(result, decreasing = T)[1:3])

