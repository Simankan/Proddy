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
















