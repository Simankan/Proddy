--------------------------------------------------------------------------
on_ready()
Case 1:
    input: start bot
    expected output: We have logged in as Proddy#5290
    
--------------------------------------------------------------------------
about()
Case 1:
    input: $about
    expected output: Hello! My name is Proddy I have 3 core features:
        1. Introduction message: This feature allows the user to personalize an introduction message to new users.    
           Use the command below and replace [user] with the target user and [message] with your message. There are two version of message command you can use.
           $message [\user]\
           $message_custom [\user]\ [\message]\
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
           
Case 2:
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

Case 3:
    input: $about abc
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