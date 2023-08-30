## In this example, we show how to do a t-test and regression at the same
## time...
Type <- factor(c(
    rep("Control", times = 4),
    rep("Mutant", times = 4)
))
Weight <- c(2.4, 3.5, 4.4, 4.9, 1.7, 2.8, 3.2, 3.9)
Size <- c(1.9, 3, 2.9, 3.7, 2.8, 3.3, 3.9, 4.8)

print(model.matrix(~ Type + Weight))

model <- lm(Size ~ Type + Weight)
print(summary(model))


# plot the data with a scatter plot
# draw line for their respective best fit lines
p <- ggplot(data.frame(Type, Weight, Size), aes(
    x = Weight,
    y = Size,
    color = Type
)) +
    geom_point() +
    geom_smooth(method = "lm", se = FALSE) +
    labs(
        title = "Predicting Mouse Size from Weight and Type (same slope)",
        subtitle = "Mouse Size vs. Weight",
        x = "Weight",
        y = "Size"
    ) +
    theme_minimal()

print(p)
