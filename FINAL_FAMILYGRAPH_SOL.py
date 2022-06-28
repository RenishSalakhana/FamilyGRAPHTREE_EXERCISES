#Questions from Family Graph Relationships 

#code(py):

import csv

import pandas as pd

import numpy as np


print("---------Reading the people.csv file-------------")
def display_people_csv():
    with open('people(1).csv','r') as obj:
        fobj = csv.reader(obj)
        for row in fobj:
            print(row)
			
			
display_people_csv()


print("-----Reading the relationships.csv file-------")
def display_relationship_csv():
    with open('relationships.csv','r') as obj:
        fobj = csv.reader(obj)
        for row in fobj:
            print(row)

			
display_relationship_csv()



print("-----------Displaying total relationship with each other------------")
def show_total_relations():
    with open('people(1).csv') as people_file, open('relationships.csv') as relative_file:
        
        people = list(csv.reader(people_file,delimiter=','))   #making list of people.csv file
    
        relationship = list(csv.reader(relative_file,delimiter=',')) #making list of relationship.csv file
        
        #Making lists  
        
        person_name_list2 = list()
        
        person_name_list1 = list()
            
        
        
          
        
        #to show the relationships of all people's with each others with validated excepted numbers of people's:
        
        for person in people:
            for relation in relationship:
                if person[1] == relation[0]: 
                    
                    print(person[0] + " and " + relation[3] + " are " + relation[1]) 
            
                    
        
        i=0
        for person in people:
            for relation in relationship:
                if person[1] == relation[0]:
                    person_name_list1.insert(i,person[0])
                    i+=1
                    
        i=0           
        for person in people:
            person_name_list2.insert(i,person[0])
            i+=1
            
            
           
                
                
        print("\n") 
        print("---List of names of people's and Relationships---")
        print(person_name_list1)
        
        print("\n") 
        print("---List of people's names---")
        print(person_name_list2)
        
        
        merged_people_and_relations_list = person_name_list2 + person_name_list1
        print("\n")
        print("People's Names")
        print(merged_people_and_relations_list)
        
        
                
    
        
        total_member_list = {}
        #i=1
        for i in merged_people_and_relations_list:
            if i in total_member_list:
                total_member_list[i] = total_member_list[i] + 1
            else:
                total_member_list[i] = 1
                
        
        k= 'Alan'
        for i in merged_people_and_relations_list:
            total_member_list[k] = 0
                
                
        total_people_relation =  total_member_list.items()
        print("\n")
        print("---3rd Exe Solution :\nTotal relations of people's with each others and Validated correct relationships loaded---")
        print("\n")
        print(total_people_relation)
        
show_total_relations()



def search_family_relations():
    with open('people(1).csv') as people_file, open('relationships.csv') as relative_file:
        people = list(csv.reader(people_file,delimiter=','))
        relationship = list(csv.reader(relative_file,delimiter=','))
          
        
        #making lists 
    
        family_relation_list = list()
    
        
        
        for person in people:
            for relation in relationship:
                if ((person[1] == relation[0] ) and relation[1] == 'FAMILY'):
                    print(person[0] + " and " + relation[3] + " are " + relation[1])
        
        i=0
        for person in people:
            for relation in relationship:
                if ((person[1] == relation[0] ) and relation[1] == 'FAMILY'):
                    family_relation_list.insert(i,relation[0])
                    i+=1
                    family_relation_list.insert(i,relation[2])
                    i+=1
                    
                
                
                
                
                
        
        print("\n")
        print("---family_relation_list---")
        print(family_relation_list)    
            
        i=1
        my_relation_list = {}
        for i in family_relation_list:
            if i in my_relation_list:
                my_relation_list[i]+=1
            else:
                my_relation_list[i] = 1
                
        
        
        total_family_relation = my_relation_list.items()
        print("\n")
        print("---Total family relations---")
        print(total_family_relation)
        
search_family_relations()         
        
        
        
                     
                    
        
        
                
                    
            
            
                
                
            
                    
        
    
        
        
        
        
        
                
        
        
        
                          
                    			



