print ("CP4.4.1")
year = int(input("How many years in life?: "))
days_year = 365
exhibit = 2.8*10**6
t_1exhib= 5 #wasted time for one exhibit in minutes
h_a_day = 8    #hours in a day
m_a_day = h_a_day*60 #minutes in a day
e_a_day = m_a_day/t_1exhib #exhibits a day
annual = days_year*e_a_day
by_1_person = annual*year #how many exhibits watched by one person for years

print ("m_a_day=",m_a_day)
print ("e_a_day=",e_a_day)
print ("annual=",annual)
print ("One person can see",by_1_person,"exhibits for",year,"years")



print ("CP4.4.2")
exhibits = int(input("Quantity of exhibits: "))
n_of_years = exhibits/annual #how many years to look through all exhibits^


print ("We spent",n_of_years,"years to see ",exhibits," exhibits")
