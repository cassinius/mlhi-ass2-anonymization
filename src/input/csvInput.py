import csv

adult_file_name = '../../data/input_sanitized.csv'
adj_list_file_name = '../../data/adult_graph_adj_list.csv'


def readAdults():
    adult_file = open(adult_file_name, 'r')
    adults_csv = csv.reader(adult_file, delimiter=',')

    # ignore the headers
    next(adults_csv, None)

    # create the dict we need
    adults = {}

    for adult_idx in adults_csv:
        adult = adults[int(adult_idx[0])] = {}
        adult['age'] = int(adult_idx[1])
        adult['workclass'] = adult_idx[2]
        adult['native-country'] = adult_idx[3]
        adult['sex'] = adult_idx[4]
        adult['race'] = adult_idx[5]
        adult['marital-status'] = adult_idx[6]

    adult_file.close()
    return adults


def readAdjList():
    adj_list_file = open(adj_list_file_name, 'r')
    adj_list_csv = csv.reader(adj_list_file, delimiter=',')

    # create the dict we need
    adj_list = {}

    for adj_idx in adj_list_csv:
        node = adj_list[int(adj_idx[0])] = adj_idx[1:len(adj_idx)-1]

    adj_list_file.close()
    return adj_list


if __name__ == "__main__":
    print readAdults()
    print readAdjList()
