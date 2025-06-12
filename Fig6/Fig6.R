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
WATcur <- st_read('./GWSens_cur.shp')

{# Calculate mean Temperature
  Tmin <- as.numeric(WATcur$TMIN)
  Tmax <- as.numeric(WATcur$TMAX)
  Temp <- data.frame(Tmax, Tmax)
  MeanT <- rowMeans(Temp, na.rm = TRUE)
  Precc <- (as.numeric(WATcur$SW1D)+as.numeric(WATcur$SW2D)+as.numeric(WATcur$SW3D)+as.numeric(WATcur$SW4D)+as.numeric(WATcur$SW5D))/5 # 60cm LAYERS
  Lat <- as.numeric(WATcur$LATITUDE)
  Lon <- as.numeric(WATcur$LONGITUDE)
  Year <- as.Date(WATcur$time)
  Yield <- as.numeric(WATcur$HWAH)
  Region <- WATcur$REGION_NAM

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

  Pronto$Avg_Yield <- Pronto %>%
    group_by(Region) %>%
    mutate(Avg_Yield = mean(Yield, na.rm = TRUE))

  Pronto$Max_Yield <- Pronto %>%
    group_by(Region) %>%
    mutate(Max_Yield = max(Yield, na.rm = TRUE))

  Pronto <- Pronto %>%
    mutate(
      Region = as.numeric(Region))

  Pronto$Ecoregion <- cut(Pronto$Region, breaks = 7,
                          labels = c('Aspen Parkland','Cypress Upland',
                                     'Fescue Grassland','Lake Manitoba Plain','Mixed Grassland',
                                     'Moist Mixed Grassland','Southwest Manitoba Uplands'))

  Pronto$Avg_Yield$Avg_Yield <- as.numeric(as.character(Pronto$Avg_Yield$Avg_Yield))
  Pronto$Max_Yield$Max_Yield <- as.numeric(as.character(Pronto$Max_Yield$Max_Yield))
}

# ------ HISTROGRAM CURRENT ----------#

hist_plot <- ggplot(Pronto, aes(x = Yield, color = Ecoregion)) +
  geom_histogram(binwidth = 0.5,  alpha = 0.7, show.legend = F) +
  scale_color_manual(values = c('#ec111a', '#fb6330', '#ffd42f', '#138468', '#009dd6', '#7849b8', '#f2609e')) +
  # Add text annotations for mean values
  geom_text(aes(x = Avg_Yield$Avg_Yield + 2, y = 30,
                label = paste0(" ", round(Avg_Yield$Avg_Yield, 1))), color = "#949494", size = 4, hjust = 0) +
  geom_vline(aes(xintercept = Avg_Yield$Avg_Yield), color = "#949494", linetype = "dashed", lwd = 0.6, show.legend = F) +
  xlim(0, 2500) +
  scale_y_continuous(limits=c(0, 35), breaks=c(0,10,20,30,35)) +
  labs(title = "Current",
       x = "Yield (kg/ha)",
       y = "Frequency"
  ) +
  theme_minimal() +
  theme(plot.title = element_text(size = 14, hjust = 0.5),
        axis.title = element_text(size = 14),
        axis.text = element_text(size = 10),
        legend.title = element_text(size = 8),
        legend.text = element_text(size = 8),
        strip.text = element_blank()) +
  facet_wrap(~ Ecoregion, ncol=1)

hist_plot

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

  Pronto$Avg_Yield <- Pronto %>%
    group_by(Region) %>%
    mutate(Avg_Yield = mean(Yield, na.rm = TRUE))

  Pronto$Max_Yield <- Pronto %>%
    group_by(Region) %>%
    mutate(Max_Yield = max(Yield, na.rm = TRUE))

  Pronto <- Pronto %>%
    mutate(
      Region = as.numeric(Region))

  Pronto$Ecoregion <- cut(Pronto$Region, breaks = 7,
                          labels = c('Aspen Parkland','Cypress Upland',
                                     'Fescue Grassland','Lake Manitoba Plain','Mixed Grassland',
                                     'Moist Mixed Grassland','Southwest Manitoba Uplands'))

  Pronto$Avg_Yield$Avg_Yield <- as.numeric(as.character(Pronto$Avg_Yield$Avg_Yield))
  Pronto$Max_Yield$Max_Yield <- as.numeric(as.character(Pronto$Max_Yield$Max_Yield))
}

# ------ HISTROGRAM SSP1-2.6 ----------#

