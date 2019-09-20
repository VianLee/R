# Getting Help
## Accessing the Help Files
Get help of a particular function,
```R
?mean
```

Search the help files for a word or phrase,
```R
help.Search('weighted mean')
```

Find help for a package,
```R
help(package='dplyr')
```


## More About An Object
Get a summary of an object's structure,
```R
str(iris)
```

Find the class an object belongs to,
```R
class(iris)
```



# Using Packages
Download and install a package from [CRAN](https://cran.r-project.org/),
```R
install.packages('dplyr')
```

Load the package into the session, making all its functions available to use,
```R
library(dplyr)
```

Use a particular function from a package,
```R
dplyr::select
```

Load a built-in dataset into the environment,
```R
data(iris)
```



# Working Directory
Find the current working directory (where inputs are found and outputs are sent),
```R
getwd()
```

Change the current working directory,
```R
# for windows
setwd('C://Users/...')
# for macosx
setwd('/Users/...')
# for linux
setwd('/home/...')
```



# Vectors
## Creating Vectors
Join elements into a vector,
```R
v <- c(2, 4, 6)
```

An integer sequence,
```R
v <- 2:6
```

An complex sequence,
```R
v <- seq(2, 3, by=0.5)
```

Repeat a vector,
```R
v <- rep(1:2, times=3)
```

Repeat elements of a vector,
```R
v <- rep(1:2, each=3)
```


## Vector Functions
Return x sorted,
```R
sort(x)
```

Return x reversed,
```R
rev(x)
```

See counts of values,
```R
table(x)
```

See unique values,
```R
unique(x)
```


## Selecting Vector Elements
### By Position
the fourth element,
```R
x[4]
```

All but the forth,
```R
x[-4]
```

Elements two to four,
```R
x[2:4]
```

All elements except two to four,
```R
x[-(2:4)]
```

Elements one and five,
```R
x[c(1, 5)]
```

### By Value
Elements which are equal to 10,
```R
x[x == 10]
```

All elements less than zero,
```R
x[x < 0]
```

Elements in the set 1, 2, 5,
```R
x[x %in% c(1, 2, 5)]
```

### Named Vectors
Elements with name 'apple',
```R
x['apple']
```



# Programming
## For Loop
```R
# for (variable in sequence) {
# 	Do something
# }
for (j in 1:4) {
	j <- i + 10
	print(j)
}
```


## While Loop
```R
# while (condition) {
# 	Do something
# }
i <- 0
while (i < 5) {
	print(i)
	i <- i + 1
}
```


## If Statements
```R
# if (condition) {
# 	Do something
# } else {
# 	Do something different
# }
i <- 3
if (i > 3) {
	print('Yes')
} else {
	print('No')
}
```


## Functions
```R
# function_name <- function(var) {
# 	Do something
# 	return(new_variable)
# }
square <- function(x) {
	squared <- x*x
	return(squared)
}
```


## Reading and Writing Data
Read and write a delimited text file,
- `df <- read.table('file.txt')`
- `write.table(df, 'file.txt')`

Read and write a comma separated value file,
- `df <- read.csv('file.csv')`
- `write.csv(df, 'file.csv')`

Read and write an `R` data file, a file type special for `R`,
- `load('file.RData')`
- `save(df, file='file.RData')`



# Matrices
```R
m <- matrix(x, nrow=3, ncol=3)
```

Select a row,
```R
m[2, ]
```

Select a column,
```R
m[ , 1]
```

Select an element,
```R
m[2, 3]
```

Transpose,
```R
t(m)
```

Matrix multiplication,
```R
m %*% n
```

Find *x* in: *m\*x=n*,
```R
solve(m, n)
```
