from collections import Counter
from collections import defaultdict
def _showTotalRelations():
    with open('people(1).csv') as people_file, open('relationships.csv') as relative_file: #opening files as file obj 
        people = list(csv.reader(people_file,delimiter=','))  #making list of people file
        relationship = list(csv.reader(relative_file,delimiter=',')) #making list of relationship file
        
        
        #required lists
        person_names = list()
        
        relation_names = list()
        
        storeCount = list()
        
        result_names = list()
        
        merged_stores = list()
        
        total_relation =list()
        
        
        #adding required columns data from lists
        i = 1
        for person in people:
            person_names.insert(i, person[1]) #add people person col 1
            i += 1
        i = 1
        for relation in relationship:
            relation_names.insert(i, relation[0]) #add relationship relation col 0
            i += 1
            relation_names.insert(i, relation[2]) #add relationship relation col 2
            i += 1
            
            
        #check whether data is there or not    
        j=1
        for names in person_names:
            if names not in relation_names:
                result_names.insert(j,names)
                j += 1
                
        j=1
        for names in relation_names:
            if names not in person_names :
                result_names.insert(j,names)
                j += 1
                
                
        #------printing lists -------------    
        #print(person_names)
        print("----------------printing the relation_names-------------------------")
        print("\n")
        print(relation_names)
        print("\n")
        print("-----------------printing the result_names--------------------------")
        print("\n")
        print(result_names)
        print("\n")
        
        
        
        #merging two lists to get output 
        merged_list = relation_names + result_names
        print("----------------printing merged data to show only for reference  ------------------------")
        print("\n")
        print(merged_list)
        
        
        
        #counts the data of each person individual based on condition 
        my_list_result = {}
        i = 0
        for i in merged_list:
            if i in my_list_result:
                my_list_result[i] = my_list_result[i] + 1
            else:
                my_list_result[i]=1
        
                
        mytups = my_list_result.items() #final output 
        print("\n")
        print("----------printing the final total family member---------")
        print("\n")
        print(mytups)