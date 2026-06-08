library(tidyverse)

df <- read_csv("arbowatch_data.csv")

# Clean data
df_clean <- df |>
  drop_na(species, count) |>
  filter(count > 0) |>
  mutate(date = as.Date(date))

# Summarise by species
species_summary <- df_clean |>
  group_by(species) |>
  summarise(
    total_count = sum(count),
    n_sites = n_distinct(site),
    .groups = "drop"
  ) |>
  arrange(desc(total_count))

# Visualise top 10
species_summary |>
  slice_max(total_count, n = 10) |>
  ggplot(aes(x = reorder(species, total_count), y = total_count)) +
  geom_col(fill = "#2E7D32") +
  coord_flip() +
  theme_minimal() +
  labs(
    title = "Top 10 Most Observed Species",
    x = "Species",
    y = "Total Count"
  )
