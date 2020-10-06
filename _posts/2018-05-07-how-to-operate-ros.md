---
layout: article
title: "How to Operate Robot Operating System (ROS)"
tags: 
    - Instructions
    - Linux
permalink: operate_ros.html
---

Operating ROS on your Linux can sometimes be a lot to begin with. This is a quick reminder as a tutorial in order to remind you how to operate ROS on your Terminal in Linux

# IP Addresses

First off, you need to figure out what is the IP Address of your robot, whenever trying to connect wirelessly. This will allow you to get the number which you will use it to connect to the robot later on, and vice-versa. To find it,

1. Connect robot to a keyboard
1. Connect robot to a display

Now, in the Terminal of your Burger Robot, type in
```
[TurtleBot External]
$ ifconfig
```

Under the section `wlanO`, you will see the IP Address in `inet addr`:
```
[TurtleBot External]
$ ifconfig
...
wlan0     
inet addr: 222.22.222.22
...
```

**Things to know about IP Address**
 - Your IP Address may change every time you log into a different network, or if you restart your computer
	- The IP Address of your robot may change every time you turn it on/off. *However*, it can sometimes stay the same for weeks. Therefore, it's always good to double-check the IP of your robot

Now, in your computer, you need to get your own IP address. Repeating the same process as before, run `ifconfig`, but this time, it will be under the section `wlp7s0`

```
[Terminal 1]
$ ifconfig
...
wlp7s0 inet addr: 111.111.11.111
...
```

So by now, we have two IP addresses!
1. Computer's IP Address: `111.111.11.111}`
1. Robots's IP Address: `222.22.222.22`

**Save these. We'll need them for the next part!**

# Starting Up ROS Core
Alright! Now, we have files that act as "Settings File" for your computer and for your robot: `bashrc`. We need to edit them to say which IP Addresses we want to use! For here, we can either use `gedit` or `nano` to edit these bad boys.

In your own computer's Terminal, enter the following
```
[Terminal 1]
$ gedit ~/.bashrc
```

