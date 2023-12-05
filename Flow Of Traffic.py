class pq():
    class node(object):
        def __init__(self,key1,value1):
            self.key=key1
            self.val=value1
        def __lt__(self,other):
            if type(self.val)==str:
                return False
            elif type(other.val)==str:
                return True
            elif self.val<=other.val:
                return True
            return False
        def change(self,new):
            self.val=new
            return None
    class wife(object):
        def __init__(self,hub):
            self.husband=hub
            self.index=hub.key
    
    def __init__(self,contents):
        self.data=[self.node(p,q) for p,q in contents]
        self.wives=[self.wife(i) for i in self.data]
        if len(self.data)>1:
            self.build()
    def build(self):
        start=self.parent(len(self.data)-1)
        for i in range (start,-1,-1):
            self.down(i)
    def add(self,key,value):
        self.data.append(self.node(key,value))
        if key<=len(self.data)-1:
            self.wives
        self.up(len(self.data)-1)
    def min(self):
        if self.isempty():
            return ("EMPTY")
        else:
            return [(self.data)[0].key,(self.data)[0].val]
    def extract(self):
        if self.isempty():
            return ("EMPTY")
        self.swap(0,len(self.data)-1)
        item=self.data.pop()
        self.down(0)
        return (item.key,item.val)
    def lot(self):
        ans=[]
        for i in self.data:
            ans.append((i.key,i.val))
        return ans
    def isempty(self):#checks if heap is empty or not
        return len(self.data)==0
    def parent(self,j):#parent of the node
        return (j-1)//2
    def left(self,j):
        return 2*j+1
    def right(self,j):
        return 2*j+2
    def isleft(self,j):
        return self.left(j)<len(self.data)
    def isright(self,j):
        return self.right(j) < len(self.data)
    def swap(self,i,j):
        self.wives[self.data[i].key].index=j
        self.wives[self.data[j].key].index=i
        self.data[i], self.data[j] = self.data[j], self.data[i]
    def up(self,j):
        parent = self.parent(j)
        if j > 0 and self.data[j] < self.data[parent]:
            self.swap(j, parent)
            self.up(parent)
    def down(self,j):
        if self.isleft(j):
            left=self.left(j)
            small_child=left
            if self.isright(j):
                right=self.right(j)
                if self.data[right]<self.data[left]:
                    small_child=right
            if self.data[small_child]<self.data[j]:
                self.swap(j,small_child)
                self.down(small_child)
    def update(self,key,new):
        if self.wives[key].husband.val=='inf':
            self.wives[key].husband.change(new)
            self.up(self.wives[key].index)
        elif new=='inf':
            self.wives[key].husband.change(new)
            self.down(self.wives[key].index)
        elif self.wives[key].husband.val>new:
            self.wives[key].husband.change(new)
            self.up(self.wives[key].index)
        else:
            self.wives[key].husband.change(new)
            self.down(self.wives[key].index)
    def wl(self):
        ans=[]
        for i in self.wives:
            ans.append((i.husband.key,i.index))
        return ans
a=pq([(0,5),(1,3),(2,'inf'),(3,5),(4,100),(5,22),(6,'inf')])


def arrange_edges(l):
    for i in range (0,len(l)):
        tmp=l[i]
        if l[i][1]<l[i][0]:
            l[i]=(tmp[1],tmp[0],tmp[2])
    l=sorted(l)
    l.append(('F','F','F'))
    ans=[]
    for i in range (0,len(l)-1):
        if l[i+1][1]!=l[i][1] or l[i+1][0]!=l[i][0]:
            ans.append(l[i])
    return ans

def graph(n,source,edges):
    graph=[]
    edges=arrange_edges(edges)
    for i in range(0,n):
        if i==source:
            graph.append([0,True,[],None])
        else:
            graph.append(['inf',False,[],None])
    for i in range(0,len(edges)):
        graph[edges[i][0]][2].append([edges[i][1],edges[i][2]])
        graph[edges[i][1]][2].append([edges[i][0],edges[i][2]])
    return graph
def algo(g):
    graph=[]
    for i in range (0,len(g)):
        graph.append(g[i])
    d=[]
    for i in range(0,len(graph)):
        d.append((i,graph[i][0]))
    x=pq(d)
    o=x.extract();flag=True
    while x.isempty()!=True:
        if flag:
            #print("origin")
            #print("wrt",o[0],-o[1])
            nl=graph[o[0]][2]
            for i in nl:
                if graph[i[0]][1]!=True:
                    x.update(i[0],-i[1])
                    graph[i[0]][3]=o[0];graph[i[0]][0]=i[1]
            tmp=x.extract()
            graph[tmp[0]][1]=True
            o=tmp
            flag=False
        else:
            #print("wrt",o[0],-o[1])
            nl=graph[o[0]][2]
            for i in nl:
                if graph[i[0]][1]!=True:
                    if graph[i[0]][0]=='inf':
                        #print('change')
                        #print(graph[i[0]][3],graph[i[0]][0])
                        graph[i[0]][3]=o[0];graph[i[0]][0]=min(i[1],-o[1])
                        x.update(i[0],-min(i[1],-o[1]))
                        #print(o[0],i[0],i[1],-o[1])
                        #print(min(i[1],-o[1]))
                    elif graph[i[0]][0]<min(i[1],-o[1]):
                        #print('change')
                        #print(graph[i[0]][3],graph[i[0]][0])
                        graph[i[0]][3]=o[0];graph[i[0]][0]=min(i[1],-o[1])
                        x.update(i[0],-min(i[1],-o[1]))
                        #print(o[0],i[0],i[1],-o[1])
            tmp=x.extract()
            graph[tmp[0]][1]=True
            o=tmp
    return graph

g=graph(6,0,[(0,1,7),(0,2,9),(2,3,6),(2,4,5),(2,5,4)])

def ans(gr,s,t):
    solved=algo(gr)
    tmp=solved[t];ans=[];maxt=tmp[0]
    while tmp[3]!=None:
        ans.append(tmp[3])
        tmp=solved[tmp[3]]
    final=[]
    for i in range (1,len(ans)+1):
        final.append(ans[-i])
    final.append(t)
    return [maxt,final]

def findMaxCapacity(n,edges,s,t):
    g=graph(n,s,edges)
    return ans(g,s,t)




