import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
covid_data = pd.read_csv('Hi.csv')
vaccination_data = pd.read_csv('HI2.csv')

# Get the lowest vaccinated countries
lowest_vaccinated = vaccination_data.sort_values(by='PERSONS_FULLY_VACCINATED', ascending=False).head(3)

# Get the lowest cases countries
lowest_cases = covid_data.sort_values(by='Cases - newly reported in last 7 days', ascending=False).head(3)

# Extract data for plotting
vaccinated_countries = lowest_vaccinated['COUNTRY'].values
vaccinated_persons = lowest_vaccinated['PERSONS_FULLY_VACCINATED'].values
cases_countries = lowest_cases['Name'].values
cases_numbers = lowest_cases['Cases - newly reported in last 7 days'].values

# Print the results for vaccinations
print('Lowest Three Countries by Fully Vaccinated Persons:')
for i in range(3):
    print(f"{i+1}) {vaccinated_countries[i]}: {vaccinated_persons[i]} fully vaccinated persons")

print('\nLowest Three Countries by Newly Reported Cases in Last 7 Days:')
for i in range(3):
    print(f"{i+1}) {cases_countries[i]}: {cases_numbers[i]} new cases")

# Chart for vaccination comparison
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
plt.bar(vaccinated_countries, vaccinated_persons, color=['blue', 'orange', 'green'])
plt.xlabel('Country')
plt.ylabel('Fully Vaccinated Persons')
plt.title('Lowest Three Countries by Fully Vaccinated Persons')

plt.subplot(1, 2, 2)
plt.bar(cases_countries, cases_numbers, color=['red', 'purple', 'yellow'])
plt.xlabel('Country')
plt.ylabel('Newly Reported Cases in Last 7 Days')
plt.title('Lowest Three Countries by Newly Reported Cases in Last 7 Days')

plt.tight_layout()
plt.show()
