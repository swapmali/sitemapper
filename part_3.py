import os
import time


fp = open("sitemap_links.txt", "r")
site_links = []
n = 5
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

print(site_links)

"""
for i in range(len(site_links)):
    if site_links[i] == '':
        pass
    else:
        print(site_links[i])
"""
set_new_cur_link = 1
k = 1
this_level_arr = []
relation = [[[] for y in range(10)] for x in range(n)]
print(relation)
# remaining iterations
# k = level
while k < n:
    # creating this level headers array
    for j in range(len(site_links)):
        if site_links[j] == '':
            pass
        elif '/' in site_links[j]:
            slash_ind = site_links[j].index('/')
            link = site_links[j][:slash_ind]
            this_level_arr.append(link)
        else:
            this_level_arr.append(site_links[j])
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
                part_of_site = site_links[i][:len(cur_link)]
                if part_of_site == cur_link:
                    site_links[i] = site_links[i][len(cur_link) + 1:]
                    if '/' in site_links[i]:
                        slash_ind = site_links[i].index('/')
                        link = site_links[i][:slash_ind]
                        relation[k][j].append(link)
                    else:
                        relation[k][j].append(site_links[i])

            set_new_cur_link = 1

    this_level_arr = []
    # print(site_links)
    k += 1

print(site_links)
print(levels)
print()
for i in range(len(relation)):
    print(i, relation[i])
