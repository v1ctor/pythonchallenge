from PIL import Image

r = Image.new('RGB', (100,100))
rx = r.load()

i = Image.open("wire.png")
px = i.load()

# for i in range(10000):
#     x = i / 100
#     y = i % 100
#     rx[y, x] = px[i, 0]

c = 0
k = 0 
m = 99
l = 0
n = 99
while k < m and l < n:

    for i in range(l, n):
        rx[k,i] = px[c,0]
        c += 1

    k += 1

    for i in range(k, m) : 
        rx[i,n - 1] = px[c,0]
        c += 1
              
    n -= 1
  
    if ( k < m) : 
            
        for i in range(n - 1, (l - 1), -1): 
            rx[m - 1,i] = px[c,0]
            c += 1
            
        m -= 1
          
    if (l < n) : 
        for i in range(m - 1, k - 1, -1): 
            rx[i,l] = px[c,0]
            c += 1
        l += 1




r.show()
