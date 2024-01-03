colours = ["grey", "white", "orange", "pink", "purple", "blue", "aqua", "turquoise"]

combinations = []

for i in colours:
    for j in colours:
        for k in colours:
            for l in colours:
                temp_list = []
                
                temp_list.append(i)
                temp_list.append(j)
                temp_list.append(k)
                temp_list.append(l)

                if i in temp_list[1:] or j in temp_list[2:] or k in temp_list[3:]:
                    continue
                
                temp_list.sort()
                
                print(temp_list)
                
                if temp_list not in combinations:
                    print(temp_list)
                    combinations.append(temp_list)

print(combinations)