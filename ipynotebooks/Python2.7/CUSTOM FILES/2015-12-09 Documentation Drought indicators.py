
# coding: utf-8

# #### **Vegetation Condition Index**
# **Introduction**
# 
# The Vegetation Condition Index (VCI) compares the current NDVI to the range of values observed in the same period in previous years. The VCI is expressed in between 0 and 1 and gives an idea where the observed value is situated between the extreme values (minimum and maximum) in the previous years. Lower and higher values indicate bad and good vegetation state conditions, respectively.
# 
# The VCI is computed as follow:
# 
# $$
# VCI_{ijk} = \frac{NDVI_{ijk} - \max{NDVI}_{ij}}{\max{NDVI}_{ij} - \min{NDVI}_{ij}} 
# $$
# 
# Where $VCI_{ijk}$ is the VCI-value for pixel $i$ during day $j$ for year $k$. $NDVI_{ijk}$ is the daily $NDVI$ value for pixel $i$ during day $j$ for year $k$, $\max{NDVI}_{ij}$ is the maximum $NDVI$ for pixel $i$ during day $j$ over $n$ years, and $\min{NDVI}_{ij}$ is the minumum $NDVI$ for pixel $i$ during day $j$ over $n$ years.
# 
# **References**
# 
# Kogan, F. N. "Application of vegetation index and brightness temperature for drought detection." Advances in Space Research 15.11 (1995): 91-100. [doi: 10.1016/0273-1177(95)00079-T](http://dx.doi.org/10.1016/0273-1177%2895%2900079-T)

# #### **Temperature Condition Index**
# **Introduction**
# 
# The Temperature Condition Index (TCI) compares the current land surface temperature (LST) to the range of values observed in the same period in previous years. The LST is expressed in between 0 and 1 and gives an idea where the observed value is situated between the extreme values (minimum and maximum) in the previous years. Higher values indicate increased temperature condititon and lower values indicate decreased temperature condition. This index was used to determine temperature-related vegetation stress and also stress caused by an excessive wetness
# 
# The TCI is computed as follow:
# 
# $$
# TCI_{ijk} = \frac{\max{LST}_{ij} - LST_{ijk}}{\max{LST}_{ij} - \min{LST}_{ij}} 
# $$
# 
# Where $TCI_{ijk}$ is the TCI-value for pixel $i$ during day $j$ for year $k$. $LST_{ijk}$ is the daily $LST$ value for pixel $i$ during day $j$ for year $k$, $\max{LST}_{ij}$ is the maximum $LST$ for pixel $i$ during day $j$ over $n$ years, and $\min{LST}_{ij}$ is the minumum $LST$ for pixel $i$ during day $j$ over $n$ years.
# 
# **References**
# 
# Kogan, F. N. "Application of vegetation index and brightness temperature for drought detection." Advances in Space Research 15.11 (1995): 91-100. [doi: 10.1016/0273-1177(95)00079-T](http://dx.doi.org/10.1016/0273-1177%2895%2900079-T)

# #### **Vegetation Health Index**
# 
# **Introduction**
# 
# The Vegetation Health Index, also called the Vegetation-Temperature Index, is based on a combination of Vegetation Condition Index (VCI) and Temperature Condition Index (TCI). It is effective enough to be used as proxy data for monitoring vegetation health, drought, moisture, thermal condition, etc.
# 
# The VHI is computed as follow:
# 
# $$
# VHI_{ijk} = \alpha\cdot VCI_{ijk} + (1-\alpha)\cdot TCI_{ijk}
# $$
# 
# Where $VHI_{ijk}$ is the VHI-value for pixel $i$ during day $j$ for year $k$. $VCI_{ijk}$ is the VCI-value for pixel $i$ during day $j$ for year $k$, $TCI_{ijk}$ is the TCI-value for pixel $i$ during day $j$ for year $k$ and $\alpha$ is used to change the importance of each separated condition index and should have a value between $0$ and $1$ and is normally set to $0.5$.
# 
# **References**
# 
# Kogan, Felix N. "Global drought watch from space." Bulletin of the American Meteorological Society 78.4 (1997): 621-636. [doi: 10.1175/1520-0477(1997)078<0621:GDWFS>2.0.CO;2](http://dx.doi.org/10.1175/1520-0477%281997%29078%3C0621%3AGDWFS%3E2.0.CO%3B2)

# #### **Normalized Vegetation Anomaly Index**
# 
# **Introduction**
# 
# The Normalized Vegetation Anomaly Index (NVAI) compares the current NDVI to the range of values observed in the same period in previous years. The NVAI is expressed in between -1 and 1 and provide an anomaly indicator relative to its long term mean. Lower and higher values indicate bad and good vegetation state conditions, respectively.
# 
# The NVAI is computed as follow:
# 
# $$
# NVAI_{ijk} = \frac{NDVI_{ijk} - \overline{NDVI_{ij}}}{\max{NDVI}_{ij} - \min{NDVI}_{ij}} 
# $$
# 
# Where $NVAI_{ijk}$ is the NVAI-value for pixel $i$ during day $j$ for year $k$. $NDVI_{ijk}$ is the daily $NDVI$ value for pixel $i$ during day $j$ for year $k$, $\overline{NDVI_{ij}}$ is the long term mean of $NDVI$ for pixel $i$ during day $j$ over $n$ years. $\max{NDVI}_{ij}$ is the maximum $NDVI$ for pixel $i$ during day $j$ over $n$ years and $\min{NDVI}_{ij}$ is the minumum $NDVI$ for pixel $i$ during day $j$ over $n$ years.
# 
# **References**
# 
# Jia, Li, et al. "Assessing the sensitivity of two new indicators of vegetation response to water availability for drought monitoring." SPIE Asia-Pacific Remote Sensing. International Society for Optics and Photonics, 2012. [doi: 10.1117/12.977416](http://dx.doi.org/10.1117/12.977416)

