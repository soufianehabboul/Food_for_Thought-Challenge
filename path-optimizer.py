from tkinter import *
import matplotlib.pyplot as plt

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, end):
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def main(start,end):  
    # Maze Example
    maze = [    
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ]
    
    # A* function call
    path = astar(maze, start, end)
    
    # Path visualization 
    maze[path[0][0]][path[0][1]] = 3
    maze[path[-1][0]][path[-1][1]] = 3
    
    for i in range (1,len(path)-1):
        maze[path[i][0]][path[i][1]] = 5
    plt.matshow(maze)
    plt.show()

if __name__ == '__main__':

    fenetre = Tk()
    fenetre.geometry("300x300")

    def action():
        start = (int(xs.get()),int(ys.get()))
        end = (int(xe.get()),int(ye.get()))
        main(start,end)

    # Interface generation    
    lblStart=Label(fenetre,text="Start")
    lblStart.pack()
    lblx=Label(fenetre,text="x: ")
    lblx.pack()
    xs=Entry(fenetre)
    xs.pack()
    lbly=Label(fenetre,text="y: ")
    lbly.pack()
    ys=Entry(fenetre)
    ys.pack()
    lblEnd=Label(fenetre,text=" ")
    lblEnd.pack()
    lblEnd=Label(fenetre,text=" ")
    lblEnd.pack()
    lblEnd=Label(fenetre,text="End")
    lblEnd.pack()
    lblx=Label(fenetre,text="x: ")
    lblx.pack()
    xe=Entry(fenetre)
    xe.pack()
    lbly=Label(fenetre,text="y: ")
    lbly.pack()
    ye=Entry(fenetre)
    ye.pack()
    lblEnd=Label(fenetre,text=" ")
    lblEnd.pack()
    ok=Button(fenetre, text="Submit !",command=action)
    ok.pack()
    fenetre.mainloop()


    
    


