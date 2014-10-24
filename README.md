#Auto Puzzle Reconstruction
The project is to solve reconstruction puzzle problem.
It use ant colony optimization algorithm.

##Example:

input image

![lena](image/lena.jpg)

Then we split the image 2 * 2 pieces,and random sorted it.

    cd script  
    python script-split.py ../image/lena.jpg 2 2
    python script-random.py

![split](demo/split.jpg)


like this:  

![split](demo/comb.jpg)