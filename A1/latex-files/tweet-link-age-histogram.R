inputFile=read.csv("url-dates.csv",stringsAsFactors=F,header=FALSE,sep="\t")
inputFile
data=inputFile[,1]
png("tweet-link-age-histogram.png")
hist(data,main="Tweet Links Date Delta",freq=T,xlab="Date Delta",ylab="Frequency")
dev.off()
