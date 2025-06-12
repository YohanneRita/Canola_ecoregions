# Load required libraries
{library(ggplot2)
library(dplyr)
library(tidyr)
library(gridExtra)
library(viridis)
library(sf)
#library(ggnewscale)
library(RColorBrewer)
library(cowplot)}

#Read Shapefile
WAT126 <- st_read('./GWSens_126.shp')

{# Calculate mean Temperature
Tmin <- as.numeric(WAT126$TMIN)
Tmax <- as.numeric(WAT126$TMAX)
Temp <- data.frame(Tmax, Tmax)
MeanT <- rowMeans(Temp, na.rm = TRUE)
Precc <- (as.numeric(WAT126$SW1D)+as.numeric(WAT126$SW2D)+as.numeric(WAT126$SW3D)+as.numeric(WAT126$SW4D)+as.numeric(WAT126$SW5D))/5 # 60cm LAYERS
Lat <- as.numeric(WAT126$LATITUDE)
Lon <- as.numeric(WAT126$LONGITUDE)
Year <- as.Date(WAT126$time)
Yield <- as.numeric(WAT126$HWAH)
Region <- WAT126$REGION_NAM

# Create the Pronto dataframe
Pronto <- data.frame(Year, Lat, Lon, MeanT, Precc, Yield, Region)
Pronto <- na.omit(Pronto)
Pronto$Region[Pronto$Region == 'Aspen Parkland'] <- 1
Pronto$Region[Pronto$Region == 'Cypress Upland'] <- 2
Pronto$Region[Pronto$Region == 'Fescue Grassland'] <- 3
Pronto$Region[Pronto$Region == 'Lake Manitoba Plain'] <- 4
Pronto$Region[Pronto$Region == 'Mixed Grassland'] <- 5
Pronto$Region[Pronto$Region == 'Moist Mixed Grassland'] <- 6
Pronto$Region[Pronto$Region == 'Southwest Manotoba Uplands'] <- 7
Pronto$MeanT <- ifelse(Pronto$MeanT < 17, NA, Pronto$MeanT)

# Define unified grid intervals
temp_min <- floor(min(Pronto$MeanT)) - 1
temp_max <- ceiling(max(Pronto$MeanT)) + 1
precip_min <- round(min(Pronto$Precc), 2) - 0.01 #LAYER
precip_max <- round(max(Pronto$Precc), 2) + 0.01

temp_intervals <- seq(19, 31, by = 1)
precip_intervals <- seq(0.1,0.3, by = 0.05) # LAYER

# Categorize data into grid bins
Pronto <- Pronto %>%
  mutate(
    Temp_Range = cut(MeanT, breaks = temp_intervals, include.lowest = TRUE, right = FALSE),
    Precip_Range = cut(Precc, breaks = precip_intervals, include.lowest = TRUE, right = FALSE)
  )

# Compute average yield in each grid
grid_overlay <- Pronto %>%
  filter(!is.na(Yield) & !is.na(Precip_Range) & !is.na(Temp_Range)) %>%
  group_by(Precip_Range, Temp_Range) %>%
  summarise(
    Avg_Yield = mean(Yield, na.rm = TRUE),
    Max_Yield = max(Yield, na.rm = TRUE),
    Center_Temp = mean(as.numeric(gsub("[^0-9.-]", "", unlist(strsplit(as.character(Temp_Range), ","))))),
    Center_Precip = mean(as.numeric(gsub("[^0-9.-]", "", unlist(strsplit(as.character(Precip_Range), ","))))),
    .groups = 'drop'
  )

# Convert to factors for plotting
grid_overlay <- grid_overlay %>%
  mutate(
    Temp_Range = as.factor(Temp_Range),
    Precip_Range = as.factor(Precip_Range)
  )

grid_overlay2 <- Pronto %>%
  filter(!is.na(Yield) & !is.na(Region) & !is.na(Precip_Range) & !is.na(Temp_Range)) %>%
  group_by(Region) %>%
  summarise(
    Avg_Yield = mean(Yield, na.rm = TRUE),
    Max_Yield = max(Yield, na.rm = TRUE),
    Center_Temp = mean(as.numeric(gsub("[^0-9.-]", "", unlist(strsplit(as.character(Temp_Range), ","))))),
    Center_Precip = mean(as.numeric(gsub("[^0-9.-]", "", unlist(strsplit(as.character(Precip_Range), ","))))),
    .groups = 'drop'
  )

grid_overlay2 <- grid_overlay2 %>%
  mutate(
    Region = as.numeric(Region))


grid_overlay2$Ecoregion <- cut(grid_overlay2$Region, breaks = 7,
                                   labels = c('Aspen Parkland','Cypress Upland',
                                              'Fescue Grassland','Lake Manitoba Plain','Mixed Grassland',
                                              'Moist Mixed Grassland','Southwest Manitoba Uplands'))

}

