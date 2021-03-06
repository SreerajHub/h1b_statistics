# h1b_statistics
Problem
A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its Office of Foreign Labor Certification Performance Data. But while there are ready-made reports for 2018 and 2017, the site doesn’t have them for past years.

As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate two metrics: Top 10 Occupations and Top 10 States for certified visa applications.

Your code should be modular and reusable for future. If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the input directory, running the run.sh script should produce the results in the output folder without needing to change the code.

Dataset:
UNITED STATES DEPARTMENT OF LABOR - Employment & Training Administration
https://www.foreignlaborcert.doleta.gov/performancedata.cfm

Code:
The task involves reading required data corresponding to respective headers from the csv file without using external libraries like pandas. The data is then sorted based on frequency of various categories. In case of equal frequencies, alphabetical order is followed. 
Detailed comments are provided in the sourcode. 

Results: 
The directories are structered as suggested.
For the example dataset provided, the results are matching the results in original directory.

TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
COMPUTER SYSTEMS ANALYSTS;107736;19.7%
SOFTWARE DEVELOPERS, APPLICATIONS;88806;16.2%
COMPUTER PROGRAMMERS;81032;14.8%
COMPUTER OCCUPATIONS, ALL OTHER;50277;9.2%
SOFTWARE DEVELOPERS, SYSTEMS SOFTWARE;15364;2.8%
MANAGEMENT ANALYSTS;12037;2.2%
ACCOUNTANTS AND AUDITORS;9841;1.8%
NETWORK AND COMPUTER SYSTEMS ADMINISTRATORS;9494;1.7%
FINANCIAL ANALYSTS;8194;1.5%
DATABASE ADMINISTRATORS;7506;1.4%

TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
CA;100710;18.4%
TX;55066;10.1%
NY;47703;8.7%
NJ;43463;7.9%
IL;29529;5.4%
GA;20663;3.8%
MA;20389;3.7%
PA;20146;3.7%
WA;19225;3.5%
FL;18296;3.3%


The execution results of testsuite are provided below. 
$ ./run_tests.sh
[PASS]: test_1
[PASS]: test_1 top_10_states.txt
[PASS]: test2
[PASS]: test2 top_10_states.txt
[Tue, Oct 30, 2018  6:34:21 AM] 2 of 2 tests passed



The results for the 2016 are as follows:

TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
SOFTWARE DEVELOPERS, APPLICATIONS;106758;18.7%
COMPUTER SYSTEMS ANALYSTS;88370;15.5%
COMPUTER PROGRAMMERS;72112;12.7%
COMPUTER OCCUPATIONS, ALL OTHER;48598;8.5%
SOFTWARE DEVELOPERS, SYSTEMS SOFTWARE;19337;3.4%
COMPUTER SYSTEMS ANALYST;16694;2.9%
MANAGEMENT ANALYSTS;13859;2.4%
ACCOUNTANTS AND AUDITORS;10187;1.8%
NETWORK AND COMPUTER SYSTEMS ADMINISTRATORS;9876;1.7%
MECHANICAL ENGINEERS;8315;1.5%


TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
CA;104070;18.3%
TX;59694;10.5%
NY;51293;9.0%
NJ;43174;7.6%
IL;31270;5.5%
GA;22229;3.9%
MA;21644;3.8%
PA;21141;3.7%
WA;20387;3.6%
FL;18684;3.3%

Year 2015:

TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
COMPUTER SYSTEMS ANALYSTS;107736;19.7%
SOFTWARE DEVELOPERS, APPLICATIONS;88806;16.2%
COMPUTER PROGRAMMERS;81032;14.8%
COMPUTER OCCUPATIONS, ALL OTHER;50277;9.2%
SOFTWARE DEVELOPERS, SYSTEMS SOFTWARE;15364;2.8%
MANAGEMENT ANALYSTS;12037;2.2%
ACCOUNTANTS AND AUDITORS;9841;1.8%
NETWORK AND COMPUTER SYSTEMS ADMINISTRATORS;9494;1.7%
FINANCIAL ANALYSTS;8194;1.5%
DATABASE ADMINISTRATORS;7506;1.4%

TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
CA;100710;18.4%
TX;55066;10.1%
NY;47703;8.7%
NJ;43463;7.9%
IL;29529;5.4%
GA;20663;3.8%
MA;20389;3.7%
PA;20146;3.7%
WA;19225;3.5%
FL;18296;3.3%

Year 2014:

TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
Computer Systems Analysts;85334;18.7%
Software Developers, Applications;68258;15.0%
Computer Programmers;64942;14.3%
Computer Occupations, All Other;36441;8.0%
Software Developers, Systems Software;13808;3.0%
Management Analysts;10547;2.3%
Accountants and Auditors;8512;1.9%
Financial Analysts;7784;1.7%
Network and Computer Systems Administrators;7300;1.6%
Mechanical Engineers;6553;1.4%


TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
CA;85164;18.7%
TX;45091;9.9%
NY;42169;9.3%
NJ;33243;7.3%
IL;24414;5.4%
PA;17167;3.8%
MA;17112;3.8%
GA;16080;3.5%
WA;15581;3.4%
FL;15563;3.4%

