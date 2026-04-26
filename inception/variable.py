#variable = acts like a container which stores value ( string, integer, float ) 
for eg:
first_name="Ashutosh"
print(first_name)
the output will be "Ashutosh"; as it stores my name which is string value. 

I can also print this in different formats too 
for eg:
print(f"My name is {first_name}")
here f represents format also known as formatted string so I can print out with 

mail="erenyegr@icloud.com"
print(f"Here is the mnail id: {mail} of {first_name}")
Output: Here is the mnail id: erenyegr@icloud.com of Ashutosh
in order to be string it should be in quotes ( " " ); otherwise it will be integers

I had some fun with this too...haha :>
#its valentines day and eren got some surprise for his gf Mikasa
girlfriend="Mikasa"
print(f"Happy Valentine's day to my beautiful gal {girlfriend}!")
  Happy Valentine's day to my beautiful gal Mikasa!
#for my beautiful girlfriend I got her a gift
gift= "rose, a kitkat and a teddy bear"
print(f"I got a {gift} for you my love, {girlfriend}!")
  I got a rose, a kitkat and a teddy bear for you my love, Mikasa!
    
#integers
age= 19;
print(f"I'm {age} years old.")
Output:I'm 19 years old. 

employees=9
print(f"During my first job at Praised Media, I used to work with {employees} employees.")
  During my first job at Praised Media, I used to work with 9 employees.
print(f"I was the youngest employee at that time, as I was only {age} years old.")
  I was the youngest employee at that time, as I was only 19 years old.

#float
#after completing my 3 months internship, I left the company and during that 3 months I made around 189.43 dollars.
earned= 189.43
print(f"During 3 months intenship, I earned around {earned} dollars..too low man")
  During 3 months intenship, I earned around 189.43 dollars..too low man

##Boolean values
am_single= True
print(f"Am I single?: {am_single}, I have been single since the day I was born.")
  Am I single?: True, I have been single since the day I was born.

#confession time
crush="Mikasa"
first_name="Eren"
print(f"Bro, I have a crush on {crush} since 2 years, should I confess my feelings to her?")
print(f"Definitely {first_name}, you should confess your feelings to {crush}.")
print(f"Do you think {crush} will accept me?")
will_accept_me= True
if will_accept_me:
    print(f"Yes ofc {first_name} she will accept you, you are a great guy and {crush} is lucky to have you.")
else:
    print(f"No, you are navie for her, {first_name}")
  Bro, I have a crush on Mikasa since 2 years, should I confess my feelings to her?
  Definitely Eren, you should confess your feelings to Mikasa.
  Do you think Mikasa will accept me?
  Yes ofc Eren she will accept you, you are a great guy and Mikasa is lucky to have you.


    
