--------------------------------------------------------------------------
**on_ready()**

    Case 1: Test for after starting the bot
        input: start bot
        expected output: We have logged in as Proddy#5290
    
--------------------------------------------------------------------------
**about()**

    Case 1: Test for $about with no other inputs
        input: $about
        expected output: Hello! My name is Proddy I have 3 core features:
            1. Introduction message: This feature allows the user to personalize an introduction message to new users.    
               Use the command below and replace [user] with the target user and [message] with your message. There are two version of message command you can use.
               $message [user]
               $message_custom [user] [message]
               I.E. $message @uriel
               I.E. $message @uriel hello, my name is Uriel. Welcome to the team!

            2. Polling/voting: This feature allows the users to create polls and vote.    
               Use the command below and replace [choice#] with your choices, 5 choices max. If you only want to use 1 choice, use dashes for the rest of the choices.After         inputting all 5 choices/dashes, input the time, in seconds, you want the poll to run for.
               $poll [choice1] [choice2] [choice3] [choice4] [choice5] [time] [prompt]
               I.E. $poll 1pm 2pm - - - 60 What time would you like?

            3. Reminder: This feature allows the users to create a reminder and would alert the users upon the desired time.    
               Use the commmand below and replace [time] and [task] with your inputs. [time] must in the format of a number follow by the either second (s), minute (m), hour (h), or day (d)
               $remind [time] [task]
               I.E. $remind 10m take out trash
           
    Case 2: Test for $about with additional random input
        input: $about feature
        expected output: Hello! My name is Proddy I have 3 core features:
            1. Introduction message: This feature allows the user to personalize an introduction message to new users.    
               Use the command below and replace [user] with the target user and [message] with your message. There are two version of message command you can use.
               $message [user]
               $message_custom [user] [message]
               I.E. $message @uriel
               I.E. $message @uriel hello, my name is Uriel. Welcome to the team!

            2. Polling/voting: This feature allows the users to create polls and vote.    
               Use the command below and replace [choice#] with your choices, 5 choices max. If you only want to use 1 choice, use dashes for the rest of the choices.After         inputting all 5 choices/dashes, input the time, in seconds, you want the poll to run for.
               $poll [choice1] [choice2] [choice3] [choice4] [choice5] [time] [prompt]
               I.E. $poll 1pm 2pm - - - 60 What time would you like?

            3. Reminder: This feature allows the users to create a reminder and would alert the users upon the desired time.    
               Use the commmand below and replace [time] and [task] with your inputs. [time] must in the format of a number follow by the either second (s), minute (m), hour (h), or day (d)
               $remind [time] [task]
               I.E. $remind 10m take out trash

--------------------------------------------------------------------------
**message(user)**

    Case 1: Test for sending a message to '@chris' where '@chris' is a user that EXISTS in the Discord server
        input: $message @chris
        expected output: Welcome, @chris to Team 6 DL5!
            We are so excited to have you with us and look forward to working with you!
            Your server role will be assigned automatically. Please let anyone know if you have any questions.
 
    Case 2: Test for sending a message to '@abc' where '@abc' is a user that DOES NOT exist in the Discord server
        input: $message @abc
        expected output: discord.ext.commands.errors.UserNotFound: User "@abc" not found.

    Case 3: Test for sending a message to 'chris' without the '@' symbol
        input: $message chris
        expected output: discord.ext.commands.errors.UserNotFound: User "chris" not found.

--------------------------------------------------------------------------
**message_custom(user, message)**

    Case 1: Test to check if message was sent to '@chris' where '@chris' is a user that EXISTS in the Discord server
        input: $message_custom @chris Welcome to the team, Chris!
        expected output: Welcome to the team, Chris!
 
    Case 2: Test to check if message was sent to '@abc' where '@abc' is a user that DOES NOT exist in the Discord server
        input: $message_custom @abc Welcome to the team, abc!
        expected output: discord.ext.commands.errors.UserNotFound: User "@abc" not found.
        
    Case 3: Test to check if message was sent to 'chris' without the '@' symbol
        input: $message_custom chris Welcome to the team, abc!
        expected output: discord.ext.commands.errors.UserNotFound: User "chris" not found.
        
 --------------------------------------------------------------------------
        
        
        
        
        
        
        
        
        
        
        
        
        







