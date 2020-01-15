import random
import string

password_length=int(input("How long will your password be? "));
password=[];
i=0;

while (i<password_length):
  i+=1;
  rand_num_for_if=random.randint(0,100);
  if(rand_num_for_if%2==0):
    number=random.randint(0,9);
    password.append(str(number));
  elif(rand_num_for_if%2!=0):
    letter=random.choice(string.ascii_letters);  
    password.append(letter);

listToStr = ' '.join([str(elem) for elem in password]) 
listToStr=listToStr.replace(' ','');
print(listToStr);
