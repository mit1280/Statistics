library("readxl")
library(ggplot2)
my_data <- read_excel("/Users/mit/Desktop/mary.xls", sheet = "Sheet1",na = "---")


s<-factor(my_data$smoke,levels=c("Yes","No"),labels=c(1,0))
p<-factor(my_data$`Prenatal session`,levels=c("Yes","No"),labels=c(1,0))

d = table(s,p)
print(chisq.test(d))
