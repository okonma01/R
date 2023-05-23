data <- read.csv("data/heart-failure.csv")


# convert chr to factor
data$Sex <- as.factor(data$Sex)
data$ChestPainType <- as.factor(data$ChestPainType)
data$RestingECG <- as.factor(data$RestingECG)
data$ExerciseAngina <- as.factor(data$ExerciseAngina)
data$ST_Slope <- as.factor(data$ST_Slope)

# convert hd to factor (0 = No, 1 = Yes)
data$HeartDisease <- ifelse(data$HeartDisease == 0, "No", "Yes")
data$HeartDisease <- as.factor(data$HeartDisease)

# check for any missing values
sum(is.na(data))

# print(str(data))

logistic <- glm(HeartDisease ~ ., data = data, family = "binomial")
print(summary(logistic))

ll.null <- logistic$null.deviance/-2
ll.proposed <- logistic$deviance/-2
r_squared <- (ll.null - ll.proposed) / ll.null

# print out the r-squared value (in the format, "R-squared: 0.000")
print(paste("McFadden's Pseudo R-squared:", round(r_squared, 3)))
