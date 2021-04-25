picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

def show_tree():
    for item in picture:
        for i in item:
            if i == 0:
                print(' ', end=' ')
            else:
                print('*', end=' ')
        print('') # need a newline after every row

show_tree()
show_tree()
show_tree()