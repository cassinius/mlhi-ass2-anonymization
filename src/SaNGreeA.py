import input.csvInput as csv
import catGenHierarchy as CGH
import rangeGenHierarchy as RGH

genh_dir = '../data/gen_hierarchies/'
adults_csv = '../data/input_sanitized.csv'
adj_list_csv = '../data/adult_graph_adj_list.csv'


def main():
    print "Starting SaNGreeA algorithm..."

    # Prepare input data structures
    adults = csv.readAdults(adults_csv)
    adj_list = csv.readAdjList(adj_list_csv)

    # Prepare categorical generalization hierarchies
    genh_workclass = CGH.CatGenHierarchy('workclass', genh_dir + 'WorkClassGH.json')
    genh_country = CGH.CatGenHierarchy('native-country', genh_dir + 'NativeCountryGH.json')
    genh_sex = CGH.CatGenHierarchy('sex', genh_dir + 'SexGH.json')
    genh_race = CGH.CatGenHierarchy('race', genh_dir + 'RaceGH.json')
    genh_marital = CGH.CatGenHierarchy('marital-status', genh_dir + 'MaritalStatusGH.json')


    # Prepare the age range generalization hierarchy
    min = float('inf')
    max = float('-inf')

    for idx in adults:
        idx_age = adults[idx].get('age')
        min = idx_age if idx_age < min else min
        max = idx_age if idx_age > max else max
    print "Found age range of: [" + str(min) + ":" + str(max) + "]"
    genh_age = RGH.RangeGenHierarchy('age', min, max)




if __name__ == '__main__':
    main()
