import io.csvInput as csv
import io.output as out
import catGenHierarchy as CGH
import rangeGenHierarchy as RGH
import nodeCluster as CL
import globals as GLOB

adults_csv = '../data/input_sanitized.csv'
adj_list_csv = '../data/adult_graph_adj_list.csv'
genh_dir = '../data/gen_hierarchies/'


def prepareGenHierarchiesObject(dataset):
    # Prepare categorical generalization hierarchies
    genh_workclass = CGH.CatGenHierarchy('workclass', genh_dir + 'WorkClassGH.json')
    genh_country = CGH.CatGenHierarchy('native-country', genh_dir + 'NativeCountryGH.json')
    genh_sex = CGH.CatGenHierarchy('sex', genh_dir + 'SexGH.json')
    genh_race = CGH.CatGenHierarchy('race', genh_dir + 'RaceGH.json')
    genh_marital = CGH.CatGenHierarchy('marital-status', genh_dir + 'MaritalStatusGH.json')

    # Prepare the age range generalization hierarchy
    min = float('inf')
    max = float('-inf')

    # We have to set the age range before instantiating it's gen hierarchy
    for idx in dataset:
        idx_age = dataset[idx].get('age')
        min = idx_age if idx_age < min else min
        max = idx_age if idx_age > max else max
    print "Found age range of: [" + str(min) + ":" + str(max) + "]"
    genh_age = RGH.RangeGenHierarchy('age', min, max)

    # Let's create one central object holding all required gen hierarchies
    # to pass around to node clusters during computation
    gen_hierarchies = {
        'categorical': {
            'workclass': genh_workclass,
            'native-country': genh_country,
            'sex': genh_sex,
            'race': genh_race,
            'marital-status': genh_marital,
        },
        'range': {
            'age': genh_age
        }
    }

    return gen_hierarchies


def main():
    print "Starting SaNGreeA algorithm..."

    ## Prepare io data structures
    adults = csv.readAdults(adults_csv)
    adj_list = csv.readAdjList(adj_list_csv)
    gen_hierarchies = prepareGenHierarchiesObject(adults)


    ## Main variables needed for SaNGreeA
    clusters = [] # Final output data structure holding all clusters
    best_candidate = None # the currently best candidate by costs
    added = {} # dict containing all nodes already added to clusters


    ## MAIN LOOP
    for node in adults:
        if node in added and added[node] == True:
            continue

        # Initialize new cluster with given node
        cluster = CL.NodeCluster(node, adults, adj_list, gen_hierarchies)

        # Mark node as added
        added[node] = True

        ## SaNGreeA inner loop - Find nodes that minimize costs and
        ## add them to the cluster since cluster_size reaches k
        while len(cluster.getNodes()) < GLOB.K_FACTOR:
            best_cost = float('inf')
            for candidate, v in ((k, v) for (k, v) in adults.items() if k > node):
                if candidate in added and added[candidate] == True:
                    continue

                cost = cluster.computeNodeCost(candidate)
                if cost < best_cost:
                    best_cost = cost
                    best_candidate = candidate

            cluster.addNode(best_candidate)
            added[best_candidate] = True

        ## We have filled our cluster with k entries, push it to clusters
        clusters.append(cluster)

    print "Successfully built " + str(len(clusters)) + " clusters."

    out.outputCSV(clusters, "anonymized_" + GLOB.VECTOR + '_weights.csv')



if __name__ == '__main__':
    main()
