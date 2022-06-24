from collections import Counter
from collections import defaultdict
def _showTotalRelations():
    with open('people(1).csv') as people_file, open('relationships.csv') as relative_file:
        people = list(csv.reader(people_file,delimiter=','))
        relationship = list(csv.reader(relative_file,delimiter=','))
        
        
        #required lists
        person_names = list()
        relation_names = list()
        storeCount = list()
        result_names = list()
        merged_stores = list()
        total_relation = list()
        
    
        
        
        count1 = 0
        
        i = 1
        for person in people:
            person_names.insert(i, person[1]) # 1 to 0
            i += 1
        i = 1
        for relation in relationship:
            relation_names.insert(i, relation[0])
            i += 1
            relation_names.insert(i, relation[2]) # 0 to 2
            i += 1
            
            
            
        j=1
        for names in person_names:
            if names not in relation_names:
                result_names.insert(j,names)
                j += 1
                
        j=1
        for names in relation_names:
            if names not in person_names:
                result_names.insert(j,names)
                j +=1
        
        
        
            
        #################################total-rel###################
       
            
                
                
 
    

    
    

                
                
            
        #print(person_names)
        print("\n")
        print(relation_names)
        print("\n")
        print(result_names)
        print("\n")
        
        
        
        
        
        #merge two list
        merged_list = relation_names + result_names
        #print(merged_list)
        #print("\n")
        
        
    
        i = 1
        
        for item in merged_list:
            if item in merged_list:
                merged_stores.insert(i,item)
                #print(item)
                #print("\n")
                
        
        
        my_list_result = {}
        i = 0
        for i in merged_list:
            if i in my_list_result:
                my_list_result[i] = my_list_result[i] + 1
            else:
                my_list_result[i] = 1
                
            
                
          
            if i not in my_list_result:
                my_list_result[i] = 1
          
                
                
            
                
                
                
                
         
        mytups = my_list_result.items()
        
        print(mytups)