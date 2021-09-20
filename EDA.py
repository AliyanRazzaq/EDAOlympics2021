from PIL.Image import ROTATE_180
import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle, islice
import seaborn as sns
from wordcloud import WordCloud
import geopandas
df = pd.read_excel("Athletes.xlsx")

# #Description of Dataset
# print (df.describe())
# print (df.info())

# # All unique countries 
# print (df['NOC'].unique())

# # All unique Atheletes
# print (df['Name'].unique())

# # All unique disciplines
# print (df['Discipline'].unique())

# # Number of Athelets participated from each country
# df1 = df.drop_duplicates(['Name'])
# df2 = df1['NOC'].value_counts()
# print(df2)


# #List of Athelets who participated in more than one discipline
# ath = df.Name.value_counts()
# l = ath[ath>1].index.tolist()
# print (l)

# #Countries of atheletes who participated in more than one discipline
# df2 = df[df["Name"].duplicated()]
# print(df2[['Name','NOC']])


#Top 25 Countries with majority participants
# df1 = df.drop_duplicates(['Name'])
# df2 = df1['NOC'].value_counts().head(25).to_frame()
# x = df2.index
# y = df2.NOC
# plt.barh(x,y)
# plt.gca().invert_yaxis()
# plt.title('Top 25 Countries with majority participants', fontsize = 20)
# plt.ylabel('Name of The Countries', fontsize = 15)
# plt.xlabel('Number of Atheletes Participated',fontsize = 15 )
# plt.show()



# Wod Clouds
# wordcloud2 = WordCloud().generate(' '.join(df['NOC']))
# plt.figure(figsize=(20,15))
# plt.imshow(wordcloud2, interpolation='bilinear')
# plt.axis("off")
# plt.show()

# wordcloud2 = WordCloud().generate(' '.join(df['Discipline']))
# plt.figure(figsize=(20,15))
# plt.imshow(wordcloud2, interpolation='bilinear')
# plt.axis("off")
# plt.show()


#GeoPandas Visualization
df1 = df.drop_duplicates(['Name'])
df2 = df1['NOC'].value_counts().head(25).to_frame()
x = df2.index
y = df2.NOC
gdf.plot(x,y)
plt.gca().invert_yaxis()
plt.title('Top 25 Countries with majority participants', fontsize = 20)
plt.ylabel('Name of The Countries', fontsize = 15)
plt.xlabel('Number of Atheletes Participated',fontsize = 15 )
plt.show()
