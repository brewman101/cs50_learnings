def Find(string):
    x=string.split()
    res=[]
    for i in x:
        if i.startswith("https://www.youtube.com"):
            res.append(i)
    return res
             
# Driver Code
string = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
print("Urls: ", Find(string))