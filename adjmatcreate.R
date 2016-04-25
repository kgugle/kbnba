ball<-read.csv("BASKETBALL.csv")
dim(ball)
#4097 57



yr.seq<-seq(2,56,by=2)
team.seq<-seq(3,57,by=2)

for(m in team.seq) ball[,m]<-as.character(levels(ball[,m]))[ball[,m]]

adj.matrix<-matrix(0,4097,4097)
for(i in 1:4096){
    for(j in (i+1):4097){
            first.yr.seq<-ball[i,yr.seq][!is.na(ball[i,yr.seq])]
            second.yr.seq<-ball[j,yr.seq][!is.na(ball[j,yr.seq])]
            if(length(intersect(first.yr.seq,second.yr.seq))!=0){
                first.tm.seq<-ball[i,team.seq][ball[i,team.seq]!=""]
                second.tm.seq<-ball[j,team.seq][ball[j,team.seq]!=""]
                if(length(intersect(first.tm.seq,second.tm.seq))!=0){
                   person1<-cbind(first.yr.seq,first.tm.seq)
                   ret.first<-which(first.tm.seq=="RET")
                   if(length(ret.first)!=0) person1<-person1[-which(first.tm.seq=="RET"),]
                   person2<-cbind(second.yr.seq,second.tm.seq)
                   ret.second<-which(second.tm.seq=="RET")
                   if(length(ret.second)!=0) person2<-person2[-which(second.tm.seq=="RET"),]
                   n.match<-0
                   for(k in 1:nrow(person1)){
                           n.match<-n.match+sum(apply(person2,1,setequal,person1[k,]))
                   }    
                   adj.matrix[i,j]<-adj.matrix[j,i]<-n.match
                }                   
            }        
        print(j)    
    }
    print(paste("i=",i))
}

write.table(adj.matrix,"adjmatrix.txt")
