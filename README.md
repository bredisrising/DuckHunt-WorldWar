# DuckHunt-WorldWar 
by Ankit, Nathan, Alex and Robert

Overview of the project:

This game is based on the popular 80's game "Duck Hunt" but with a twist: the duck (or birds) shoot back at the player!
This turns the game into more of a First Person Shooter where they can move left and right and duck under cover. Another fun twist is the way you aim:
Either you can use the mouse or use the computer's camera to track a makeshift controller that the player can use to aim and shoot in real life. 

In terms of design, we wanted to keep the 8-bit art style of the original game. The original game layout consists of a background, a middleground bush the enemy comes out of and a 
foreground bush that the player is behind. In our game, we made 3 maps: Africa, Australia and America. Each of the maps had their own respective background, middleground and 
foreground. Another thing we wanted was a simple and easy UI, with a similar style in button design with the 8-bit style of the game. After the completion of each level, there is 
a success screen, and we wanted that to break up the pace of the game as well as add to the user experience. The player aspect of the design (crosshair, weapon, etc) is not as 
similar to the base game. We wanted to improve one aspect of the game - ours has a crosshair which allows the player to aim and fire, making it easier to play the game. Finally, 
to add some sense of difficulty, we added a reload time, shown by the green circle around the crosshair and also, the enemy shooting which is shown by the red circle shrinking 
down on its target over time.

Instructions for running the game:

In VS Code, go into the terminal and pip install the following: pygame, numpy, opencv-python, scipy

Make sure the user has a camera and it is not covered or in a badly lit area as that is how the game tracks the controller. 
Make sure there is a functional mouse, whether that be a physical mouse or a track pad.
To run the game, run the "main.py" file in the "main" folder 

Architecture:

For the interactions, the biggest ones can be seen in the image below; that shows how all the major classes and abstract classes interact in the tightly wound system. 

![Image](StructureDiagram.png)

For the smaller interactions, they'll be described here: to start, the main.py calls game.py which is the whole management system of the game. For that, each level is made into its own class, which is then imported 
and put into a list which the game moves through. For the levels that have buttons, each button is a piece of the button.py class. Each button is designed with a function, some of which actually have the ability to 
+1 or -1 in the level list. Every single image you see in the game, is a child of the ImageObject class, which takes the image and gives it certain attributes that we can work with and manipulate. 


For the gun tracking, the system scans a QR code on the gun through the camera. From there, the relative location of the gun is mirrored onto the screen and acts as a cursor. 

