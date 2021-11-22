**poll(c1, c2, c3, c4, c5, time, topic):**
--------------------------------------------------------------------------
    Case 1: Single result #1
        input: $poll 1 2 3 4 5 15s What is your favorite number?
        interaction: reaction 1 is selected by two users
        expected output: 1
--------------------------------------------------------------------------
    Case 2: Single result #2
        input: $poll 1 2 3 4 5 15s What is your favorite number?
        interaction: reaction 4 is selected by two users
        expected output: 4
--------------------------------------------------------------------------
    Case 3: Single tie
        input: $poll 1 2 3 4 5 15s What is your favorite number?
        interaction: reaction 1 & 5 are selected by two users
        expected output: 1 5
--------------------------------------------------------------------------
    Case 4: Multiple ties
        input: $poll 1pm 11am 9am 4pm 6pm 1m When are you free?
        interaction: reaction 3, 4, and 5  are selected by two users
        expected output: 9am 4pm 6pm
--------------------------------------------------------------------------
    Case 5: Ignore Dashes
        input: $poll Red - Yellow Green - 15s What is your favorite color?
        interaction: reaction 2 is selected by two users
        expected output: 
--------------------------------------------------------------------------
    Case 6: Ignore Dashes & Single Tie
        input: $poll poll Red - Yellow Green - 15s What is your favorite color?
        interaction: reaction 1, 2, and 3 are selected by two users
        expected output: Red Yellow
--------------------------------------------------------------------------
    Case 7: Ignore Dashes & Multiple Ties
        input: $poll - Orange Yellow Green - 15s What is your favorite color?
        interaction: reaction 1, 2, 3, 4, and 5 are selected by two users
        expected output: Orange Yellow Green
