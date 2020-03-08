def towerofhanoi(n,fromnode,tonode,auxnode):
    if n == 1:
        print("Move disk from ",fromnode, " to ",tonode)
        return
    towerofhanoi(n-1,fromnode,auxnode,tonode)
    print("Move disk from ",fromnode," to ",tonode)
    towerofhanoi(n-1,auxnode,tonode,fromnode)


towerofhanoi(20,"A","C","B")