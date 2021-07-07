import os
import sys
import warnings

import pandas as pd

warnings.simplefilter(action='ignore', category=FutureWarning)


def main(path_to_csv, path_to_txt):
    data = pd.DataFrame(pd.read_csv(path_to_csv))
    reader = open(path_to_txt)
    test: str = reader.readline()
    reader.close()
    STRs = data.drop("name", 1).columns.values
    suspect_profile = {}
    for STR in STRs:
        count_max = 0
        counter = 0
        prev_index = 0
        index = test.find(STR)
        while index != -1:
            if index-prev_index == len(STR):
                counter += 1
            else:
                if counter >= count_max:
                    count_max = counter
                    counter = 1
            prev_index = index
            index = test.find(STR, index+len(STR))
        if counter >= count_max:
            count_max = counter
        suspect_profile[STR] = count_max

    mb_who = data["name"].values.tolist()
    for STR in STRs:
        df = data[data[STR] == suspect_profile[STR]]['name'].values

        new_mb_who = []
        for name in df:
            if mb_who.count(name) != 0:
                new_mb_who.append(name)
        mb_who = new_mb_who
        if len(mb_who) == 0:
            break

    # print result
    print("%s" % (mb_who[0] if len(mb_who) > 0 else "No match"))


def checking_1st_argument(mb_path_to_csv):
    return os.path.isfile(mb_path_to_csv) and mb_path_to_csv[-3:] == "csv"


def checking_2nd_argument(mb_path_to_txt):
    return os.path.isfile(mb_path_to_txt) and mb_path_to_txt[-3:] == "txt"


def print_help():
    print("Right: dna.py path/to/your.csv path/to/your.txt")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Wrong number of args.")
        print_help()
    else:
        is_1st_arg_valid = checking_1st_argument(sys.argv[1])  # check 1st arg: path to csv
        is_2nd_arg_valid = checking_2nd_argument(sys.argv[2])  # check 2nd arg: path to txt
        if is_1st_arg_valid and is_2nd_arg_valid:
            main(sys.argv[1], sys.argv[2])
        else:
            if is_1st_arg_valid == is_2nd_arg_valid:
                print("Both args are invalid.")
            else:
                print("%s arg is invalid." % ("First" if is_2nd_arg_valid else "Second"))
            print_help()
