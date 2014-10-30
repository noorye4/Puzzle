#Auto Puzzle Reconstruction
The project is to solve reconstruction puzzle problem.
It use ant colony optimization algorithm.

##Example:

input image

![lena](demo/lena.jpg)

Then we split the image 2 * 2 pieces,and random sorted it.

    cd script
    python script-split.py ../image/lena.jpg 2 2
    python script-random.py

in random_output folder
like this

![split](demo/lena_2_2.png)

or

![split](demo/lena_3_3.png)

