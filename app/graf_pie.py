import utils 
import read_csv
import chasrts

def run():
    data = read_csv.read_csv('./app/data.csv')
    data = list(filter(lambda item: item['Continent'] == 'South America', data))
    
    countries = list(map(lambda x: x['Country/Territory'], data))
    porcentages = list(map(lambda x: x['World Population Percentage'], data))
    chasrts.generate_pie_chart(countries, porcentages)
    
    country = input('pype country: ')
    
    result = utils.population_by_country(data,country)
    
    if len(result) >0:
        country = result[0]
        labels, values = utils.get_poulation(country)
        chasrts.generte_bar_chasrt(country['Country/Territory'], labels, values)
    
if __name__ == '__main__':
    run()
    
    