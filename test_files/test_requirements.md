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
**poll(c1, c2, c3, c4, c5, time, topic):**

    Case 1: Single result #1
        input: $poll 1 2 3 4 5 15s What is your favorite number?
        interaction: reaction 1 is selected by two users
        expected output: 1

    Case 2: Single result #2
        input: $poll 1 2 3 4 5 15s What is your favorite number?
        interaction: reaction 4 is selected by two users
        expected output: 4

    Case 3: Single tie
        input: $poll 1 2 3 4 5 15s What is your favorite number?
        interaction: reaction 1 & 5 are selected by two users
        expected output: 1 5

    Case 4: Multiple ties
        input: $poll 1pm 11am 9am 4pm 6pm 1m When are you free?
        interaction: reaction 3, 4, and 5  are selected by two users
        expected output: 9am 4pm 6pm

    Case 5: Ignore Dashes
        input: $poll Red - Yellow Green - 15s What is your favorite color?
        interaction: reaction 2 & 1 are selected by two users
        expected output: Red

    Case 6: Ignore Dashes & Single Tie
        input: $poll poll Red - Yellow Green - 15s What is your favorite color?
        interaction: reaction 1, 2, and 3 are selected by two users
        expected output: Red Yellow

    Case 7: Ignore Dashes & Multiple Ties
        input: $poll - Orange Yellow Green - 15s What is your favorite color?
        interaction: reaction 1, 2, 3, 4, and 5 are selected by two users
        expected output: Orange Yellow Green
 
--------------------------------------------------------------------------
**remind(time, task)**

    Case 1: Test with time as 's' (second) with generic task
        input: $remind 5s take out trash
        expected output: Started reminder for take out trash and will last 5s.
                         Reminder for take out trash
        
    Case 2: Test with time as 'm' (minute) with generic task
        input: $remind 5m take out trash
        expected output: Started reminder for take out trash and will last 5m.
                         Reminder for take out trash
        
    Case 3: Test with time as 'h' (hour) with generic task
        input: $remind 5h take out trash
        expected output: Started reminder for take out trash and will last 5h.
                         Reminder for take out trash
        
    Case 4: Test with time as 'd' (day) with generic task
        input: $remind 5d take out trash
        expected output: Started reminder for take out trash and will last 5d.
                         Reminder for take out trash
        
    Case 5: Test with time as with invalid time tag and generic task
        input: $remind 5a take out trash
        expected output: You didn't enter the time in correctly
        
    Case 6: Test with time as with negative time and generic task
        input: $remind -5s take out trash
        expected output: You didn't enter the time in correctly
        
    Case 7: Test with time as with no sepcified time (with time tag) and generic task
        input: $remind s take out trash
        expected output: You didn't enter the time in correctly
        
    Case 8: Test with time as with no sepcified time (without time tag) and generic task
        input: $remind take out trash
        expected output: You didn't enter the time in correctly
        
    Case 9: Test with time as with an extremely large time and generic task
        input: $remind 9999999999999999s take out trash
        expected output: Started reminder for take out trash and will last 9999999999999999s.
                         Reminder for take out trash
                         
    Case 10: Test with a valid time but no task inputted
        input: $remind 5s
        expected output: discord.ext.commands.errors.MissingRequiredArgument: task is a required argument that is missing.
    
--------------------------------------------------------------------------


