from itertools import combinations
import random
import pickle
#from datetime import datetime
import os

## List of names of people
n = [
    "Harry Potter",
    "Gru",
    "Jane Doe",
    "Bruce Wayne",
    "Peter Parker",
    "Wade Wilson",
    "Tony Stark",
    "Walter White",
    "Clark Kent",
    "Oliver Queen",
    "Michael Scofield",
    "Sarah Wright",
    "Amanda Robinson",
    "Laura Shaw"
]

## Function to save pickle files to disk
def save_files(filename, groups):
    """Function to save pickle files to disk

    Args:
        filename (_type_): name of the file to save
        groups (_type_): content to save
    """
    with open(os.path.join("groups",filename), 'wb') as f:
        pickle.dump(groups, f)
        
## Function to load pickle files from disk
def load_files(filename):
    """Function to load pickle files from disk

    Args:
        filename (_type_): name of file to load

    Returns:
        _type_: content of the pickled file
    """
    with open(os.path.join("groups",filename), 'rb') as f:
        return pickle.load(f)


def make_groups(group_comb, groups_count_dict):
    """takes input an already shuffled list of pairs and outputs set of pairs which have not been formed previously (90%)

    Args:
        group_comb (_type_): list of combinations of pair of groups
        groups_count_dict (_type_): dictionary to keep count of formed groups

    Returns:
        _type_: list of pair of groups
    """
    pairs = []
    seen = set()
    for p1, p2 in group_comb:
        if p1 not in seen and p2 not in seen and groups_count_dict[p1,p2]<1:
            pairs.append((p1, p2))
            seen.add(p1)
            seen.add(p2)
    return pairs

## name of file for group combinations
groups_list_filename = "group_list.pkl"

## name of file for group dictionary to keep count
groups_count_filename = "groups_count.pkl"

seed = 10 ## random seed

try:
    ## make a directory if it doesn't exists. To save files.
    if not os.path.exists("groups"):
        os.makedirs("groups")

        ## create pair combinations
        groups_combinations = list(combinations(n,2))
        ## shuffle the pairs
        random.Random(seed).shuffle(groups_combinations)

        ## save the pairs in a file
        save_files(groups_list_filename, groups_combinations)

        ## create a dictionary and initialize to 0 for every pair
        groups_count_dict = dict.fromkeys(groups_combinations,0)
        ## save the dictionary to disk
        save_files(groups_count_filename, groups_count_dict)

    else:
        ## load the pair file and the dictionary
        groups_combinations = load_files(groups_list_filename)
        groups_count_dict = load_files(groups_count_filename)

except:
    pass

## create pairs for the current day
pairs = make_groups(groups_combinations, groups_count_dict)

## check if there are all groups formed
if len(set(pairs)) != (len(n)/2):
    ## unpack tuple into a list
    current_pairs = [element for tupl in pairs for element in tupl]

    ## create list of remaining people
    remaining = tuple(set(n) - set(current_pairs))
    ## if more than 2 people are remaining
    ## then for pairs serial wise
    if len(remaining) > 2:
        for i in range(0,len(remaining),2):
            pairs.append((remaining[i], remaining[i+1]))
    ## if only 2 people remain then form their group        
    elif len(remaining) == 2:
        pairs.append(remaining)

## display all the pairs
for i, x in enumerate(pairs):
    print(i + 1, ":", x)

## for each pair
#### remove it from the pair combination list and increment counter in pair dictionary
for item in pairs:
    if (min(item), max(item)) in groups_combinations:
        groups_combinations.remove((min(item), max(item)))
        groups_count_dict[min(item), max(item)] += 1
    else:
        try:
            ## check (b,a) in group pair or (a,b)
            groups_combinations.remove((max(item), min(item)))
        except ValueError:
            ## if it comes here the both (a,b) and (b,a) doesn't exists in group pairs list
            #### simply increment the counter
            try:
                groups_count_dict[max(item), min(item)] += 1
            except KeyError:
                groups_count_dict[min(item), max(item)] += 1

## save both the group pair list and the pair counter dictionary to the disk
save_files(groups_list_filename, groups_combinations)
save_files(groups_count_filename, groups_count_dict)
