# reading the raw data
df <- data.frame(readxl::read_excel('C:/Users/pratikgl/Downloads/tTestData.xls'))

# pre processing
gene_names = df[, 1]
df = df[, -1]
df = df[c(-na_rows),]
gene_names = gene_names[-(na_rows)]

# Relevance using T test
# Gene_Selection function
Gene_Selection <- function(dataf, genenames, n){
  
  # calculating the start time
  start = Sys.time()
  df = data.frame(dataf)
  genes = genenames
  final_bucket = c()
  for(i in 1 : n){
    pvalues = c()
    for (j in 1 : nrow(df)){
      class1 = df[j,1:14]
      class2 = df[j,15:28]
      t_test = t.test(class1,class2)
      
      # t test calculation
      p <- t_test$p.value
      
      # p value calculation
      pvalues <- append(pvalues, p)
    }
    
    # sorting using p value
    sorted_pval <- sort(pvalues,index.return = T)   
    select_gene_index <- sorted_pval$ix[1]
    selected_gene <- genes[select_gene_index]
    final_bucket <- append(final_bucket, selected_gene)
    selected_gene_row <- df[select_gene_index,]
    corr_values <- c()
    for (k in 1 : nrow(df)){
     temp_row <- df[k,]
     corr <- cor(t(selected_gene_row),t(temp_row),method = 'pearson')
     corr_values <- append(corr_values,corr)
    }
    
    # taking the threshold value as 0.8
    to_remove_index_row <- which(corr_values > 0.8)
    df <- df[c(-(to_remove_index_row)),]
    genes <- genes[-(to_remove_index_row)]
  }
  end <- Sys.time()
  total_time <- round( end - start, digits = 4)
  print(final_bucket)  
  print(paste0('Time taken: ', total_time,' secs'))
}

# calling the Gene_Selection function
# selecting 50 genes
Gene_Selection(df,gene_names, 50)

