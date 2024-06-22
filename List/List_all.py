# List example

print('********************** List Example **********************')
list1 = [11,22,33,45,6,7,78,9,0,None]
print(list1)

print('********************** New **********************')
# Adding number into list
list1.append(444)
print(list1)

print('********************** New **********************')
mixList = [21,3,"Mix", 'Mango',5.5,6,'Eins']
print(mixList)

print('********************** New **********************')
# Adding data into list
mixList.append('Kivi')
print(mixList)

# Inserting data at perticulat position
print('********************** New **********************')
fruits =  ['Mango', 'Orange']
fruits.insert(0,'Jackfruit')
fruits.insert(8, 'Kiiiiiiiii')
print(fruits)

# Joining two list 
print('********************** New **********************')
Color1 = ['Yello', 'Red']
Color2 = ['Green', 'Black']
All_Color = Color1+Color2
print(All_Color)

# extend method for list
print('********************** New **********************')
Color1.extend(Color2)
print(Color1)
print(Color2)

# Difference between append and extend(It will give list inside list)
print('********************** New **********************')
Color1.append(Color2)
print(Color1)