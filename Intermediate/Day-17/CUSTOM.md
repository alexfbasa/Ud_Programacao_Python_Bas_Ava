# Upgrade
If you want to increase this app, you can create a new quiz database yourself.
```text
https://opentdb.com/  -- API
```

Take a look at the data.py file and format your new data file with the same format. You can remove the keys and leave it starting from [ ].
e.g:
```text
{
  "response_code": 0,  # TODO - Remove it
  "results":           # TODO - Remove it
   [                   # Start
    {
      "category": "Entertainment: Video Games",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Amazon acquired Twitch in August 2014 for $970 million dollars.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    }
```
Now change the keys on Question constructor - from text to question and from answer to correct_answer.