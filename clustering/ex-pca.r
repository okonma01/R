library(ggplot2)

# generate dataset
data_matrix <- matrix(nrow = 100, ncol = 10)

# set gene types
# wt stands for wild type, for normal genes
# ko stands for knock out, for abnormal genes
colnames(data_matrix) <- c(
    paste("wt", 1:5, sep = ""),
    paste("ko", 1:5, sep = "")
)

# set gene names (generically)
rownames(data_matrix) <- paste("gene", 1:100, sep = "")

# set gene values, using poisson distribution
for (i in 1:100) {
    wt_values <- rpois(5, lambda = sample(x = 10:1000, size = 1))
    ko_values <- rpois(5, lambda = sample(x = 10:1000, size = 1))

    data_matrix[i, ] <- c(wt_values, ko_values)
}

# print first 5 rows
print(head(data_matrix))

# do pca analysis
pca <- prcomp(t(data_matrix), scale = TRUE)

# plot the first two components
# print(plot(pca$x[, 1], pca$x[, 2], xlab = "PC1", ylab = "PC2", pch = 19, col = "blue"))

# plot scree plot
pca_var <- pca$sdev^2
pca_var_percent <- round(pca_var / sum(pca_var) * 100, 1)
scree_plot <- barplot(pca_var_percent, main = "Scree Plot", xlab = "Principal Component", ylab = "Percent Variation", col = "blue")
print(scree_plot)


# plot pca graph with ggplot2
pca_data <- data.frame(Sample=rownames(pca$x), PC1=pca$x[, 1], PC2=pca$x[, 2])
pca_plot <- ggplot(
    data = pca_data,
    aes(x = PC1, y = PC2, label = Sample)) +
    # geom_point() +
    geom_text() +
    xlab(paste("PC1 - ", pca_var_percent[1], "%", sep = "")) +
    ylab(paste("PC2 - ", pca_var_percent[2], "%", sep = "")) +
    theme_bw() +
    ggtitle("My PCA Graph")

print(pca_plot)

# print loading scores
loading_scores <- pca$rotation[, 1]
gene_scores <- abs(loading_scores)
gene_score_ranked <- sort(gene_scores, decreasing = TRUE)
top_10_genes <- names(gene_score_ranked[1:10])
print(top_10_genes)