hist_plotA <- ggplot(Pronto, aes(x = Yield, color = Ecoregion)) +
  geom_histogram(binwidth = 0.5,  alpha = 0.7, show.legend = F) +
  scale_color_manual(values = c('#ec111a', '#fb6330', '#ffd42f', '#138468', '#009dd6', '#7849b8', '#f2609e')) +
  # Add text annotations for mean values
  geom_text(aes(x = Avg_Yield$Avg_Yield + 2, y = 30,
                label = paste0(" ", round(Avg_Yield$Avg_Yield, 1))), color = "#949494", size = 4, hjust = 0) +
  geom_vline(aes(xintercept = Avg_Yield$Avg_Yield), color = "#949494", linetype = "dashed", lwd = 0.6, show.legend = F) +
  xlim(0, 2500) +
  scale_y_continuous(limits=c(0, 35), breaks=c(0,10,20,30,35)) +
  labs(title = "SSP1-2.6",
       x = "Yield (kg/ha)",
       y = "Frequency"
  ) +
  theme_minimal() +
  theme(plot.title = element_text(size = 14, hjust = 0.5),
        axis.title = element_text(size = 14),
        axis.text = element_text(size = 10),
        legend.title = element_text(size = 8),
        legend.text = element_text(size = 8),
        strip.text = element_blank()) +
  facet_wrap(~ Ecoregion, ncol=1)

hist_plotA

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

  Pronto$Avg_Yield <- Pronto %>%
    group_by(Region) %>%
    mutate(Avg_Yield = mean(Yield, na.rm = TRUE))

  Pronto$Max_Yield <- Pronto %>%
    group_by(Region) %>%
    mutate(Max_Yield = max(Yield, na.rm = TRUE))

  Pronto <- Pronto %>%
    mutate(
      Region = as.numeric(Region))

  Pronto$Ecoregion <- cut(Pronto$Region, breaks = 7,
                          labels = c('Aspen Parkland','Cypress Upland',
                                     'Fescue Grassland','Lake Manitoba Plain','Mixed Grassland',
                                     'Moist Mixed Grassland','Southwest Manitoba Uplands'))

  Pronto$Avg_Yield$Avg_Yield <- as.numeric(as.character(Pronto$Avg_Yield$Avg_Yield))
  Pronto$Max_Yield$Max_Yield <- as.numeric(as.character(Pronto$Max_Yield$Max_Yield))
}

# ------ HISTROGRAM SSP2-4.5 ----------#

hist_plotB <- ggplot(Pronto, aes(x = Yield, color = Ecoregion)) +
  geom_histogram(binwidth = 0.5,  alpha = 0.7, show.legend = F) +
  scale_color_manual(values = c('#ec111a', '#fb6330', '#ffd42f', '#138468', '#009dd6', '#7849b8', '#f2609e')) +
  # Add text annotations for mean values
  geom_text(aes(x = Avg_Yield$Avg_Yield + 2, y = 30,
                label = paste0(" ", round(Avg_Yield$Avg_Yield, 1))), color = "#949494", size = 4, hjust = 0) +
  geom_vline(aes(xintercept = Avg_Yield$Avg_Yield), color = "#949494", linetype = "dashed", lwd = 0.6, show.legend = F) +
  xlim(0, 2500) +
  scale_y_continuous(limits=c(0, 35), breaks=c(0,10,20,30,35)) +
  labs(title = "SSP2-4.5",
       x = "Yield (kg/ha)",
       y = "Frequency"
  ) +
  theme_minimal() +
  theme(plot.title = element_text(size = 14, hjust = 0.5),
        axis.title = element_text(size = 14),
        axis.text = element_text(size = 10),
        legend.title = element_text(size = 8),
        legend.text = element_text(size = 8),
        strip.text = element_blank()) +
  facet_wrap(~ Ecoregion, ncol=1)

hist_plotB

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

  Pronto$Avg_Yield <- Pronto %>%
    group_by(Region) %>%
    mutate(Avg_Yield = mean(Yield, na.rm = TRUE))

  Pronto$Max_Yield <- Pronto %>%
    group_by(Region) %>%
    mutate(Max_Yield = max(Yield, na.rm = TRUE))

  Pronto <- Pronto %>%
    mutate(
      Region = as.numeric(Region))

  Pronto$Ecoregion <- cut(Pronto$Region, breaks = 7,
                          labels = c('Aspen Parkland','Cypress Upland',
                                     'Fescue Grassland','Lake Manitoba Plain','Mixed Grassland',
                                     'Moist Mixed Grassland','Southwest Manitoba Uplands'))

  Pronto$Avg_Yield$Avg_Yield <- as.numeric(as.character(Pronto$Avg_Yield$Avg_Yield))
  Pronto$Max_Yield$Max_Yield <- as.numeric(as.character(Pronto$Max_Yield$Max_Yield))
}

