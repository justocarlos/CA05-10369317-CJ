
#CA04 
#student number:10369317
#Carlos Justo

library(stringr)
library(stats)
library(base)


setwd("D:/Python27")
my_commits <- read.csv("changes.csv", header = TRUE, stringsAsFactors = F)

summary(my_commits)
str(my_commits)
names(my_commits)


unique(my_commits$author)
check<-table(my_commits$author)
check
hist(check) #histogram counting the commimentments by author

barplot(counts, main="Author Breakdown",xlab="Commits per author", col=c("Darkblue"))

data_set <- subset(my_commits, author != "/OU=Domain Control Validated/CN=svn.company.net")
new_data<-subset(data_set, author != "ajon0002")
unique(new_data$author)

check<-table(new_data$author)
check
barplot(counts, main="Authors",xlab="Commits per author", col=c("Darkblue"), cex.axis = 1, cex.lab=1)


#splitting the date

split_the_date <- str_split_fixed(new_data$date, " ",2)
split_the_date
str(split_the_date)
unique(split_the_date$V1) #I can check that is an atomic vector
the_date=as.data.frame(split_the_date) #converting to data frame
the_date$V1
the_date$V2

split_year<-str_split_fixed(the_date$V1, "-",2)

the_year=as.data.frame(split_year)
the_year
the_year$V1
the_year$V2

split_month<-str_split_fixed(the_year$V2, "-",2)
the_month<-as.data.frame(split_month)
the_month
the_month$V1
checking <- table(the_month$V1)
barplot(checking, main="Month Breakdown by 2015",xlab="Commits per month", col=12)
unique(checking) 








