# a4-hackers_t-test_gui
Based on an existing Python script, create a graphical user interface to compute a hacker's t-test.


# Problem statement
We would like to compute whether measurements of two groups are different. As an example, we could ask if students that had prior Python experience did better in this course (Group A), than students that are new to Python (Group B). We could use final grade as the measurement and ask *Does the observed difference in mean final grade lie within normal chance variation?* The computation needed is called a [t-test](https://en.wikipedia.org/wiki/Student's_t-test).

While there are formulae and a process to carry out a student t-test, the goal of this assignment to implement a hacker's version as presented in this video [Jake Vanderplas - Statistics for Hackers - PyCon 2016](https://www.youtube.com/watch?v=Iq9DzN6mvYA) (start at ~8min). A github user prepared a [Jupyter notebook](https://github.com/croach/statistics-for-hackers/blob/master/statistics-for-hackers.ipynb) with Python code for what is presented. The relevant code is available in `a4-hackers_t-test.py` with Sneetches data in `sneetches.txt`.

As explained in the video, the hacker's t-test assumes that measurements of Group A and Group B come from the same parent group, i.e. are the same. All measurements are pooled, then, repeatably, measurements are randomly assigned to Group A and Group B. The difference in means between the groups is calculated and stored. The percentage of simulated group differences larger than the original group difference indicates the significance value (p-value). The smaller the p-value, the higher the chances that Group A and Group B are different. A small p-value would warrant further investigation.

You will build a graphical user interface with Python and tkinter that:
1. Uses the object-oriented pattern and grid geometry manager.
2. Provides two text fields, one labeled *Group A*, the other *Group B*, to enter measurements for the two groups.
3. Contains a button to start the simulation with **10'000** iterations, and displaying the resulting p-value in a copy-paste'able widget.
4. Includes a Matplotlib plotting canvas to display the simulated histogram along with measured difference and p-value.
5. Alerts the user with a pop-up message about errors in data conversion when reading values from the text fields.
6. Test your GUI with the Sneetches data available in `sneetches.txt`. 

Optionally, you might consider including:
- Adding a widget to select the number of iterations.
- Add widgets and logic to compare simulation to `statsmodel.t_test`.
- Add a progressbar indicating simulation progress.
- Move the simulation into a thread in order for the GUI not to block.
- Extend the t-test from handling only 'larger' to handling 'larger', 'smaller' and 'two-sided' alternatives.

# What to do
Watch the video [Jake Vanderplas - Statistics for Hackers - PyCon 2016](https://www.youtube.com/watch?v=Iq9DzN6mvYA) (start at ~8min). Study the code in `a4-hackers_t-test.py`.

Design and implement a graphical user interface with the mandatory elements 1. - 6. outlined above. The idea is to re-use the code from `a4-hackers_t-test.py`. Save your GUI code in the file `a4-hackers_t-test_gui.py`. A possible implementation could look like this:

![Screenshot of example GUI](hackers_t-test_gui_screenshot.png)

Follow the [Style Guide](StyleGuide.md), and use git and github to track your changes.

Edit `README.md` (this file) and include instructions on how to run your program and expected outputs (screenshots) in the _How to run this program_ section below. Make sure to describe how the data needs to be formatted, e.g. one measurement per line, space separated, etc. Use the Sneetches data in `sneetches.txt` as test data. 

Make sure final version of your code `a4-hackers_t-test_gui.py` and updated `README.md` with referenced files (screenshots etc.) are committed to git and pushed to github. 

# How to run this program
To start this program, simply start running it. Upon running, a GUI will appear to interact with. This GUI holds a graph to show t-test measured, two text boxes that hold the data being measured, the p value measured, and a button to complete the t-test. The program initially runs with data collected from `sneetches.txt`, but you can edit and change the values to whatever you want as long as their space separated numbers. Once you have the values you want to compute in the text boxes of group A and B, press the button t-test. Once you press it, the following graph will show up, along with a copy and pastable p value:
![Example screenshot of GUI](example_screenshot.png)

If you happen to input anything other than space separated numbers, an error pop-up shows with an error message, such as the following:
![Example of failed t-test](failed_test.png)

# Summary

I thought this assignment was very helpful in learning how to effectively display data in a GUI. It was very nice to be able to visually see the code I put in turn into a system that I can look at and tweak how I see fit. Going forward, I think this assignment can better help me when I choose to write programs in the future that require visual components so that I can better write effective code. I think the assignment overall was a bit challenging when trying to figure out how all the different components work together to create a final product, but once I was able to piece it together, it was satisfying to finally see it work.

