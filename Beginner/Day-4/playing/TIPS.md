The difference between 
```text
choice_images = rock, paper, scissors 
```
and 
```text
choice_images = [rock, paper, scissors] 
```
Is the data type of the variable choice_images.
In choice_images = rock, paper, scissors,  are being assigned to choice_images as separate values. This creates a tuple of 
three strings, where each string corresponds to one of the images.
In choice_images = [rock, paper, scissors] - rock, paper, and scissors are being assigned to choice_images as a list containing the three image strings.
This creates a list of strings, where each string corresponds to one of the images.
If you want to randomly choose one of the images from the list, you can use the second option (choice_images = [rock, paper, scissors]) 
and then use the random.choice() function to randomly select one of the images from the list.