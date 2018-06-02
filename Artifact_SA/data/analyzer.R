library(tidyr)
library(dplyr)

setwd("~/Documents/Papers/FSE18-NIER-testrefactoring/Artifact_SA/data/elasticsearch")
results <- read.table(
  file = "elasticsearch-monthly-metrics.csv", 
  sep = ',', 
  header = T)

new_results <- results %>% filter(hash == "72b9859bd572e824654245a57bbe8e192d97a3af")

class_pairs <- read.table(
  file = "elasticsearch-class-pairs.csv", 
  sep = ',', 
  header = F)
colnames(class_pairs) <- c("commit", "prod_name", "test_name")

for(i in 1:nrow(new_results)) {
  row <- new_results[i,]
  filename <- row$file
  if (row$fileType == "ProductionFile"){
    test_filename <- class_pairs %>% filter(prod_name == "filename")
  }
}
