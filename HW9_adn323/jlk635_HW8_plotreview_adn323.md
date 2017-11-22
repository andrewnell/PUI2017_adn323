# Review of jlk635 HW8 plot
# adn323

I believe the Chernoff faces are a very interesting and novel way of communicating multi-dimensional data that is often very tricky to convey visually. As a means of conveying all these characteristics it is an effective and clear way of conveying the information. However I do think that trying to convey this much information is difficult and it is hard as a reader to understand all the dimensions without getting confused. Ideally one has a clearer message that they want to convey and does not need to use something as complex as this. 

Aesthetically, the visualisation provides an easy way for a user to compare the differences between two countries by comparing features of the faces, however, I think that it becomes difficult to understand differences between countries that are not that different or if there are outliers that skew the changes between two countries. There are some features that can become difficult to view, for instance South Africa’s mouth width (Number of Researchers) is so narrow that it becomes difficult to see things like whether there is a smile (unemployement). If possible these should be identified and resolved where possible. The legend attached is clear and concise and provides an easy way to reference what features mean in the chart, however the one feature I did not understand was the colouring of the faces which is not referenced anywhere.

I believe the chart is honest and is reproducing the data.

Overall it is an interesting visualisation, however in practice I would avoid using it due to complexity.

See visualisation and description below.

# The Chernoff faces of CUSP 2017/18

Jon chose to plot avisualisation using the **Chernoff faces**

He compiled a series of aggregate country level statistics for each of the countries represented by CUSP students in the 2017/18 class - along with a few additional misc. countries for comparison purposes. The statistics were mainly urban in nature, relating to the overall economy, mobility, health, education, technology, industry and law and order. A summary of the data is provided in the data section later. The R code is also [provided](https://raw.githubusercontent.com/jkastelan/PUI2017_jlk635/master/HW8_jlk635/HW8_jlk635_Code_for_Chernoff_faces_in_R.txt) in the repo for reference.


## Visualisation
<kbd>![alt text](https://github.com/andrewnell/PUI2017_jlk635/raw/master/HW8_jlk635/HW8_jlk635_Chernoff_faces_in_R.png)</kbd>


#### Legend
The variables represented by characteristics of the Chernoff faces are as follows:


|**Variable No.** |**Chernoff face representation** |**Indicator Name** |
|:----------:|:----------|:------------|
1 |Height of face   |CO2 emissions (kt), total |
2 |Width of face   |Death rate, crude (per 1,000 people) |
3 |Structure of face |GDP per capita, PPP (constant 2011 international $) |
4 |Height of mouth  |New businesses registered (number) |
5 |Width of mouth   |Researchers in R&D (per million people) |
6 |Smiling     |Unemployment, total (% of total labor force) (national estimate) |
7 |Height of eyes    |Refugee population by country or territory of asylum (number) |
8 |Width of eyes    |Mobile cellular subscriptions (per 100 people) |
9 |Height of hair   |Individuals using the Internet (% of population) |
10 |Width of hair  |Population, total |
11 |Style of hair   |Scientific and technical journal articles, total |
12 |Height of nose   |Armed forces personnel, total |
13 |Width of nose  |Rail lines (total route-km) |
14 |Width of ear   |Fertility rate, total (births per woman) |
15 |Height of ear   |Intentional homicides (per 100,000 people) |
16 |[not fitted] |Poverty headcount ratio at $1.90 a day (2011 PPP) (% of population) |
17 |[not fitted] |Adolescents out of school (% of lower secondary school age) |
18 |[not fitted] |Air transport, passengers carried |
|||