# #### **Normalized Temperature Anomaly Index**
# 
# **Introduction**
# 
# The Normalized Temperature Anomaly Index (NTAI) compares the current land surface temperature (LST) to the range of values observed in the same period in previous years. The NTAI is expressed in between -1 and 1 and provide an anomaly indicator relative to its long term mean. Lower and higher values indicate good and bad temperature related vegetation conditions, respectively.
# 
# The NTAI is computed as follow:
# 
# $$
# NTAI_{ijk} = \frac{LST_{ijk} - \overline{LST_{ij}}}{\max{LST}_{ij} - \min{LST}_{ij}} 
# $$
# 
# Where $NTAI_{ijk}$ is the LST-value for pixel $i$ during day $j$ for year $k$. $LST_{ijk}$ is the daily $LST$ value for pixel $i$ during day $j$ for year $k$, $\overline{LST_{ij}}$ is the long term mean of $LST$ for pixel $i$ during day $j$ over $n$ years. $\max{LST}_{ij}$ is the maximum $LST$ for pixel $i$ during day $j$ over $n$ years and $\min{LST}_{ij}$ is the minumum $LST$ for pixel $i$ during day $j$ over $n$ years.
# 
# **References**
# 
# Jia, Li, et al. "Assessing the sensitivity of two new indicators of vegetation response to water availability for drought monitoring." SPIE Asia-Pacific Remote Sensing. International Society for Optics and Photonics, 2012. [doi: 10.1117/12.977416](http://dx.doi.org/10.1117/12.977416)

# #### **Normalized Drought Anomaly Index**
# 
# **Introduction**
# 
# The Normalized Drought Anomaly Index is a combined index by integrating the Normalized Vegetation Anomaly Index (NVAI) and the Normalized Temperature Anomaly Index (NTAI). This integrated index can remove the impact of flooding on NVAI, thus being more effective for detecting vegatation damage from drought.
# 
# The NDAI is computed as follow:
# 
# $$
# NDAI_{ijk} = \alpha\cdot NVAI_{ijk} - (1-\alpha)\cdot NTAI_{ijk}
# $$
# 
# Where $NDAI_{ijk}$ is the NDAI-value for pixel $i$ during day $j$ for year $k$. $NVAI_{ijk}$ is the NVAI-value for pixel $i$ during day $j$ for year $k$, $NTAI_{ijk}$ is the NTAI-value for pixel $i$ during day $j$ for year $k$ and $\alpha$ is used to set the importance of each separated condition index and should have a value between $0$ and $1$ and is normally set to $0.5$.

# #### **Precipitation Anomaly Percentage**
# 
# **Introduction**
# 
# Precipitation Anomaly Percentage (PAP) is a traditional drought monitoring indicator which
# presents anomaly in precipitation as a percentage of the long-term average or normal. PAP can
# intuitively indicate the anomaly of precipitation and being used to evaluate drought events in
# meteorology. For drought monitoring, accumulative precipitation and its deficit over a certain period
# (e.g. weekly or monthly) is more meaningful than daily values.
# 
# The PAP is computed as follow:
# 
# $$
# PAP^{m}_{ijk} = \frac{P^{m}_{ijk}-\overline{P^{m}_{ijk}}}{\overline{P^{m}_{ijk}}}\cdot 100\%
# $$
# 
# Where $PAP^{m}_{ijk}$ is the moving Accumulative Precitation Anomaly Percentage with moving window period $m$ for pixel $i$ with $j$ as first day of each moving window period for year $k$ . $P^{m}_{ijk}$ is the cumulative precipitation over the period $m$ for pixel $i$ with $j$ as the first day the moving window period for year $k$ and $\overline{P^{m}_{ij}}$ is the long-term mean of accumulative precipitation with window period $m$ for pixel $i$ with $j$ as the first day of the moving window period and calculated as:
# 
# $$
# \overline{P^{m}_{ijk}} = \frac{\sum_1^n{P^{m}_{ij}}}{n}
# $$
# 
# Where $n$ is the total number of years
# 
# **References**
# 
# Jia, Li, et al. "Assessing the sensitivity of two new indicators of vegetation response to water availability for drought monitoring." SPIE Asia-Pacific Remote Sensing. International Society for Optics and Photonics, 2012. [doi: 10.1117/12.977416](http://dx.doi.org/10.1117/12.977416)

# In[ ]:



