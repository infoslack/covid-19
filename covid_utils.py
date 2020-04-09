def last_date(data):
    """
    Agrupa os dados por país e filtra pela última data
    """
    return data.groupby("Country/Region").sum().iloc[:, -1]

def rename_location(location):
    """
    Renomeia alguns países do dataset da UN para o Johns Hopkins CSSE
    """
    if location == 'China':
        return 'Mainland China'
    if location == 'Republic of Korea':
        return 'South Korea'
    if location == 'Iran (Islamic Republic of)':
        return 'Iran'
    if location == 'China, Hong Kong SAR':
        return 'Hong Kong'
    if location == 'United States of America':
        return 'US'
    return location
