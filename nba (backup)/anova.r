library(readr)
library(ggplot2)

fp <- "./data/nba_2015.csv"

nba_data <- read_csv(fp)

nba_model <- lm(nba_data$trb_per_36_min ~ pos, data = nba_data)

print(anova(nba_model))