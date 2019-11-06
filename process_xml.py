from xml.dom import minidom
import os
import json
# parse an xml file by name
mydoc = minidom.parse('sitemap.xml')

items = mydoc.getElementsByTagName('loc')
fp = open("sitemap_links.txt", "w+")
print(items)
# all items data

print('\nAll item data:')
for elem in items:
    fp.write(elem.firstChild.data+"\n")
    print(elem.firstChild.data)
print("\n Data Written to a file sitemap_links.txt")
fp.close()


"""
PART-3

NOTE:  @ time of crawling, The domain link should be like http://cse.nitk.ac.in and not like http://cse.nitk.ac.in/
"""

fp = open("sitemap_links.txt", "r")
site_links = []
n = int(input("Enter the Levels You want to Explore: "))
# n = 20
levels = [[] for x in range(n)]

link = fp.readline()

# creating array of links by reading sitemap_links.txt file
while link:
    site_links.append(link[:-1])
    link = fp.readline()
# print(site_links)
cur_link = site_links[0]

# print(levels)

# for 1st iteration
for i in range(len(site_links)):
    part_of_site = site_links[i][:len(cur_link)]
    if part_of_site == cur_link:
        site_links[i] = site_links[i][len(cur_link) + 1:]

levels[0].append(cur_link)

# print(site_links)


set_new_cur_link = 1
k = 1
this_level_arr = []
relation = [[[] for y in range(len(site_links))] for x in range(n)]

# remaining iterations
# k = level
while k < n:
    # creating this level headers array
    this_level_arr = []
    for j in range(len(site_links)):
        if site_links[j] == '':
            pass
        elif '/' in site_links[j]:
            slash_ind = site_links[j].index('/')
            link = site_links[j][:slash_ind]
            if link not in this_level_arr:
                this_level_arr.append(link)
        else:
            if site_links[j] not in this_level_arr:
                this_level_arr.append(site_links[j])
            site_links[j] = ''
    # print(this_level_arr)

    # copy this_level_arr into the correct level
    for j in range(len(this_level_arr)):
        levels[k].append(this_level_arr[j])

    for i in range(len(site_links)):
        for j in range(len(this_level_arr)):
            if set_new_cur_link:
                cur_link = this_level_arr[j]
                set_new_cur_link = 0

            if '/' not in site_links[i]:
                pass
            else:
                # remove current headers from the site_links and add relation from this headers to next level children
                # e.g. for level 1 parent relation 1 contains its children (obv which lies in level 2)
                part_of_site = site_links[i][:len(cur_link)]
                if part_of_site == cur_link:
                    site_links[i] = site_links[i][len(cur_link) + 1:]
                    if '/' in site_links[i]:
                        slash_ind = site_links[i].index('/')
                        link = site_links[i][:slash_ind]
                        if link not in relation[k][j]:
                            relation[k][j].append(link)
                    else:
                        if site_links[i] not in relation[k][j]:
                            relation[k][j].append(site_links[i])

            set_new_cur_link = 1

    # print(site_links)
    k += 1
relation[0][0] = levels[1]
#print(site_links)
print("-"*50 + "Levels" + "-"*50)

if os.path.exists('levels.json'):
    os.remove('levels.json')
if os.path.exists('relation.json'):
    os.remove('relation.json')

print("{\"levels\":[", file=open("levels.json", "a"))
for i in range(len(levels)):
    print(i, levels[i])
    print(json.dumps(levels[i]), file=open("levels.json", "a"))
    if i != len(levels) - 1:
        print(",", file=open("levels.json", "a"))
print("]}", file=open("levels.json", "a"))
print()
print("-"*50 + "Relations" + "-"*50)

print("{\"relations\":[", file=open("relation.json", "a"))
for i in range(len(relation)):
    print(i, relation[i])
    print(json.dumps(relation[i]), file=open("relation.json", "a"))
    if i != len(relation) - 1:
        print(",", file=open("relation.json", "a"))

print("]}", file=open("relation.json", "a"))
