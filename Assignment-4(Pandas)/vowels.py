#Vowels, having 5 elements with index labels ‘a’, ‘e’, ‘i’, ‘o’ and ‘u’ and all the five values set to zero. Check if it is an empty series. 
import pandas as pd
vowels=pd.Series([0,0,0,0,0],index=["a","e","i","o","u"])
empty=vowels.empty
print(vowels)
print("Is Series empty?",empty)

# Set all the values of Vowels to 10 and display the Series. 
vowels[:]  =10
print(vowels)

# Divide all values of Vowels by 2 and display the Series. 
vowels=vowels/2
print(vowels)

#Create another series Vowels1 having 5 elements with index labels ‘a’, ‘e’, ‘i’, ‘o’ and ‘u’ having values [2,5,6,3,8] respectively.
vowels1=pd.Series([2,3,6,3,8],index=['a','e','i','o','u'])
print(vowels1)

# Add Vowels and Vowels1 and assign the result to Vowels3.
vowels3=vowels+vowels1
print(vowels3)

#Subtract, Multiply and Divide Vowels by Vowels1. 
vowels4=vowels-vowels1
vowels5=vowels*vowels1
vowels6=vowels/vowels1
print(vowels4)
print(vowels5)
print(vowels6)

#Alter the labels of Vowels1 to [‘A’, ‘E’, ‘I’, ‘O’, ‘U’].
vowels1.index=['A','E','I','O','U']
print(vowels1)



