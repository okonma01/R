library(readr)
library(ggplot2)

fp <- "./data/nba_2015.csv"

nba_data <- read_csv(fp)

# Plot data with scatter plot (without info for each point)
p <- ggplot(nba_data, aes(x = pos, y = trb_per_36_min)) +
    geom_point() +
    stat_summary(fun = mean, geom = "crossbar", width = 0.75, col = "blue") +
    labs(
        title = "NBA 2014/15",
        subtitle = "Total Rebounds per 36 Minutes by Position",
        x = "Position",
        y = "Total Rebounds per 36 Minutes"
    ) +
    theme_minimal()

print(p)