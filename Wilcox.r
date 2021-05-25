library("readxl")
library("ggpubr")
my_data <- read_excel("/Users/mit/Desktop/tesla.xlsx", sheet = "Sheet1",na = "---")
auto<-my_data$`With Auto pilot`
man<-my_data$`Without Auto pilot`
my_data <- data.frame(type = rep(c("With Auto pilot", "Without Auto pilot"), each = 10),miles = c(auto, man))
ggboxplot(my_data, x = "type", y = "miles", color = "type", palette = c("#00AFBB", "#E7B800"),ylab = "miles", xlab = "type")
res <- wilcox.test(miles ~ type, data = my_data,exact = FALSE)
