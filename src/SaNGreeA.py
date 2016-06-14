import input.csvInput as csv
import rangeGenHierarchy as RGH

adults_csv = '../data/input_sanitized.csv'
adj_list_csv = '../data/adult_graph_adj_list.csv'


def main():
    print "Starting SaNGreeA algorithm..."

    # Prepare input data structures
    adults = csv.readAdults(adults_csv)
    adj_list = csv.readAdjList(adj_list_csv)

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
