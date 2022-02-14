#!/usr/bin/env python
# coding: utf-8

# # Program wyznaczający trase za pomocą algorytmu A*

# In[142]:
import sys, math #this library is necessery only to define infinite

"""Function preparing matrix to read nodes"""

def graph_node(matrix):
    
    node_list = [] 
    end_list = {}

    for line in matrix:
        if line[0] == ' ':
            line = line[1:]
        num_list = list(map(lambda x: float(x),line.split(' '))) #delete /n
        result_all = {}
        # To jest żle
        #for i in num_list:
        #    result_all[num_list.index(i)] = i
        # Powinno być
        for j,i in enumerate(num_list):
            result_all[j] = i

        result = {key:val for key, val in result_all.items() if val != 0}
        node_list.append(result) 
    # Było
    #for i in node_list:
    #        end_list[node_list.index(i)] = i
    # Jest
    for j,i in enumerate(node_list):
        end_list[j] = i
    #return direction of directions with connection of each nodes
    return end_list


# In[143]:


"""Create a list of nodes coordinates from txt file"""
def read_coordinates(lines):
    coordinates = []
    for bracket in range(lines[0].count(',')):
        coordinates.append([float(i) for i in (lines[0].split("("))[bracket+1].split(")")[0].split(', ')]) #extract numbers from bracket
    return coordinates


# In[144]:


"""Heuristic function is the distance from  a point to the goal"""
def heuristic_function(coordinates, goal):
    heuristic = {}
    for coordinate in coordinates:
        distance = ((coordinates[goal][0]-coordinate[0])**2+(coordinates[goal][1]-coordinate[1])**2)**(1/2) #distance from formula
        heuristic[coordinates.index(coordinate)] =  distance #add as a list of dictionaries
    # returns a distance from each point to finish
    return heuristic


#  # Algoritm A*

# In[145]:


def reconstruct_route(came_from, consider_node):
    route = [consider_node]
    while consider_node in came_from.keys():
        consider_node = came_from[consider_node]
        route.insert(0,consider_node)
    route = [i+1 for i in route] #algoritm count from 0, but we want to see that the first node is 1 so add 1 to each of node
    return route


# In[146]:




def algoritm_A(start, goal):
    suspicious = [start]
    came_from = {}
    g_score ={}
    f_score = {}

    # fill dictonaries 'inf'
    for coordinate in range(len(coordinates)):
        g_score[coordinate] = 'inf'
        f_score[coordinate] = 'inf'
    g_score[start] = 0
    f_score[start] = heuristic.get(start)

    while len(suspicious)>0:
    
        consider_node = min(suspicious, key = lambda sus : f_score[sus])
    
        if consider_node == goal:
            route = reconstruct_route(came_from,consider_node)
            # if you want to display cost of route uncomment this: 
            #print(f_score[goal], end=' : ')
            return route 
    
        suspicious.remove(consider_node)
        for y in graph[consider_node]:
            t_g = g_score[consider_node] + graph[consider_node][y]
            if t_g < float(g_score[y]):
                came_from[y] = consider_node
                g_score[y] = t_g
                f_score[y] = g_score[y] + heuristic[y]
                if y not in suspicious:
                    suspicious.append(y)
    return "Brak"


# In[147]:


"""Main Program"""
file_number = sys.argv[1:]
for i in range(len(file_number)):
    filename = f'{file_number[i]}'
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()

        """definition start and goal value"""
        start = int(lines[1].split(" ")[0])-1
        goal = int(lines[1].split(" ")[-1])-1
        graph = graph_node(lines[2:])
        coordinates = read_coordinates(lines)
        heuristic = heuristic_function(coordinates, goal)

        a = algoritm_A(start,goal)
        if isinstance(a, str):
            print(a)
        else:
            print(''.join(str(i)+' ' for i in a))
    except:
        print('Nie można wczytać pliku, Nie poprawny graf')


# In[ ]:


