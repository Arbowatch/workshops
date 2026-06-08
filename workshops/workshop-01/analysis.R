library(tidyverse)

# Load example dataset
df <- read_csv("data.csv")

# Quick summary
glimpse(df)

df |>
  ggplot(aes(x = species, y = count)) +
  geom_col() +
  theme_minimal() +
  labs(title = "Species Counts - Workshop 01")
