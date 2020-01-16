import random
import string

def pw_generator():
  password_length=int(input("How long will your password be? "));
  i=0;
  password=[];
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
  ask_to_save=input("Do you wish to save this password? yes/no ");
  if(ask_to_save=='no'):
    generate_again=input('Generate again? yes/no ');
    if(generate_again=='yes'):
      pw_generator();
    elif(generate_again=='no'):
      print("aight, head");
  elif(ask_to_save=='yes'):
    which_format=input("In which format would you like to save? Txt ")
    pass_for_what=input("Name for what that password is used: ");
    if(which_format=='txt'):
      Pass_file = open("password_file.txt", "a");
      Pass_file.write("Password for "); Pass_file.write(pass_for_what);
      Pass_file.write(" : ");
      Pass_file.write(listToStr);
      Pass_file.close();
      print("check file named password_file.txt");

print("To generate a password enter 1.");
print("To get a password from DB enter 2.");
option=int(input("What do you want to do? "));
if(option==1):
  pw_generator();

