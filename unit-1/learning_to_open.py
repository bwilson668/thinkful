from __future__ import division

info = {}


def national_population_numbers(currentPopulation, futurePopulation, landArea):
    return {
        'population_2010': currentPopulation,
        'population_2100': futurePopulation,
        'land_area': landArea,
        'population_growth': futurePopulation - currentPopulation,
        'population_density': futurePopulation / landArea
    }

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv', 'rU') as inputFile:
    header = next(inputFile)

    for line in inputFile:
        line = line.rstrip().split(',')

        if line[1] == "Total National Population":
            pop2010 = int(line[5])
            pop2100 = int(line[6])
            landArea = int(line[7])

            info[line[0]] = national_population_numbers(
                pop2010,
                pop2100,
                landArea
            )

with open('national_population.csv', 'w') as outputFile:
    header = 'continent,'
    header += '2010_population,'
    header += '2100_population,'
    header += 'population_growth,'
    header += 'population_density'
    header += '\n'

    outputFile.write(header)

    worldPop = 0

    for k, v in info.iteritems():
        msg = k + ','
        msg += str(info[k]['population_2010']) + ','
        msg += str(info[k]['population_2100']) + ','
        msg += str(info[k]['land_area']) + ','
        msg += str(info[k]['population_growth']) + ','
        msg += str(info[k]['population_density'])
        msg += '\n'
        outputFile.write(msg)
        pass

    outputFile.write('World,' + str(worldPop) + '\n')