# ----------------- SCATTER PLOT SSP1-2.6 -----------------
scatter_plot <- ggplot(Pronto, aes(x = Precc, y = MeanT, fill = Yield)) +
  geom_point(size = 3, alpha = 0.3, shape = 21, color=scales::alpha("white", 1), stroke = 0.05, show.legend = F) +
  scale_fill_viridis_c(name = "Yield (kg/ha)", option = "viridis", limits = c(20, 2761), direction = -1) +

  # Add grid lines
  geom_vline(xintercept = precip_intervals, color = "#DFDFDF", lwd = 0.5) +
  geom_hline(yintercept = temp_intervals, color = "#DFDFDF", lwd = 0.5) +

  # Add small squares at grid centers
  geom_point(data = grid_overlay, mapping = aes(x = Center_Precip, y = Center_Temp, fill = Avg_Yield), show.legend = F,
             shape = 22, size = 3, color = "black", stroke = 0.4) +

  labs(title = "SSP1-2.6",
       x = expression("Soil Water Content (cm"^3*" cm"^-3*")"),
       y = "Mean Temperature (°C)",
       color = "Ecoregion") +

  scale_x_continuous(breaks = precip_intervals) +
  scale_y_continuous(breaks = temp_intervals) +

  # Add points for regions
  geom_point(data = grid_overlay2, mapping = aes(x = Center_Precip, y = Center_Temp, fill = Max_Yield, color = Ecoregion), show.legend = F,
             shape = 21, size = 4, stroke = 1.1) +
  scale_color_manual(values = c('#ec111a', '#fb6330', '#ffd42f', '#138468', '#009dd6', '#7849b8', '#f2609e')) +

  theme_minimal() +
  theme(plot.title = element_text(size = 10, hjust = 0.5),
        axis.title = element_text(size = 8),
        axis.text = element_text(size = 8),
        legend.title = element_text(size = 8),
        legend.text = element_text(size = 8),
        axis.text.x = element_text(hjust = 0.5),
        axis.text.y = element_text(angle = 90, hjust = 0.5),
        panel.grid = element_blank())

scatter_plot

#Read Shapefile
WAT245 <- st_read('./GWSens_245.shp')

