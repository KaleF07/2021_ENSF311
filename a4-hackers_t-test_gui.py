import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

#seaborn variables
sns.set_style('whitegrid')
sns.set_palette('deep')

# Create a couple of colors to use throughout the notebook
red = sns.xkcd_rgb['vermillion']
blue = sns.xkcd_rgb['dark sky blue']


class TtestFrame(ttk.Frame):
    """Tkinter Frame containing widgets that take input and display t-test results
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid(row=2, column=4)
        
        # tk variables
        self.groupA = tk.StringVar()
        self.groupB = tk.StringVar()
        self.p_value = tk.StringVar()

        # matplotlib related variables
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)

        self.makewidgets()
    
    def makewidgets(self):
        """ creates widgets in TtestFrame

        returns: Nothing
        """

        ttk.Label(self, text="Group A").grid(row=2, column=0)
        ttk.Label(self, text="Group B").grid(row=2, column=1)
        
        self.groupA = tk.Text(self, width=20, height=20)
        self.groupA.grid(row=3, column=0)
        self.groupB = tk.Text(self, width=20, height=20)
        self.groupB.grid(row=3, column=1)
        self.groupA.insert('1.0', '84 72 57 46 63 76 99 91')
        self.groupB.insert('1.0', '81 69 74 61 56 87 69 65 66 44 62 69')

        ttk.Button(self, text="t-test", command=self.set_plot).grid(row=0, column=0)

        ttk.Label(self, text="p value").grid(row=0, column=3, sticky=tk.E)
        ttk.Entry(self, text=self.p_value).grid(row=0, column=4, sticky=tk.W)

        # A tk.DrawingArea linked to the Frame and the matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, self)  
        self.canvas.get_tk_widget().grid(column=4, row=3, columnspan=5, sticky=tk.W)
        self.canvas.draw()

        # NavigationToolbar uses pack geometry manager, we cannot mix managers.
        # Workaround is to put toolbar into its own Frame
        toolbar_frame = ttk.Frame(self)
        toolbar_frame.grid(column=0, row=5, columnspan=5, sticky=tk.S+tk.E)
        toolbar = NavigationToolbar2Tk(self.canvas, toolbar_frame)
        toolbar.update()

    def set_plot(self):
        """ Sets tk variables and plots simulated t distribution

        returns: Nothing
        """
        
        try:
            # group text boxes into lists
            groupA = list(map(int, self.groupA.get('1.0', tk.END+'-1c').split()))
            groupB = list(map(int, self.groupB.get('1.0', tk.END+'-1c').split()))

            # Turning list into DataFrame
            df = pd.DataFrame({'star': [], 'measurement': []})
            for i in range(len(groupA)):
                df = df.append({'star': 1, 'measurement': groupA[i]}, ignore_index=True)
            for i in range(len(groupB)):
                df = df.append({'star': 0, 'measurement': groupB[i]}, ignore_index=True)

            label = df['star'].values.copy()
            diff_measured =df[label == 1]['measurement'].mean() - df[label == 0]['measurement'].mean()
            
            # Calculating differences in the two groups
            differences = []
            num_simulations = 10000
            for i in range(num_simulations):
                np.random.shuffle(label)
                group_1_mean = df[label == 1]['measurement'].mean()
                group_0_mean = df[label == 0]['measurement'].mean()
                differences.append(group_1_mean - group_0_mean)
            
            p_value = sum(diff >= diff_measured for diff in differences) / num_simulations
            self.p_value.set(p_value)

            # plotting
            self.ax.clear()
            self.ax.hist(differences, bins=50, color=blue)
            xmin, xmax = self.ax.get_xlim()
            ymin, ymax = self.ax.get_ylim()

            self.ax.plot((diff_measured, diff_measured), (0, ymax), color=red)
            self.ax.annotate('{:3.1f}%'.format(p_value * 100), 
                            xytext=(diff_measured + (xmax-diff_measured)*0.5, ymax//2), 
                            xy=(diff_measured, ymax//2), 
                            multialignment='right',
                            va='center',
                            color=red,
                            size='large',
                            arrowprops={'arrowstyle': '<|-', 
                                        'lw': 2, 
                                        'color': red, 
                                        'shrinkA': 10})
            self.ax.set(xlabel='score difference', ylabel='number')
            self.canvas.draw()
        except Exception as e:
            tk.messagebox.showinfo(type(e), e)

        


root = tk.Tk()
TtestFrame(parent=root)
root.mainloop()