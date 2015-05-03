library(RColorBrewer)

data <- read.table("mementoCount.txt",header=FALSE)
finalData = rep(data[,1])
title <- "CDF for # of mementos for each original URI "
xlab <- "# of Mementos"
ylab <- "% of links"
P1 = ecdf(finalData)
png("mementoCount.png")

p1 <- plot(P1,col="blue", main=title, xlab=xlab, ylab=ylab)