{# Calculate mean Temperature
  Tmin <- as.numeric(WAT245$TMIN)
  Tmax <- as.numeric(WAT245$TMAX)
  Temp <- data.frame(Tmax, Tmax)
  MeanT <- rowMeans(Temp, na.rm = TRUE)
  Precc <- (as.numeric(WAT245$SW1D)+as.numeric(WAT245$SW2D)+as.numeric(WAT245$SW3D)+as.numeric(WAT245$SW4D)+as.numeric(WAT245$SW5D))/5 # 60cm LAYERS
  Lat <- as.numeric(WAT245$LATITUDE)
  Lon <- as.numeric(WAT245$LONGITUDE)
  Year <- as.Date(WAT245$time)
  Yield <- as.numeric(WAT245$HWAH)
  Region <- WAT245$REGION_NAM

  # Create the Pronto dataframe
  Pronto <- data.frame(Year, Lat, Lon, MeanT, Precc, Yield, Region)
  Pronto <- na.omit(Pronto)
  Pronto$Region[Pronto$Region == 'Aspen Parkland'] <- 1
  Pronto$Region[Pronto$Region == 'Cypress Upland'] <- 2
  Pronto$Region[Pronto$Region == 'Fescue Grassland'] <- 3
  Pronto$Region[Pronto$Region == 'Lake Manitoba Plain'] <- 4
  Pronto$Region[Pronto$Region == 'Mixed Grassland'] <- 5
  Pronto$Region[Pronto$Region == 'Moist Mixed Grassland'] <- 6
  Pronto$Region[Pronto$Region == 'Southwest Manotoba Uplands'] <- 7
  Pronto$MeanT <- ifelse(Pronto$MeanT < 17, NA, Pronto$MeanT)

  # Define unified grid intervals
  temp_min <- floor(min(Pronto$MeanT)) - 1
  temp_max <- ceiling(max(Pronto$MeanT)) + 1
  precip_min <- round(min(Pronto$Precc), 2) - 0.01 #LAYER
  precip_max <- round(max(Pronto$Precc), 2) + 0.01

  temp_intervals <- seq(19, 31, by = 1)
  precip_intervals <- seq(0.1,0.3, by = 0.05) # LAYER

  # Categorize data into grid bins
  Pronto <- Pronto %>%
    mutate(
      Temp_Range = cut(MeanT, breaks = temp_intervals, include.lowest = TRUE, right = FALSE),
      Precip_Range = cut(Precc, breaks = precip_intervals, include.lowest = TRUE, right = FALSE)
    )

  # Compute average yield in each grid
  grid_overlay <- Pronto %>%
    filter(!is.na(Yield) & !is.na(Precip_Range) & !is.na(Temp_Range)) %>%
    group_by(Precip_Range, Temp_Range) %>%
    summarise(
      Avg_Yield = mean(Yield, na.rm = TRUE),
      Max_Yield = max(Yield, na.rm = TRUE),
      Center_Temp = mean(as.numeric(gsub("[^0-9.-]", "", unlist(strsplit(as.character(Temp_Range), ","))))),
      Center_Precip = mean(as.numeric(gsub("[^0-9.-]", "", unlist(strsplit(as.character(Precip_Range), ","))))),
      .groups = 'drop'
    )

  # Convert to factors for plotting
  grid_overlay <- grid_overlay %>%
    mutate(
      Temp_Range = as.factor(Temp_Range),
      Precip_Range = as.factor(Precip_Range)
    )

  grid_overlay2 <- Pronto %>%
    filter(!is.na(Yield) & !is.na(Region) & !is.na(Precip_Range) & !is.na(Temp_Range)) %>%
    group_by(Region) %>%
    summarise(
      Avg_Yield = mean(Yield, na.rm = TRUE),
      Max_Yield = max(Yield, na.rm = TRUE),
      Center_Temp = mean(as.numeric(gsub("[^0-9.-]", "", unlist(strsplit(as.character(Temp_Range), ","))))),
      Center_Precip = mean(as.numeric(gsub("[^0-9.-]", "", unlist(strsplit(as.character(Precip_Range), ","))))),
      .groups = 'drop'
    )

  grid_overlay2 <- grid_overlay2 %>%
    mutate(
      Region = as.numeric(Region))


  grid_overlay2$Ecoregion <- cut(grid_overlay2$Region, breaks = 7,
                                 labels = c('Aspen Parkland','Cypress Upland',
                                            'Fescue Grassland','Lake Manitoba Plain','Mixed Grassland',
                                            'Moist Mixed Grassland','Southwest Manitoba Uplands'))

}