# ------ HISTROGRAM SSP3-7.0 ----------#

hist_plotC <- ggplot(Pronto, aes(x = Yield, color = Ecoregion)) +
  geom_histogram(binwidth = 0.5,  alpha = 0.7, show.legend = F) +
  scale_color_manual(values = c('#ec111a', '#fb6330', '#ffd42f', '#138468', '#009dd6', '#7849b8', '#f2609e')) +
  # Add text annotations for mean values
  geom_text(aes(x = Avg_Yield$Avg_Yield + 2, y = 30,
                label = paste0(" ", round(Avg_Yield$Avg_Yield, 1))), color = "#949494", size = 4, hjust = 0) +
  geom_vline(aes(xintercept = Avg_Yield$Avg_Yield), color = "#949494", linetype = "dashed", lwd = 0.6, show.legend = F) +
  xlim(0, 2500) +
  scale_y_continuous(limits=c(0, 35), breaks=c(0,10,20,30,35)) +
  labs(title = "SSP3-7.0",
       x = "Yield (kg/ha)",
       y = "Frequency"
  ) +
  theme_minimal() +
  theme(plot.title = element_text(size = 14, hjust = 0.5),
        axis.title = element_text(size = 14),
        axis.text = element_text(size = 10),
        legend.title = element_text(size = 8),
        legend.text = element_text(size = 8),
        strip.text = element_blank()) +
  facet_wrap(~ Ecoregion, ncol=1)

hist_plotC

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

Pronto$Avg_Yield <- Pronto %>%
  group_by(Region) %>%
  mutate(Avg_Yield = mean(Yield, na.rm = TRUE))

Pronto$Max_Yield <- Pronto %>%
  group_by(Region) %>%
  mutate(Max_Yield = max(Yield, na.rm = TRUE))

Pronto <- Pronto %>%
  mutate(
    Region = as.numeric(Region))

Pronto$Ecoregion <- cut(Pronto$Region, breaks = 7,
                        labels = c('Aspen Parkland','Cypress Upland',
                                    'Fescue Grassland','Lake Manitoba Plain','Mixed Grassland',
                                    'Moist Mixed Grassland','Southwest Manitoba Uplands'))

Pronto$Avg_Yield$Avg_Yield <- as.numeric(as.character(Pronto$Avg_Yield$Avg_Yield))
Pronto$Max_Yield$Max_Yield <- as.numeric(as.character(Pronto$Max_Yield$Max_Yield))
}

# ------ HISTROGRAM SSP5-8.5 ----------#

hist_plotD <- ggplot(Pronto, aes(x = Yield, color = Ecoregion)) +
  geom_histogram(binwidth = 0.5,  alpha = 0.7, show.legend = F) +
  scale_color_manual(values = c('#ec111a', '#fb6330', '#ffd42f', '#138468', '#009dd6', '#7849b8', '#f2609e')) +
  # Add text annotations for mean values
  geom_text(aes(x = Avg_Yield$Avg_Yield + 2, y = 30,
                label = paste0(" ", round(Avg_Yield$Avg_Yield, 1))), color = "#949494", size = 4, hjust = 0) +
  geom_vline(aes(xintercept = Avg_Yield$Avg_Yield), color = "#949494", linetype = "dashed", lwd = 0.6, show.legend = F) +
  xlim(0, 2500) +
  scale_y_continuous(limits=c(0, 35), breaks=c(0,10,20,30,35)) +
  labs(title = "SSP5-8.5",
       x = "Yield (kg/ha)",
       y = "Frequency"
  ) +
  theme_minimal() +
  theme(plot.title = element_text(size = 14, hjust = 0.5),
        axis.title = element_text(size = 14),
        axis.text = element_text(size = 10),
        legend.title = element_text(size = 8),
        legend.text = element_text(size = 8),
        strip.text = element_blank()) +
  facet_wrap(~ Ecoregion, ncol=1)

hist_plotD

combined_plothi <- grid.arrange(hist_plot, hist_plotA, hist_plotB,hist_plotC,hist_plotD, ncol = 5)
ggsave(".\\ALL_HistogramCURRENT.png", combined_plothi, width = 16.5, height = 12, dpi=400, bg = "white")
