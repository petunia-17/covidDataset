from bs4 import BeautifulSoup 
import  requests,openpyxl


excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = 'Covid Data'
print(excel.sheetnames)
sheet.append(['country name ', 'new covid  Cases','confirmed Cases','deaths Cumulative Total','new covid  Deaths','vaccine Total','Persons Fully Vaccinated per 100 Population'])
 
    

try:

  source = requests.get('https://covid19.who.int/table')
  source.raise_for_status()

  soup=BeautifulSoup(source.text,'html.parser')
  

  covidData = soup.find('div',class_='tbody').find_all('div')

 


  for cData in covidData:
      
   
          countryName = cData.find('div',class_='sc-AxjAm sc-qXRQq bJEXVx').span.text

          newCases =cData.find('div',class_='sc-AxjAm sc-fzocqA jwZhay').get_text()

          confirmedCases=cData.find('div',class_='column_Last_7_Days_Confirmed td').get_text()

          deathsCumulativeTotal=cData.find('div',class_='column_Cumulative_Deaths td')

          newDeaths=cData.find('div',class_='column_Last_7_Days_Deaths td')

          vaccineTotal =cData.find('div',class_='column_Total_Vaccinations_Per_100 td')

          PersonsFullyVaccinatedper100Population =cData.find('div',class_='column_Total_Fully_Vacc_Per_100 td')


          print(countryName ,newCases , confirmedCases , deathsCumulativeTotal , newDeaths ,vaccineTotal , PersonsFullyVaccinatedper100Population)
          sheet.append(['countryName','newCases','confirmedCases','deathsCumulativeTotal','newDeaths','vaccineTotal','PersonsFullyVaccinatedper100Population'])



         
except Exception as e:

    print(e)

excel.save('covidData.xlsv')
