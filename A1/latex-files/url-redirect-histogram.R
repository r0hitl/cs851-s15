redirects=read.csv("tweets-processed-1.txt",stringsAsFactors=F,header=FALSE,sep="\t")
redirects
data=redirects[,1]
png("url-redirect-histogram.png")
hist(data,main="Url Redirects Frequency Distribution ",freq=T,xlab="Number of Redirects",ylab="Frequency")
dev.off()