![Controller Schematic](https://github.com/bredisrising/DuckHunt-WorldWar/assets/90003108/ddfb6980-b368-4aaf-b1db-426ff7c3f37b)

The gun is tracked in the PhysicalGunDetection.py file, and it distributes information to the rest of the game through it, since it is running the whole time. In the levels with enemies, the level itself handles the tracking of the enemy, the cursor and the health of the enemy. 

For the majority of the Modules, we made an abstract class that outlined the basic form. For example, the level.py and enemy.py file are abstract classes that are implemented into each level or enemy respectively. We 
did this to reduce the redundancy of coding and make the coding process as a whole more efficient. Another choice made was the game management system. There is a main.py class that is the main game and the game.py 
class that allows us to easily manage the game and the levels in a simple way. Finally, in our globals.py class, we made all the "things" we would need to use multiple times, such as images and variables in one class.
This allowed for ease of importing when creating new levels and enemies.
Below is a sturcture diagram of the code:


The APIs of the system:
As mentioned above, we have several different module and classes in our game, each having a plethora of different features, methods, and attributes. Since these modules are each very complex, understanding each and 
every module would be too hard for each group member to accomplish, so we ended up abstracting all the useful features and the main "job" of the module into a single function called update(each major module like the 
enemy, player, and game class has this function). When the update method of a module is called, like the update method on the enemy, it does the main job of the module (for example with the enemy, it moves the enemy 
around and shoots the player) without the user having to understand what is happening in the background. This is the main API method that is used throughout our program, which is used a lot when we are integrating 
together several modules. For example, in our game class, where we integrate several major modules like the enemy, player, level, and button modules together, we are able to do so by just calling the respective update
methods of these external modules, which gets them to do their main task job within the game task, smoothly integrating all these together. Below is a description of the update class for each major module. 

AI class update(): moves the enemy to a given point based on its current state
Enemy class update(): tracks enemy health, interactions with player, and shoots the player
Button class update(): handles mouse clicks, toggles, and events after the mouse is clicked/toggled
Player + Player Gun class update(): fires the weapon and handles reloading
Game class update(): pretty much calls the update to each and every major module, and handles moving from level to level. 
In conclusion, using these different update method of these major modules, we abstract the main tasks of each module of this function, which we can then call in other modules to integrate them together. 

User Experience:

The User will launch the game and be put on a screen with clearly highlighted "Play" and "Options" buttons. If the user pushes the Options button, they are met with a screen that has a toggle switch to "use mouse" 
(set to on by default).
The user also will see a tracking demo screen for the controller, which when pressed, will open a screen and show the user what is being tracked by the camera for their understanding. Upon pressing "Play" they are 
greeted with a loading screen and then a screen that shows them the key bindings for the game (AWSD, SPACE or Left Click) and their respective actions. From there, the user will be placed on the first level, with a 
crosshair on their screen, implying that you can now attack the first enemy. Through the use of the key binding screen, they will know how everything works before they start the game. In order to use the controller, 
the user must demo it first, ensurting that they know how to use it (assuming they know pulling a trigger means "shoot"). 

For the experienced player, the game is still challenging. The AI of the enemies is tricky to predict and after hours of testing, each level still poses some challenge to the game. Because the hit marker system is in
use, it is super satisfying to hit a shot, and even more satisfying with a headshot, that even the experienced player can come back and have a different experience each time they play the game. Additionally, the game 
uses sound effects and music to make each level more fun and increase the intensity. Each level is paired with some intense music to amp the user up and each time the in game weapon is fired, the user can hear the
satisfying sound of a hunting rifle shot.

The user will want to come back because of a few reasons. One being that each time the code is ran, the experience will be new. The AI movement is extremely hard to predict and further, the enemy shots are even more 
random. This aspect of randomness brings a new game entirely to the user each time they play the game - no two experiences will be the same. Another reason is because of the different play modes: One is the typical 
keyboard and mouse, but the other is the controller mode. This mode is fun because it brings a reality aspect where the user will actually need to know how to aim to hit their shots. And with that, the hit markers 
become even more satisfying when the user is able to finally track and shoot the enemy.


Retrospective:

Overall, the process for writing this app was great, as we were able to get a finished game, despite it not being what we imagined it to be at the beginning of the project. We had a very solid structure that took 
several evolutions and made designing levels and everything on it very efficient and easy to do; our artwork was great and added a really nice touch to the game; and our tracking system and the tracker that we 
designed worked very well (adding a fun element to the game), and we were able to optimize it to run the game at good fps levels universally.

However, despite this, our communication as a group could be improved upon. Looking on the good side, we would have very good stand ups with very concise and meaningful progress checks on how we were doing on our 
respective tasks; discuss issues in code and ways to fix them; and assign tasks for the day. Furthermore, during work time, we would explain our code structure and logic to other group members so we could integrate 
our code, and we would collaboratively debug and design various parts of our code. 
But, when we were out of class, we would rarely communicate with each other, and we would kind of do our own things without really talking with anyone else in the group. To fix this in future projects, we could have 
designated specific times over the weekends to call and discuss, send progress reports in the group chat we created, or utilize GitHub Tasks more often as we rarely used it to divvy out work and discuss problems. 

The only major surprise that our group faced was the fact that we might not be able to finish our planned game by the project deadline. We had a brilliant idea of the game which we still stayed true to but due to our 
own time management, some of the aspects had to be cut down to save time. However, this did not throw us off too much as we met as a group and decided 
on ways to downsize our project (removing enemies, levels, and special gun features) to create a more manageable game to finish on time. Other than this, there weren’t any big roadblocks. Of course, there were 
typical code issues and optimization problems (some of which required us to redesign classes and structure to improve modularity and efficiency), but we were able to fix most of these issues without much problem, and 
none of them required us to redesign actual parts of our game. 

The one thing that our group should have done differently is coming up with the structure of the game at the beginning of the project. At the beginning of the project, we never really discussed the structure of the
code, and we all did our own experimenting with the game with our own branches. After we did all our experimenting, we never really had a defined structure, so we had all this code, and we didn’t know how we wanted
to put it together. This created a lot of confusion, and once we did figure out our structure, we had to spend a lot of precious time rewriting our code to integrate it within the structure which wasted a lot of 
time. Therefore, I think it would be beneficial to create our architecture at the beginning of the project and then work directly in it, which saves us time.  
