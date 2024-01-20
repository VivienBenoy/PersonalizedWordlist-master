# PersonalizedWordlist
This program helps you generate personalized wordlist by answering some of the question about the person you wanna generate wordlist for. (Inspired by Mr Robot)
**This Program is only made for Educational Purposes**

Note: The Number of Keywords Generated is directly propotional to the Input given by User

This program helps you generate a keyword by using certain key inputs that you need to provide to the program. The program asks you for certain basic inputs such as Victims name, address, organization, date of birth, age, fathers and mothers name, nationality. These basic inputs are mainly what people use as their passwords but that's not all, in this program we also ask inputs like victims phone number, pet name, old address, his/her inspiration, name of girlfriend or wife, etc. The program also askes for victims old passcode to understand the combination and things like whether the victim uses nicknames or any other hidden detail useful. These random information are used as inputs to generate passwords.


-->How does this program work?
The logic behind this program is as follows:

(1) We filter out all the null variables and collect all the filled up inputs and if the basic information are not entered we shall not proceed the program,

(2) We create functions for combinations by replacing name and other inputs with non sorted variable,

(3) We run all the loops with filter variables to get all possible outcomes with the inputs entered as well as other useful inputs entered by the program itself such as 123 at the end of passcodes or at intervals,

(4) The program make a txt file of all the possibilities and saves it by the name of "victim_namepass.txt",

(5) Another txt file is made that save all the inputs made by the Script for future purposes

(6) After the txt file of all random passcodes is made, suitable programs can be used for further hacking by brute force.
 
 -->How to use?
 
 (1)Make sure you have python3 installed
 
 (2)Run the Installation.py file by typing python Installation.py in cmd/shell
 
 (3)Run Main.py file by typing python Main.py in cmd/shell 
 Enjoy!
