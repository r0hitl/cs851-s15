inputFile=read.csv("http-statuses.txt",stringsAsFactors=F,header=FALSE,sep="\t")
inputFile
data=inputFile[,1]
png("http-statuses.png")
hist(data,main="HTTP Status",freq=T,xlab="Http Status",ylab="Frequency")
#barData <- table(data)
#png("http-statuses-bar.png")
#barplot(barData, main="HTTP Status", xlab="Http Status",ylab="Frequency")
dev.off()