# ----------------- SCATTER PLOT SSP2-4.5 -----------------
scatter_plotB <- ggplot(Pronto, aes(x = Precc, y = MeanT, fill = Yield)) +
  geom_point(size = 3, alpha = 0.3, shape = 21, color=scales::alpha("white", 1), stroke = 0.05, show.legend = F) +
  scale_fill_viridis_c(name = "Yield (kg/ha)", option = "viridis", limits = c(20, 2761), direction = -1) +

  # Add grid lines
  geom_vline(xintercept = precip_intervals, color = "#DFDFDF", lwd = 0.5) +
  geom_hline(yintercept = temp_intervals, color = "#DFDFDF", lwd = 0.5) +

  # Add small squares at grid centers
  geom_point(data = grid_overlay, mapping = aes(x = Center_Precip, y = Center_Temp, fill = Avg_Yield), show.legend = F,
             shape = 22, size = 3, color = "black", stroke = 0.4) +

  labs(title = "SSP2-4.5",
       x = expression("Soil Water Content (cm"^3*" cm"^-3*")"),
       y = "Mean Temperature (°C)",
       color = "Ecoregion") +

  scale_x_continuous(breaks = precip_intervals) +
  scale_y_continuous(breaks = temp_intervals) +

  # Add points for regions
  geom_point(data = grid_overlay2, mapping = aes(x = Center_Precip, y = Center_Temp, fill = Max_Yield, color = Ecoregion), show.legend = F,
             shape = 21, size = 4, stroke = 1.1) +
  scale_color_manual(values = c('#ec111a', '#fb6330', '#ffd42f', '#138468', '#009dd6', '#7849b8', '#f2609e')) +

  theme_minimal() +
  theme(plot.title = element_text(size = 10, hjust = 0.5),
        axis.title = element_text(size = 8),
        axis.text = element_text(size = 8),
        legend.title = element_text(size = 8),
        legend.text = element_text(size = 8),
        axis.text.x = element_text(hjust = 0.5),
        axis.text.y = element_text(angle = 90, hjust = 0.5),
        panel.grid = element_blank())

scatter_plotB

#Read Shapefile
WAT370 <- st_read('./GWSens_370.shp')

