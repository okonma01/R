library(readr)
library(ggplot2)

fp <- "data/nba_2015.csv"

# read in the data
nba_data <- read_csv(fp)

# create a design matrix with pos and blk_per_36_min as predictors
design_matrix <- model.matrix(~ pos * blk_per_36_min, data = nba_data)

# fit a linear regression model with trb_per_36_min as the response variable,
# and the design matrix as the predictor matrix
nba_regression <- lm(nba_data$trb_per_36_min ~ design_matrix)

# print the summary of the regression model
summary(nba_regression)

# plot the data with a scatter plot
# draw line for their respective best fit lines
p <- ggplot(nba_data, aes(
    x = blk_per_36_min,
    y = trb_per_36_min,
    color = pos
)) +
    geom_point() +
    geom_smooth(method = "lm", se = FALSE) +
    labs(
        title = "NBA 2014/15",
        subtitle = "Total Rebounds per 36 Minutes vs. Blocks per 36 Minutes",
        x = "Blocks per 36 Minutes",
        y = "Total Rebounds per 36 Minutes"
    ) +
    theme_minimal()

print(p)
