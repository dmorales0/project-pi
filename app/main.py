import utils
import chasrts
import read_csv


def run():
    data = read_csv.read_csv('./app/data.csv')
    country = input('ingresa el pais: ')
    
    result = utils.population_by_country(data, country)
    
    if len(result) >0:
        country = result[0]
        labels, values = utils.get_poulation(country)
        chasrts.generte_bar_chasrt(labels, values)


  
    
if __name__ == '__main__':
    run()
