**poll(c1, c2, c3, c4, c5, time, topic):**
--------------------------------------------------------------------------
    Case 1: Single result #1
        input: $poll 1 2 3 4 5 15s What is your faovrite number?
        interaction: reaction 1 is selected by two users
        expected output: 1
--------------------------------------------------------------------------
    Case 2: Single result #2
        input: $poll 1 2 3 4 5 15s What is your faovrite number?
        interaction: reaction 1 is selected by two users
        expected output: 1
--------------------------------------------------------------------------
    Case 3: Single tie
        input: $poll 1 2 3 4 5 15s What is your faovrite number?
        interaction: reaction 1 is selected by two users
        expected output: 1    
--------------------------------------------------------------------------
    Case 4: Multiple ties
        input: $poll 1 2 3 4 5 15s What is your faovrite number?
        interaction: reaction 1 is selected by two users
        expected output: 1    
--------------------------------------------------------------------------
    Case 5: Ignore Dashes
        input: $poll 1 2 3 4 5 15s What is your faovrite number?
        interaction: reaction 1 is selected by two users
        expected output: 1    
--------------------------------------------------------------------------
    Case 6: Ignore Dashes & Single Tie
        input: $poll 1 2 3 4 5 15s What is your faovrite number?
        interaction: reaction 1 is selected by two users
        expected output: 1   
--------------------------------------------------------------------------
    Case 7: Ignore Dashes & Multiple Ties
        input: $poll 1 2 3 4 5 15s What is your faovrite number?
        interaction: reaction 1 is selected by two users
        expected output: 1    
--------------------------------------------------------------------------