This will open a gedit window! (Gedit is essentially a text editor!) When you scroll down down down, you'll see two lines, where you should be putting your PC's IP Address. In the `ROS_MASTER_URI`, leave the last numbers alone (e.g. `:11311`. In the end, you'll have

`ROS_MASTER_URI=http://111.111.11.111:11311`  
`export ROS_HOSTNAME=111.111.11.111`

To make these changes effective, you NEED to source that file!
```
[Terminal 1]
$ source ~/.bashrc
```

Before we get to the juicy part, you need to start up **ROS Core**. You can think of this as *initializing a platform where you can build ROS-related thing on!*

```
[Terminal 1]
$ cd ~/catkin_ws
$ roscore
```

*Now, Terminal 1 will have to remain open and untouched to keep running ROS Core!*  
**Yay! Now we have _ROS Core_ running, and now we can start to activate things!**


# Connect to Robot
Now it's time to connect your computer to the robot! To do so, we first need to set up your Turtlebot to be able to talk to your computer! By the end of this, you'll be able to *control your robot from your computer*

Open up a new Terminal, and put the following command with your Turtlebot's IP Address

```
[Terminal 2]
$ ssh burger@222.22.222.222}
```

Here, it will ask if you're sure you want to connect (Say Yes `y`), and it may ask for the password. The password is `burger`. Once this step is done, the name of the Terminal windown will no longer be the `[Terminal 2]`, but this time, it will be a variant of
`burger@222.22.222.222`. We'll call it `[TurtleBot]` from now on.

Then, now we gotta edit the `bashrc` file once again!
 ```
[TurtleBot 1]
$ sudo nano ~/.bashrc
```


In the \texttt{bashrc} file, edit the lines such that the `ROS_MASTER_URI` is your `PC's IP Address`, and the `ROS_HOSTNAME` is the `Robot's IP Address`

```
export ROS_MASTER_URI=http://111.111.11.111:11311
export ROS_HOSTNAME=222.22.222.22
```


Once again, you need to source your file in order to make the effects!

 ```
[TurtleBot 1]  
$ source ~/.bashrc
 ```

**Now you should be able to run operations on your robot from your computer!**


# Bring Up
Now, in order for you to send commands to your robot, *you need to wake it up!* The term used for this case is *bring up*!  
To *bring up* your robot, run the following command from a remote terminal:

```
[TurtleBot 1]
$ roslaunch turtlebot3_bringup turtlebo#    t3_robot.launch#
 ```



# Teleoperation
One thing you can do is to control the robot by using your keyboard, a Wiimote, an Xbox360 controller, or a PS4 controller! Here we'll cover how to get to use your *keyboard to operate your TurtleBot*

After you've brought up your robot, you can run the following command. First make sure to source it

```
[Terminal 2]
$ source ~/catkin_ws/devel/setup.bash
```

Then run the command
```
[Terminal 2]  
$ roslaunch turtlebot3_teleop turtlebot3_#  teleop_key.launch#
```

# Camera

You can often times want to use the camera. Here is how you can turn on your camera, and how to set it up.
```
[Turtlebot}}  
$ cd ~/catkin_ws/src/raspicam_node#  
$ cd ~/src/launch#  
$ ls#  
camerav2_1280x960.launch  
camerav2_640x480.launch  
camerav2_320x240.launch
 ```

From here, if you want to create a new setting, you can use touch# and edit with nano#

```
[Turtlebot}}  
$ touch newfilename.launch
$ sudo nano newfile.launch
 ```

Here you can set your settings to different **resolution and frame rates**. Finally to start the camera,

```
 [Turtlebot]
	\verb@$ roslaunch raspicam_node newfile.launch @
````

# Create a New Package
Often times, when creating a new project, you might need to create a new package! Sometimes, that package might have some `dependencies`! To create a new package that has dependencies (e.g. `dep1 dep2 dep3`

```
[Terminal]
$ catkin_create_pkg package_name dep1 dep2 dep3}
```


# Nodes and Topics
Alright! Usually you'll want to get information from the robot, send information back to the robot, etc. With that, you'll `nodes` and `topics`.

{Nodes} are the "centers" where operations happen. They acquire values (e.g. distance from sensor) and hold on to them!
	- **Topics** are the medium/messages that send those variables through.


You will need these commands in order to know *what* to pull out the topics. To get information about a topic, you run the command

```
[Terminal]
$ rostopic info topic\_name  
Type: /topic
```


From here, it says that your *Package Name* is *package\_name* and your **Topic Name** is topic. This information allows you to move forward to get the *type of variables* that you'll pull out later. To `show` the information about that `topic`, you run the following command

```
[Terminal]
$ rosmsg show package_name/topic
```

 And this will list you a lot of information about your topic. You'll then need to figure out what and how to pull out of this topic

 ### Example
As an example, if you are interested in the **odometry** of your robot,

```
Terminal
$ rostopic info #
```

Press Tab + Tab

```
[Terminal]
$ rostopic info #  
...#  
blabla  
bleble  
odom  
bloblo  
...#
```

```
[Terminal]
$ rostopic info odom  
Type: nav_msgs/Odometry
```

Here, your package that is being used is $nav_msgs$. So to get info about the topic `Odometry` in the package `nav_msgs`, you write the following, and it will show a lot of lines.

```
[Terminal]
$ rosmsg show nav_msgs/Odometry
...  
...  
...
```


In this case, this field is more or less organized as  
%\begin{center}
%\begin{tabular}{|c|}
%	\hline
%	Pose  
%	\hline
%\end{tabular}
%\end{center}

msgs
\begin{itemize}[noitemsep,nolistsep]
	\item pose \begin{itemize}[noitemsep,nolistsep]
		\item pose\begin{itemize}[noitemsep,nolistsep]
			\item position \begin{itemize}[noitemsep,nolistsep]
				\item x
				\item y
				\item z
			\end{itemize}
		\end{itemize}
	\end{itemize}
\end{itemize}

Now, you'll have to store `pose.pose.position.x` if you want the x position, and `pose.pose.position.y` if you want the y position.

# Saving and Running Scripts

You have the option to either write scripts in C++ or in Python. You will then save the .py or .cpp files in the \texttt{package\_name/src/} folder and on Terminal, you can run, when in the directory


Python
```
$ chmod +x myScript.py  
$ python myScript.py
	OR  
$ python3 myScript.py   
```

# Running Simulation

To run a simulation, you might need to do a couple of extra steps.

## Main Steps
You might need to install some dependent packages for TurtleBot3 Simulation, which could be accomplished with

```
[Terminal]
$ cd ~/catkin_ws/src
$ git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
$ cd ~/catkin_ws && catkin_make
```

First off, the first thing you'll need is to type
```
[Terminal]
$ export TURTLEBOT3_MODEL=burger#  
```

on every Terminal you open OR you can put that into your `~/.bashrc` file. The file `.bashrc` always opens on boot up, so by putting it into the `.bashrc` file allows you not to have to repeat it everytime.

Second, but very important is that you will need to source the following file:
 ```
[Terminal]
$ source ~/catkin_ws/devel/setup.bash#
 ```

This step is really important, and you will need to repeat it with every new Terminal.
Finally, you can run some simulations. Here are some examples

```
[Terminal]
$ roslaunch turtlebot3_fake turtlebot3_fake.launch
```
```
Terminal  
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```
```
[Terminal]  
$ roslaunch turtlebot3_gazebo turtlebot3_world.launch
```
## Errors
When running it, there's a chance you may get errors like `exit code 255`. To solve this, you might have to kill some background processes that were still running
```
[Terminal]  
$ killall gzserver#
$ killall gzclient#
```
