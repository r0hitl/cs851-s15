j4 <- read.csv(file="j7.txt",header=TRUE,sep="\t")

j4$Time <- as.Date(strptime(j4$Time, "%Y-%m-%dT%H:%M:%S"))

ggplot(j4, aes(Time, Distance)) + geom_line(colour="#000099") +
scale_x_date(breaks = "1 year", minor_breaks = "1 month") + xlab("Time") + ylab("Jacard Distance")