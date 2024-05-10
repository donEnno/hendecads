library(kernlab)

sitewise_anova = function(X, groups, alignmentColumns, fdr) {
  weights = table(groups)
  vals=sapply(unique(alignmentColumns), function(x) {
    dat = apply(X[,alignmentColumns==x],1,sum)
    SVM = ksvm(dat, groups, C=0.5, class.weights=weights, kernel="vanilladot")
    val = error(SVM)
    return(val)
  })
  scores=vals
  #BUM=fitBumModel(vals,plot=FALSE)
  #scores = scoreFunction(BUM, fdr)
  finalScores = scores
  names(finalScores)=unique(alignmentColumns)
  
  return(finalScores)
}

