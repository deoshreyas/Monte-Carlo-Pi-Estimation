# Monte-Carlo-Pi-Estimation

A Python program (with GUI) to estimate the value of $pi$.

## :grey_question: How to use it?
- Clone the repository on your local machine.
- Make sure you have **Python** and **Pygame** installed.
- Run the program. 

**NOTE #1:** You can change the value of *n* in the code. Remember, the higher the value of *n*, the more accurate the estimation. 
**NOTE #2:** You can also change the value of *FRAME_RATE* in the code to speed up (or slow down) the estimation.

## :interrobang: But how does it work
The program uses the Monte Carlo method to calculate the value of $pi$. 

The Monte Carlo method is a type of computational algorithm that relies on random sampling to obtain results. This is a way of using randomness to solves problems, and is different from the traditional deterministic methods.

Here, the window represents a square of side $1 unit$. The radius of the circle is $0.5 unit$. The area of the circle is :
$$pi(r^2) = pi(0.5)^2 = {pi \over 4}$$

The area of the square is $1 unit squared$. Dividing area of the circle by this, we are left with:
$${{pi/4} \over 1} = {pi \over 4}$$

We then generate a large number of uniformly distributed random points and display them. These points can be in any position within the square (or window) i.e. between (0,0) and (1,1). If they fall within the circle, they are coloured red, otherwise they are coloured blue. We record the total number of points $N_{total}$, and the number of points that are inside the circle $N_{inner}$. 

If we divide the number of points within the circle, by the total number of points, we get a value that is approximately equal to the ratio of the areas we calculated above, i.e. $pi \over 4$.

In other words:

$$ {pi \over 4} \approx {N_{inner} \over N_{total}} $$

$$ pi \approx 4{N_{inner} \over N_{total}} $$
## :computer: How to help?
Please feel free to suggest improvements, including but not limited to new operations and GUI updates.

*I have done my best to eradicate all _known_ bugs from the code. However, if you feel you have found a potential bug, please open a pull request.
