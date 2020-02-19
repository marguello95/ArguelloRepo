import csv

#Setting intial variables which will be used in more than one of the steps
years = []
months = []
count = []


#Finding Min, Max and avg for overall dataset
#Gives initial comand for reading in the csv file into python code fort this step
with open("co2-ppm-daily.csv") as CO:
    csv_reader = csv.reader(CO, delimiter=',')

    Tot_line_count = 0
    headerline = CO.next() #Ignores the line with titles of each row (Date and Value) so only data values accounted for

#Create open list for year and month as well as a count list

    for row in csv_reader:
        # splits dates from xxxx-xx-xx format into individual days, months and years, split at dash "-" like it is in origionl data
        year, month, day = row[0].split("-")

        #Creates a list for years
        if year not in years:
             years.append(year)


        #Adds data to create month list
        if month not in months:
            months.append(month)

        #Will count haw many lines of data a present within the entire data set
        count.append(float(row[1]))
        Tot_line_count = Tot_line_count + 1

#The following will print out the minimium, maximum and average of the entire dataset
print "Min: " + str(min(count))
print "Max: " + str(max(count))
print "Avg: " + str(sum(count) / len(count))




#This step uses the years list created in the previous step
#Finding Average values for each year of dataset:
year_avg = {}

#Gives initial comand for reading in the csv file into python code for this step
for year in years:
    temp_year_avg = []
    with open("co2-ppm-daily.csv") as CO:
        csv_reader = csv.reader(CO, delimiter=',')
        headerline = CO.next() #Ignores the line with titles of each row (Date and Value) so only data values accounted for

        for row in csv_reader:
            year_av, month_av, day = row[0].split("-")  # splits dates from xxxx-xx-xx format into individual days, months and years, split at dash "-" like it is in origionl data
            if year_av == year:
                temp_year_avg.append(float(row[1]))  #Creates a list for each year in dataset

    #Calculates the average for individual year
    year_avg[year] = str(sum(temp_year_avg) / len(temp_year_avg))

#Print the year and average value for that year
print year_avg


##Average by each season

#create an open list for each season:
winter = []
spring = []
summer = []
fall = []

#Gives initial comand for reading in the csv file into python code fort this step
with open("co2-ppm-daily.csv") as CO:
    csv_reader = csv.reader(CO, delimiter=',')
    headerline = CO.next()

    for row in csv_reader:
        year_av, month_av, day = row[0].split("-")  # splits dates from xxxx-xx-xx format into individual days, months and years, split at dash "-" like it is in origionl data

       #Creates a list for winter dates based on month (in number format = 12,1,2 = dec,jan,feb)
        if month_av == '12' or month_av == '01' or month_av == '02':
            winter.append(float(row[1]))
        # Creates a list for spring dates based on month (in number format = 3,4,5 = march, apr, may)
        if month_av == '03' or month_av == '04' or month_av == '05':
            spring.append(float(row[1]))
        # Creates a list for summer dates based on month (in number format = 6,7,8 = june, july, aug)
        if month_av == '06' or month_av == '07' or month_av == '08':
            summer.append(float(row[1]))
        #Creates a list for fall dates based on month (in number format = 9,10,11 = sep,oct,nov)
        if month_av == '09' or month_av == '10' or month_av == '11':
            fall.append(float(row[1]))

#prints list created above for all 4 seasons
print "Winter = " + str(sum(winter) / len(winter))
print "Spring = " + str(sum(spring) / len(spring))
print "Summer = " + str(sum(summer) / len(summer))
print "Fall = " + str(sum(fall) / len(fall))



# #Finding the annomaly for each point
#Gives initial comand for reading in the csv file into python code fort this step
with open("co2-ppm-daily.csv") as CO:
    csv_reader = csv.reader(CO, delimiter=',')
    headerline = CO.next()

    for row in csv_reader:
        anom = int(float(row[1])) - int(float(354.85)) #Subtracts average from the data for each data
        print str(row[0]) + ": Annomaly for date = " + str(anom) #Prints the data of each year and the annomaly of each point
