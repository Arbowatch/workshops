library(tidyverse)
library(sf)

# Load field data
df <- read_csv("field_data.csv")

# Summarise observations by site
df |>
  group_by(site, species) |>
  summarise(total = sum(count), .groups = "drop") |>
  arrange(site, desc(total))
