"""
Avraham Bar Ilan
205937949
01
ass07
"""
import csv

"""
Function name: dict_sorting
Input: dict (dictionary)
Output: dict (sorted dictionary)
Function operation: function sort the keys and put them into a list
    and then moves on the sorted keys and put them into a dict with their original values
"""

def dict_sorting(dict):
    # declare new dict and list
    sorted_dict = {}
    sorted_keys = []
    # put sorted keys into the list
    sorted_keys = sorted(dict.keys())
    # moves on the sorted keys and put the values into the sorted keys
    for key in sorted_keys:
        sorted_dict[key] = dict[key]
    return sorted_dict

"""
Function name: parser
Input: str (string of file content)
Output: list (list of the links from the file)
Function operation: function gets a string which contains the content of the file
    function splits the string and search the words with href= inside
    if function finds href= function cut the word and add it to the links list,
    and then sorts the list and returns it
"""

def parser(file_str):
    # declare new lists
    words_list = []
    links_list = []
    # split string to seperated words
    words_list = file_str.split()
    for word in words_list:
        if "href=" in word:
            # remove the first 6 chars and the last 7 chars from the word
            word = word[6:-7]
            if word not in links_list:
                # add the link to the list
                links_list.append(word)
    links_list.sort()
    return(links_list)

"""
Function name: crawler
Input: str (file name)
Output: void
Function operation: function check if key exists, if exists function returns, if not exist
    functioin open the file and put the links from the list into a links list
    and then put the list into a dict with the file name as a key
    and go recursively on the links from the list
"""

def crawler(file):
    file_name = file
    # if key is alreadt exist function returns
    if file_name in dict:
        return
    # open the given file
    file = open(file)
    file_content = file.read()
    file.close()
    # if the content of the file contains a href=
    if "href=" in file_content:
        links_list = parser(file_content)
        # put the list of the links into to dict
        dict[file_name] = links_list
        # the function call itself for each link (recursively)
        for link in links_list:
            crawler(link)
    return


dict = {}
# get file name from user
file_name = input("enter source file:\n")
crawler(file_name)
# sort the dict
dict = dict_sorting(dict)
# put dict into a csv file
with open('results.csv', 'w') as f:
    for key in dict.keys():
        f.write("%s, %s\n" % (key, dict[key]))
# get another file name
file_given = input("enter file name:\n")
# call craler for the file given
crawler(file_given)
dict = dict_sorting(dict)
# print the links in the file
print(dict[file_given])