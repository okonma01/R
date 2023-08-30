library(readr)

fp <- "data/nba_2015.csv"

nba_data <- read.csv(fp)

p <- plot(nba_data$fga_per_36_min, nba_data$pts_per_36_min,
    xlab = "Field Goal Attempts per 36 Minutes",
    ylab = "Points per 36 Minutes",
    main = "NBA 2014/15",
    sub = "Points per 36 Minutes vs. Field Goal Attempts per 36 Minutes",
    # col = "blue",
    pch = 16
)

nba_regression <- lm(nba_data$pts_per_36_min ~ nba_data$fga_per_36_min)

summary(nba_regression)

abline(nba_regression, col = "blue")

print(p)