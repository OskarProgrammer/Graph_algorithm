# how many woman are in the graph from the name point

from collections import deque

def isWoman(person): return True if person[-1] == 'a' else False

def countWomanInTheGraph(name, graph):
    searchQueue = deque()

    try:
        searchQueue += graph[name]
    except KeyError:
        print(f"There is no {name} in the graph")
        return None
    
    searchedAlready = []
    count = 0 

    while searchQueue:
        person = searchQueue.popleft()

        if not person in searchedAlready:
            if isWoman(person):
                if person != name:
                    count += 1
            searchedAlready.append(person)
            searchQueue += graph[person]
        
    
    return count

# implementation of the graph
graph = {
    "me": ["Nathan", "Sara", "Karolina","Julka"],
    "Nathan": ["Oskar", "Maciek", "Kamil"],
    "Julka": ["Sara", "Kamil"],
    "Karolina": ["Paulina"],
    "Sara": ["Oskar"],
    "Paulina": ["Ela"],
    "Oskar": ["me", "Lara"],
    "Ela": ["Paulina"],
    "Kamil": ["Sara"],
    "Maciek": [],
    "Lara": []
}

arg = "me"

if countWomanInTheGraph(arg,graph) != None:
    amount = countWomanInTheGraph(arg,graph)
    print(f"The amount of woman in the graph: {amount}")