{# Calculate mean Temperature
  Tmin <- as.numeric(WAT370$TMIN)
  Tmax <- as.numeric(WAT370$TMAX)
  Temp <- data.frame(Tmax, Tmax)
  MeanT <- rowMeans(Temp, na.rm = TRUE)
  Precc <- (as.numeric(WAT370$SW1D)+as.numeric(WAT370$SW2D)+as.numeric(WAT370$SW3D)+as.numeric(WAT370$SW4D)+as.numeric(WAT370$SW5D))/5 # 60cm LAYERS
  Lat <- as.numeric(WAT370$LATITUDE)
  Lon <- as.numeric(WAT370$LONGITUDE)
  Year <- as.Date(WAT370$time)
  Yield <- as.numeric(WAT370$HWAH)
  Region <- WAT370$REGION_NAM

  # Create the Pronto dataframe
  Pronto <- data.frame(Year, Lat, Lon, MeanT, Precc, Yield, Region)
  Pronto <- na.omit(Pronto)
  Pronto$Region[Pronto$Region == 'Aspen Parkland'] <- 1
  Pronto$Region[Pronto$Region == 'Cypress Upland'] <- 2
  Pronto$Region[Pronto$Region == 'Fescue Grassland'] <- 3
  Pronto$Region[Pronto$Region == 'Lake Manitoba Plain'] <- 4
  Pronto$Region[Pronto$Region == 'Mixed Grassland'] <- 5
  Pronto$Region[Pronto$Region == 'Moist Mixed Grassland'] <- 6
  Pronto$Region[Pronto$Region == 'Southwest Manotoba Uplands'] <- 7
  Pronto$MeanT <- ifelse(Pronto$MeanT < 17, NA, Pronto$MeanT)

  # Define unified grid intervals
  temp_min <- floor(min(Pronto$MeanT)) - 1
  temp_max <- ceiling(max(Pronto$MeanT)) + 1
  precip_min <- round(min(Pronto$Precc), 2) - 0.01 #LAYER
  precip_max <- round(max(Pronto$Precc), 2) + 0.01

  temp_intervals <- seq(19, 31, by = 1)
  precip_intervals <- seq(0.1,0.3, by = 0.05) # LAYER

  # Categorize data into grid bins
  Pronto <- Pronto %>%
    mutate(
      Temp_Range = cut(MeanT, breaks = temp_intervals, include.lowest = TRUE, right = FALSE),
      Precip_Range = cut(Precc, breaks = precip_intervals, include.lowest = TRUE, right = FALSE)
    )

  # Compute average yield in each grid
  grid_overlay <- Pronto %>%
    filter(!is.na(Yield) & !is.na(Precip_Range) & !is.na(Temp_Range)) %>%
    group_by(Precip_Range, Temp_Range) %>%
    summarise(
      Avg_Yield = mean(Yield, na.rm = TRUE),
      Max_Yield = max(Yield, na.rm = TRUE),
      Center_Temp = mean(as.numeric(gsub("[^0-9.-]", "", unlist(strsplit(as.character(Temp_Range), ","))))),
      Center_Precip = mean(as.numeric(gsub("[^0-9.-]", "", unlist(strsplit(as.character(Precip_Range), ","))))),
      .groups = 'drop'
    )

  # Convert to factors for plotting
  grid_overlay <- grid_overlay %>%
    mutate(
      Temp_Range = as.factor(Temp_Range),
      Precip_Range = as.factor(Precip_Range)
    )

  grid_overlay2 <- Pronto %>%
    filter(!is.na(Yield) & !is.na(Region) & !is.na(Precip_Range) & !is.na(Temp_Range)) %>%
    group_by(Region) %>%
    summarise(
      Avg_Yield = mean(Yield, na.rm = TRUE),
      Max_Yield = max(Yield, na.rm = TRUE),
      Center_Temp = mean(as.numeric(gsub("[^0-9.-]", "", unlist(strsplit(as.character(Temp_Range), ","))))),
      Center_Precip = mean(as.numeric(gsub("[^0-9.-]", "", unlist(strsplit(as.character(Precip_Range), ","))))),
      .groups = 'drop'
    )

  grid_overlay2 <- grid_overlay2 %>%
    mutate(
      Region = as.numeric(Region))


  grid_overlay2$Ecoregion <- cut(grid_overlay2$Region, breaks = 7,
                                 labels = c('Aspen Parkland','Cypress Upland',
                                            'Fescue Grassland','Lake Manitoba Plain','Mixed Grassland',
                                            'Moist Mixed Grassland','Southwest Manitoba Uplands'))
}

# ----------------- SCATTER PLOT SSP3-7.0 -----------------
scatter_plotC <- ggplot(Pronto, aes(x = Precc, y = MeanT, fill = Yield)) +
  geom_point(size = 3, alpha = 0.3, shape = 21, color=scales::alpha("white", 1), stroke = 0.05, show.legend = F) +
  scale_fill_viridis_c(name = "Yield (kg/ha)", option = "viridis", limits = c(20, 2761), direction = -1) +

  # Add grid lines
  geom_vline(xintercept = precip_intervals, color = "#DFDFDF", lwd = 0.5) +
  geom_hline(yintercept = temp_intervals, color = "#DFDFDF", lwd = 0.5) +

  # Add small squares at grid centers
  geom_point(data = grid_overlay, mapping = aes(x = Center_Precip, y = Center_Temp, fill = Avg_Yield), show.legend = F,
             shape = 22, size = 3, color = "black", stroke = 0.4) +

  labs(title = "SSP3-7.0",
       x = expression("Soil Water Content (cm"^3*" cm"^-3*")"),
       y = "Mean Temperature (°C)",
       color = "Ecoregion") +

  scale_x_continuous(breaks = precip_intervals) +
  scale_y_continuous(breaks = temp_intervals) +

  # Add points for regions
  geom_point(data = grid_overlay2, mapping = aes(x = Center_Precip, y = Center_Temp, fill = Max_Yield, color = Ecoregion), show.legend = F,
             shape = 21, size = 4, stroke = 1.1) +
  scale_color_manual(values = c('#ec111a', '#fb6330', '#ffd42f', '#138468', '#009dd6', '#7849b8', '#f2609e')) +

  theme_minimal() +
  theme(plot.title = element_text(size = 10, hjust = 0.5),
        axis.title = element_text(size = 8),
        axis.text = element_text(size = 8),
        legend.title = element_text(size = 8),
        legend.text = element_text(size = 8),
        axis.text.x = element_text(hjust = 0.5),
        axis.text.y = element_text(angle = 90, hjust = 0.5),
        panel.grid = element_blank())

scatter_plotC

#Read Shapefile
WAT585 <- st_read('./GWSens_585.shp')

{# Calculate mean Temperature
  Tmin <- as.numeric(WAT585$TMIN)
  Tmax <- as.numeric(WAT585$TMAX)
  Temp <- data.frame(Tmax, Tmax)
  MeanT <- rowMeans(Temp, na.rm = TRUE)
  Precc <- (as.numeric(WAT585$SW1D)+as.numeric(WAT585$SW2D)+as.numeric(WAT585$SW3D)+as.numeric(WAT585$SW4D)+as.numeric(WAT585$SW5D))/5 # 60cm LAYERS
  Lat <- as.numeric(WAT585$LATITUDE)
  Lon <- as.numeric(WAT585$LONGITUDE)
  Year <- as.Date(WAT585$time)
  Yield <- as.numeric(WAT585$HWAH)
  Region <- WAT585$REGION_NAM

  # Create the Pronto dataframe
  Pronto <- data.frame(Year, Lat, Lon, MeanT, Precc, Yield, Region)
  Pronto <- na.omit(Pronto)
  Pronto$Region[Pronto$Region == 'Aspen Parkland'] <- 1
  Pronto$Region[Pronto$Region == 'Cypress Upland'] <- 2
  Pronto$Region[Pronto$Region == 'Fescue Grassland'] <- 3
  Pronto$Region[Pronto$Region == 'Lake Manitoba Plain'] <- 4
  Pronto$Region[Pronto$Region == 'Mixed Grassland'] <- 5
  Pronto$Region[Pronto$Region == 'Moist Mixed Grassland'] <- 6
  Pronto$Region[Pronto$Region == 'Southwest Manotoba Uplands'] <- 7
  Pronto$MeanT <- ifelse(Pronto$MeanT < 17, NA, Pronto$MeanT)

  # Define unified grid intervals
  temp_min <- floor(min(Pronto$MeanT)) - 1
  temp_max <- ceiling(max(Pronto$MeanT)) + 1
  precip_min <- round(min(Pronto$Precc), 2) - 0.01 #LAYER
  precip_max <- round(max(Pronto$Precc), 2) + 0.01

  temp_intervals <- seq(19, 31, by = 1)
  precip_intervals <- seq(0.1,0.3, by = 0.05) # LAYER

  # Categorize data into grid bins
  Pronto <- Pronto %>%
    mutate(
      Temp_Range = cut(MeanT, breaks = temp_intervals, include.lowest = TRUE, right = FALSE),
      Precip_Range = cut(Precc, breaks = precip_intervals, include.lowest = TRUE, right = FALSE)
    )

  # Compute average yield in each grid
  grid_overlay <- Pronto %>%
    filter(!is.na(Yield) & !is.na(Precip_Range) & !is.na(Temp_Range)) %>%
    group_by(Precip_Range, Temp_Range) %>%
    summarise(
      Avg_Yield = mean(Yield, na.rm = TRUE),
      Max_Yield = max(Yield, na.rm = TRUE),
      Center_Temp = mean(as.numeric(gsub("[^0-9.-]", "", unlist(strsplit(as.character(Temp_Range), ","))))),
      Center_Precip = mean(as.numeric(gsub("[^0-9.-]", "", unlist(strsplit(as.character(Precip_Range), ","))))),
      .groups = 'drop'
    )

  # Convert to factors for plotting
  grid_overlay <- grid_overlay %>%
    mutate(
      Temp_Range = as.factor(Temp_Range),
      Precip_Range = as.factor(Precip_Range)
    )

  grid_overlay2 <- Pronto %>%
    filter(!is.na(Yield) & !is.na(Region) & !is.na(Precip_Range) & !is.na(Temp_Range)) %>%
    group_by(Region) %>%
    summarise(
      Avg_Yield = mean(Yield, na.rm = TRUE),
      Max_Yield = max(Yield, na.rm = TRUE),
      Center_Temp = mean(as.numeric(gsub("[^0-9.-]", "", unlist(strsplit(as.character(Temp_Range), ","))))),
      Center_Precip = mean(as.numeric(gsub("[^0-9.-]", "", unlist(strsplit(as.character(Precip_Range), ","))))),
      .groups = 'drop'
    )

  grid_overlay2 <- grid_overlay2 %>%
    mutate(
      Region = as.numeric(Region))


  grid_overlay2$Ecoregion <- cut(grid_overlay2$Region, breaks = 7,
                                 labels = c('Aspen Parkland','Cypress Upland',
                                            'Fescue Grassland','Lake Manitoba Plain','Mixed Grassland',
                                            'Moist Mixed Grassland','Southwest Manitoba Uplands'))
}

