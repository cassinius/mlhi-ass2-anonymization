import sys

out_dir = '../output/'


def outputCSV(clusters, outfile):
    out_string = "age, workclass, native-country, sex, race, marital-status\n"
    for cluster in clusters:
        out_string += cluster.toString()

    csvOutput = open(out_dir + outfile, 'w')
    csvOutput.write(out_string)