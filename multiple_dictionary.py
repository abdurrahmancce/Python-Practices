country = {
    'finland': {
        'name': 'Finland',
        'population': 5_540_000,
        'capital': 'Helsinki',
        'coin': 'Euro',
        'continent': 'Europe',
        'economy': 'Mixed',
        'neighbors': ['Sweden', 'Norway', 'Russia'],
    },
    'japan': {
        'name': 'Japan',
        'population': 126_300_000,
        'capital': 'Tokyo',
        'coin': 'Yen',
        'continent': 'Asia',
        'economy': 'Developed', 
        'neighbors': ['Russia', 'South Korea', 'China'],
    },
    'norway': {
        'name': 'Norway',
        'population': 5_400_000,
        'capital': 'Oslo',
        'coin': 'Norwegian Krone',
        'continent': 'Europe',
        'economy': 'Developed',
        'neighbors': ['Sweden', 'Finland', 'Russia'],
    },
    'netherlands': {
        'name': 'Netherlands',
        'population': 17_000_000,
        'capital': 'Amsterdam',
        'coin': 'Euro',
        'continent': 'Europe',
        'economy': 'Developed',
        'neighbors': ['Germany', 'Belgium', 'Luxembourg'],                                                  
    },
    'sweden': {
        'name': 'Sweden',
        'population': 10_000_000,
        'capital': 'Stockholm',
        'coin': 'Swedish Krona',
        'continent': 'Europe',
        'economy': 'Developed',
        'neighbors': ['Norway', 'Finland'],
    },
    'scotland': {
        'name': 'Scotland',
        'population': 5_400_000,
        'capital': 'Edinburgh',
        'coin': 'Pound',
        'continent': 'Europe',
        'economy': 'Developed',
        'neighbors': ['England', 'Wales'],
    },
}
for country_name, country_info in country.items():
    print(f"\nCountry: {country_name.title()}")
    name = country_info['name']
    population = country_info['population']
    capital = country_info['capital']
    coin = country_info['coin']
    continent = country_info['continent']
    economy = country_info['economy']
    neighbors = country_info['neighbors']

    print(f"\tName: {name}")
    print(f"\tPopulation: {population}")
    print(f"\tCapital: {capital}")
    print(f"\tCurrency: {coin}")
    print(f"\tContinent: {continent}")
    print(f"\tEconomy: {economy}")
    print(f"\tNeighbors: {', '.join(neighbors)}")
    