# ----------------- SCATTER PLOT SSP5-8.5 -----------------
scatter_plotD <- ggplot(Pronto, aes(x = Precc, y = MeanT, fill = Yield)) +
  geom_point(size = 3, alpha = 0.3, shape = 21, color=scales::alpha("white", 1), stroke = 0.05, show.legend = F) +
  scale_fill_viridis_c(name = "Yield (kg/ha)", option = "viridis", limits = c(20, 2761), direction = -1) +

  # Add grid lines
  geom_vline(xintercept = precip_intervals, color = "#DFDFDF", lwd = 0.5) +
  geom_hline(yintercept = temp_intervals, color = "#DFDFDF", lwd = 0.5) +

  # Add small squares at grid centers
  geom_point(data = grid_overlay, mapping = aes(x = Center_Precip, y = Center_Temp, fill = Avg_Yield), show.legend = F,
             shape = 22, size = 3, color = "black", stroke = 0.4) +

  labs(title = "SSP5-8.5",
       x = expression("Soil Water Content (cm"^3*" cm"^-3*")"),
       y = "Mean Temperature (°C)",
       color = "Ecoregion") +

  scale_x_continuous(breaks = precip_intervals) +
  scale_y_continuous(breaks = temp_intervals) +

  # Add points for regions
  geom_point(data = grid_overlay2, mapping = aes(x = Center_Precip, y = Center_Temp, fill = Max_Yield, color = Ecoregion), show.legend = F,
             shape = 21, size = 4, stroke = 1.1) +
  scale_color_manual(values = c('#ec111a', '#fb6330', '#ffd42f', '#138468', '#009dd6', '#7849b8', '#f2609e')) +

  theme_minimal() +
  theme(plot.title = element_text(size = 10, hjust = 0.5),
        axis.title = element_text(size = 8),
        axis.text = element_text(size = 8),
        legend.title = element_text(size = 8),
        legend.text = element_text(size = 8),
        axis.text.x = element_text(hjust = 0.5),
        axis.text.y = element_text(angle = 90, hjust = 0.5),
        panel.grid = element_blank())

scatter_plotD

combined_plots <- grid.arrange(scatter_plot, scatter_plotB,scatter_plotC,scatter_plotD, ncol = 2,nrow=2)
ggsave(".\\ALL_scatterCM3.png", combined_plots, width = 10, height = 8, dpi=400, bg = "white")
