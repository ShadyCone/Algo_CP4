print ("CP4.4")
year = 80
days_year = 365
exhibit = 2.8*10**6
t_1exhib= 5
h_a_day = 8    #hours a day
m_a_day = h_a_day*60 #min a day
e_a_day = m_a_day/t_1exhib #exhibits a day
annual = days_year*e_a_day
by_1_person = annual*year #how many exhibits watched by one person 
exhibits = 1000000
n_of_years = exhibits/annual


print ("m_a_day=",m_a_day)
print ("e_a_day=",e_a_day)
print ("annual=",annual)
print ("by_1_person=",by_1_person)
print ("exhibits=",exhibits)
print ("annual=", annual)
