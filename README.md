# Data Visualization & Statistics in the Geosciences 2019
UPDATE: The 2019 and 2018 versions of this class are hosted both on this Github user profile, as well as on github.com/astro-abby. 

This repository contains the laboratory portion of a split upper level undergraduate / graduate class in Python on data visualization and statistics for geo &amp; space scientists. Labs will be updated from January - May at the same cadence as the course (2019). The 2018 version may be found in the 2018 branch.

The labs uploaded will be in Jupyter primarily and coded in Python 3.5+. However, most of the functions and methods should work in Python 2.7. If you do not have/know what Jupyter is - you can download Python/Jupyter from Anaconda or Canopy as a fully installed and interactive environment. This will support most if not all of the packages used in the labs and then you can navigate to Jupyter through Anaconda/Canopy.

Make sure you check out the [Frequently Asked Questions](https://github.com/astro-abby/data_vis_statistics_geosciences/blob/2019/FAQ/FAQ.md) section as you go through the labs. 

Please see our liscense at the end of this readme. This class has been developed in collaboration between [Dr. Michael Liemohn](http://clasp.engin.umich.edu/people/liemohn) of the Climate & Space Sciences & Engineering department and [Abby Azari](https://astro-abby.github.io/). The 2019 version updated with the assistance of [Brian Swiger](https://github.com/briswi). 

If you find it useful and end up using in your work please cite this as: 
- Azari, A. R., Liemohn, M. W., & Swiger, B. M. "Data Visualization and Statistics in the Geosciences". Accessed on *insert date*. github.com/astro-abby/data_vis_statistics_geosciences. 2019.



# Current Content

### [Frequently Asked Questions](https://github.com/astro-abby/data_vis_statistics_geosciences/blob/2019/FAQ/FAQ.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Grouping of frequently asked questions on programming, visualization, and statistics.

### [Lab 1 - Intro to Python - What IS Pandas? (1/13/2019)](https://github.com/astro-abby/data_vis_statistics_geosciences/blob/2019/Lab1/Lab1_ClimaticAverages_GlobalTemperatures.ipynb)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Temperature Changes: Looking at Global Temperature Variances in the Last Century 

### [Lab 2 - Multi-plots and Datetime Objects (1/21/2019)](https://github.com/astro-abby/data_vis_statistics_geosciences/blob/2019/Lab2/Lab2_BirdRanges.ipynb)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Ecosystem Impacts: Looking at Audubon Society Data on Bird Wintering Patterns

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Note: http://climate.audubon.org/article/audubon-report-glance#FAQ-4. Update for 2020  planned.

### [Lab 3 - Image Manipulation and Spacecraft Data (1/28/2019)](https://github.com/astro-abby/data_vis_statistics_geosciences/blob/2019/Lab3/Lab3_JupiterFlyBy.ipynb)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Jupiter Images with Jupyter: Looking at Spacecraft Image Data from the Recent Juno Mission  

### [EXTRA Course Lecture - From Chart to Art (2/3/2019)](https://github.com/astro-abby/data_vis_statistics_geosciences/blob/2019/VisualizationBasics/CLaSP405_W19_4Visualization.pdf)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Lecture for course on visualization basics.

### [Lab 4 - Data Merging and Indexing with Spacecraft Data (2/5/2019)](https://github.com/astro-abby/data_vis_statistics_geosciences/blob/2019/Lab4/Lab4_JupiterFlyBy.ipynb)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Jupiter Data with Jupyter: Looking at Magnetic Field Data from the Recent Juno Mission

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Note: For the error analysis section there are equations written in LaTeX.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; They might not show up with Github's preview - if you want to view these please download the Jupyter notebook.  

### [Lab 5 - Groupby, Normal Distributions, & Boxplots (2/12/2019)](https://github.com/astro-abby/data_vis_statistics_geosciences/blob/2019/Lab5/Lab5_NormalsTempsHealthImpacts.ipynb)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Health Impacts: Normal Distributions of Temperature and Boxplots of Extremes

### [Lab 6 - Linear Regression & Geo-Mapping with Sea Ice (2/19/2019)](https://github.com/astro-abby/data_vis_statistics_geosciences/blob/2019/Lab6/Lab6_MappingSeaIce.ipynb)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Arctic Indicators: Calculating Rates of Change of Sea Ice Extent & Mapping

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Note: The netCDF file required for analysis must be downloaded seperately. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; You can find the gridded ice concentration data from the [National Snow & Ice Data Center](http://nsidc.org/data/G10010).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Additionally this lab is dependent on the Python packages for [netCDF-4](http://unidata.github.io/netcdf4-python/) and [Basemap](https://matplotlib.org/basemap/).

### [Lab 7 - Correlation Coefficients, Classification Problems, & Space Weather (3/12/2019)](https://github.com/astro-abby/data_vis_statistics_geosciences/blob/2019/Lab7/Lab7_SpaceWeatherClassifiers.ipynb)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Space Weather: Solar Impacts on Geomagnetic Storms

### [Lab 8 - Object Oriented Programming and Bootstrap Analysis (3/19/2019)](https://github.com/astro-abby/data_vis_statistics_geosciences/blob/2019/Lab8/Lab8_SpaceWeatherBootstraps.ipynb)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Space Weather: Linear Regression with Bootstrap Analysis

### [EXTRA Data Visualization Basics (5/16/2018)](https://github.com/astro-abby/data_vis_statistics_geosciences/blob/master/VisualizationBasics/Visualization_Basics.pdf)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Mini lessons and lectures for the [2018 ICOS Big Data Summer Camp](https://github.com/ICOSBigDataCamp/2018-summer-camp) at University of Michigan

| | |
|:-------------------------:|:-------------------------:|
|Lab 1 <img width="1500" alt="img1" src="./Lab1/Figures/Example_TempVariants_GlobalYearlyAverages_Transparent.png"> | Lab 2 <img width="1500" alt="img2" src="./Lab2/Figures/LatitudeBirds_NorthAmerica_TempAnomalies.png"> 
|Lab 3 <img width="1500" alt="img3" src="./Lab3/FinalPNGs/augmentedProject.png"> | Lab 4 <img width="1500" alt="img4" src="./Lab4/Figures/JunoCam_MagData_2017-086-08-20.png" alt="Drawing4"> 
|Lab 5 <img width="1500" alt="img5" src="./Lab5/Figures/SummerTemps.png"> | Lab 6 <img width="1500" alt="img5" src="./Lab6/Figures/2010SeaIceConcentration.png"> 
|Lab 7 <img width="1500" alt="img7" src="./Lab7/Figures/LongDurationSolar.png"> |Lab 8 <img width="1500" alt="img8" src="./Lab8/Figures/BootstrapLinearFits.png">



This README will be updated to reflect current changes. Data used in the lessons will be accredited to the providers. Lab assignments are availiable and will be mentioned in the tutorials but are not linked. 

Discussions with climate scientist [Samantha Basile](http://clasp.engin.umich.edu/people/sjbasile/GSTUDENT) were critical in developing these materials. We also thank planetary scientist [Camilla Harris](https://github.com/cdkharris) for discussions of Juno data, Gabriel Harp the Research Director of ArtsEngin at University of Michigan for pointing us toward climate health impact data, space scientist [Doga Ozturk](http://orcid.org/0000-0002-8071-2707) for expertise in space weather informatics, solar physicist [Yeimy Rivera](http://clasp.engin.umich.edu/people/yrivera/GSTUDENT) for expertise in solar surface data, and Jeff Lockhart of the [Computational Social Scientists](https://github.com/UM-CSS) (CSS) for offering resources through CSS.

Last update 12/4/2019

# License
The content and lessons of this repository itself is licensed under the [Creative Commons Attribution-Non Commercial 4.0 license](https://creativecommons.org/licenses/by-nc/4.0/). However, the specific code used within the notebooks taken out of context and to format and display that content is licensed under the [MIT license](https://choosealicense.com/licenses/mit/).
