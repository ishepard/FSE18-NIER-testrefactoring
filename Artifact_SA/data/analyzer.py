
import random

total_commit = set()


with open("sonarqube/sonarqube-class-pairs.csv", "r") as f:
    for line in f:
        commit, _, _ = line.strip().lower().split(",")
        total_commit.add(commit)

selected_commit = random.sample(total_commit, 5)
# selected_commit = ["32e1a9c85506afc25e62fdbd2076473bdc4fc4d0"]

print(selected_commit)

def category_assigner(metric: str, val : int):
    cat = "HIGH"
    if metric == "nof":
        if val < 9: cat = "MEDIUM"
        if val < 5: cat = "LOW"
        if val < 3: cat = "VERY_LOW"
    if metric == "nom":
        if val < 20: cat = "MEDIUM"
        if val < 13: cat = "LOW"
        if val < 9: cat = "VERY_LOW"
    if metric == "wmc":
        if val < 46: cat = "MEDIUM"
        if val < 26: cat = "LOW"
        if val < 17: cat = "VERY_LOW"
    if metric == "loc":
        if val < 281: cat = "MEDIUM"
        if val < 173: cat = "LOW"
        if val < 126: cat = "VERY_LOW"
    return cat


for c_commit in selected_commit:
    class_pairs = {}
    with open("sonarqube/sonarqube-class-pairs.csv", "r") as f:
        for line in f:
            commit, prod_name, test_name = line.strip().lower().split(",")

            # if commit != c_commit:
            #     continue

            class_pairs[prod_name] = test_name

    metrics = {}
    with open("sonarqube/sonarqube-monthly-metrics.csv", "r") as f:
        for line in f:
            hash, _, fileType, file, _, _, _, _, _, nof, _, _, nom, _, _, _, _, wmc, loc, _ = line.strip().lower().split(",")

            if hash != c_commit:
                continue

            metrics[file] = (fileType, nof, nom, wmc, loc)

    for file in metrics.keys():
        fileType, nof, nom, wmc, loc = metrics[file]

        if fileType == "productionfile":
            if file in class_pairs:
                test_filename = class_pairs[file]

                if test_filename in metrics:
                    fileType_T, nof_T, nom_T, wmc_T, loc_T = metrics[test_filename]

                    # print("PROD VALUES: {},{},{},{},{}".format(file, nof, nom, wmc, loc))
                    # print("TEST VALUES: {},{},{},{},{}".format(test_filename, nof_T, nom_T, wmc_T, loc_T))

                    cat_p_nof = category_assigner("nof", int(nof))
                    cat_p_nom = category_assigner("nom", int(nom))
                    cat_p_wmc = category_assigner("wmc", int(wmc))
                    cat_p_loc = category_assigner("loc", int(loc))

                    cat_t_nof = category_assigner("nof", int(nof_T))
                    cat_t_nom = category_assigner("nom", int(nom_T))
                    cat_t_wmc = category_assigner("wmc", int(wmc_T))
                    cat_t_loc = category_assigner("loc", int(loc_T))

                    print("{}:{},{}:{},{}:{},{}:{}".format(cat_p_nof,cat_t_nof,cat_p_nom,cat_t_nom,cat_p_wmc,cat_t_wmc,cat_p_loc,cat_t_loc))
