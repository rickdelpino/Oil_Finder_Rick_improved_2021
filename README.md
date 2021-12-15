# Oil_Finder_Rick_improved_2021
Open source Windows Application in Python for Geosciences, Artificial Intelligence and Data Sciences - Starting Framework 2021

Hello World!
I am Edgar Del Pino, an exploration and production geophysicist/geoscientist which have a lot of projects in mind related with
geology, geophysics, programming, AI and Data Sciences.

This is my first attempt to create a software platform where I can implement Machine Learning, AI and data Sciences to a variety
of problems that I have faced during my different jobs and assignations inside the oil industry, in different settings and departments, 
where the lack of time and resources led me to choose a practical solution, but, I always kept some doubts about what kind of output 
could be obtained if we would had apply a more scientific approach using Machine Learning...

The software is incomplete because this is only the design stage of the User Interface and early implemmentations of segy reading, 
plotting and dataframes implementation. There are a lot of fixes to do, rewrite, recoding, debugging and obviously, changes
to be made. This is because for me, the most important thing in an app or analysis software, is the UI. The most popular
geological interpretation software has a very intuitive and straightforward UI, however the closest competitor's software 
has a very serious UI problem: it is not intuitive. So I chose the most user friendly framework construction software: PyQT5.
That is why the following are the first focus of this early software version: the fundations construction and data reading, 
the purposes of each module, the plotting of the data and the framework design. This is only the begining... 


Let's start with the project!:

- Programming language: Python 3.8 - because it has a lot of documentation and a very active community.
- Windows IDE (Integrated Development Environment):  Visual Studio Code. It works very well. In Linux, Spyder was my choice.
- Framework: PyQT5 - For me, it has the best QT designer, and it's extremely easy to use (on Windows).
- SEGY library: SEGYIO - a very interesting option for reading and manipulation of SEGY files, but I am strugling with its 
                coordinates management or vectorized applications. It has pros and cons.
- Python libraries:
        * numpy: for a very easy array manipulation and best performance.
        * pandas: for Data Science forms or massive ascii and number manipulation. These are the famous Dataframes.
        * matplotlib: a library to plot almost everything with python. I am struggling with its PyQT5 integration.
        * xarray: segyoi has a better integration with it and has matplotlib plotting routines.
        * csv: for readign CSV  files.


What the software do so far:
1) Can load a no-referenced 2D seismic lines and plot them in the Seismic 2D View Tab.
2) Can load a 3D Seismic an plot a line in the Seismic 3D View Tab.
3) Can load sigle trace seismic in the single trace VSP Tab.
4) Can load and display the content of a Dataframe in form of Bar charts and Pie charts, in the Data Science Tab.
5) Most of the loading will be done in the Import Button and the Data Sience Button.


Inside the Data folder, there is a csv file "Exploratory_Wells_Data.csv" that is used in the Data Sciences module for
testing purposes.
