# example for ridge, lasso, and elastic-net regression, in R

# import glmnet library
library(glmnet)

# set seed for reproducibility
set.seed(42)

# create dataset
n <- 1000
p <- 5000
actual_p <- 15

# create design matrix
x <- matrix(rnorm(n * p), nrow = n, ncol = p)

# create vector of true coefficients
y <- apply(x[, 1:actual_p], 1, sum) + rnorm(n)

# divide data into training and test sets
train_rows <- sample(1:n, 0.66 * n)
x_train <- x[train_rows, ]
x_test <- x[-train_rows, ]

y_train <- y[train_rows]
y_test <- y[-train_rows]


# fit ridge regression model
alpha0_fit <- cv.glmnet(x_train, y_train,
    type.measure = "mse",
    alpha = 0, family = "gaussian"
)

alpha0_predicted <- predict(alpha0_fit, s = alpha0_fit$lambda.1se, newx = x_test)

mean((y_test - alpha0_predicted)^2)


# fit lasso regression model
alpha1_fit <- cv.glmnet(x_train, y_train,
    type.measure = "mse",
    alpha = 1, family = "gaussian"
)

alpha1_predicted <- predict(alpha1_fit, s = alpha1_fit$lambda.1se, newx = x_test)

mean((y_test - alpha1_predicted)^2)


# fit elastic-net regression model (alpha = 0.5)
alpha0.5_fit <- cv.glmnet(x_train, y_train, # nolint
    type.measure = "mse",
    alpha = 0.5, family = "gaussian"
)

alpha0.5_predicted <- predict(alpha0.5_fit, s = alpha0.5_fit$lambda.1se, newx = x_test)

mean((y_test - alpha0.5_predicted)^2)


# use different values of alpha
list_of_fits <- list()

# fit models for alpha = 0, 0.1, 0.2, ..., 1
for (i in 0:10) {
    fit_name <- paste0("alpha", i / 10)

    list_of_fits[[fit_name]] <- cv.glmnet(x_train, y_train, # nolint
        type.measure = "mse",
        alpha = i / 10, family = "gaussian"
    )
}

# create dataframe to store results
results <- data.frame()

# test models on test set
for (i in 0:10) {
    fit_name <- paste0("alpha", i / 10)

    predicted <- predict(list_of_fits[[fit_name]], s = list_of_fits[[fit_name]]$lambda.1se, newx = x_test) # nolint

    mse <- mean((y_test - predicted) ^ 2)

    temp <- data.frame(alpha=i/10, mse=mse, fit_name=fit_name)
    results <- rbind(results, temp)
}

print(results)