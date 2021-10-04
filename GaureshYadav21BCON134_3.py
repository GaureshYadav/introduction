import pandas as pd
import matplotlib.pyplot as plt
x=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
y=[31,28,31,30,31,30,31,31,30,31,30,31]
df=pd.DataFrame(y,x)
print(df)
plt.bar(x,y,color=['r','g','b','y','orange','c','k','pink','grey','purple','brown','violet'])
plt.title('Name and Days of a Month',size=15,style='italic')
plt.Line2D(x,y)
plt.show()
plt.plot(x,y,marker='s')
plt.show()
