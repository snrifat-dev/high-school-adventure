print("Welcome to High School Adventure!")
answer = input("You are a new student at XYZ High School. Are you ready to start? (y/n) ")

if answer == 'y':
    score = 0
    print("Great! Let's begin.")
    
    print("Episode 1: New Kid in School")
    answer = input("You meet a group of students during lunch. Do you sit with them? (y/n) ")
    
    if answer == 'y':
        print("You make new friends and feel welcomed in school. +1 point")
        score += 1
    else:
        print("You feel lonely and isolated. -1 point")
        score -= 1
        
    print("Episode 2: First Test")
    answer = input("You have a math test next week. Do you study over the weekend? (y/n) ")
    
    if answer == 'y':
        print("You do well on the test. +1 point")
        score += 1
    else:
        print("You don't do well on the test. -1 point")
        score -= 1
        
    print("Episode 3: Parent-Teacher Conference")
    answer = input("Your parents meet with your math teacher. Do they praise you for your good grades? (y/n) ")
    
    if answer == 'y':
        print("Your parents are proud of you. +1 point")
        score += 1
    else:
        print("Your parents are disappointed in you. -1 point")
        score -= 1
        
    print("Final score:", score)
    
    if score >= 2:
        print("Congratulations! You have successfully completed High School Adventure.")
    else:
        print("Sorry, you didn't make it. Better luck next time!")
    
else:
    print("Maybe next time then. Goodbye!")
