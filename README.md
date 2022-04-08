<!-- Project Title -->
# ![cv-ball-tracking-game](https://user-images.githubusercontent.com/95453430/161440799-106b786a-70ec-4dd1-b87f-53232e0b4e32.svg)

<!-- Project Images -->
![Main Project Image](https://user-images.githubusercontent.com/95453430/162502552-b5c57946-f457-4bcc-8fff-62fb372bbdc8.png)

![GameMainMenu](https://user-images.githubusercontent.com/95453430/161451448-f93d9f67-8726-4fb0-b03c-e0d341833a3b.png)

![GamePlayScreen](https://user-images.githubusercontent.com/95453430/161451492-6c939b7b-090e-49b6-88aa-bb9e68d91c90.png)

<!-- Project Description -->
# ![project-description (11)](https://user-images.githubusercontent.com/95453430/161440805-8d37a946-8b44-46e3-a7a5-6b785e5fcce3.svg)

The **CV Ball Tracking Game** is a **Computer Vision** project in which the user is able to control the **ball in-game** using a **Red Colored Ball** where the image data is fed through their Webcam/Camera. The game is made using **Unity** and scripts handling the recieving of data and logics were all were written in **C#**. The **Python Script** and the **Unity Game** communicated through a **UDP connection**. The screen coordinates of the ball are extracted using **OpenCV** through the custom **HSVColorDetector module**. This data is then encoded and sent from the **Python Script** using the **socket** library to the game which is then received by a **C#** script which decodes it, and is used by the other logical **C#** scripts to update the ball's position on the game screen.

<!-- Project Tech-Stack -->
# ![technologies-used (11)](https://user-images.githubusercontent.com/95453430/161440810-a43d9988-a19b-4c9d-a595-5f096f127d05.svg)

![C#](https://img.shields.io/badge/c%20Sharp-%2300599C.svg?style=for-the-badge&logo=csharp&logoColor=99CC00)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Python Socket](https://img.shields.io/badge/socket-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Unity](https://img.shields.io/badge/unity-000000?style=for-the-badge&logo=unity&logoColor=FFFFFF)

<!-- How To Use Project -->
# ![how-to-use-project (6)](https://user-images.githubusercontent.com/95453430/161440811-26edcf11-1238-4348-8ecb-065a18f860ce.svg)

**Download & Install Unity hub:**
https://unity3d.com/get-unity/download

**Download & Install Unity Editor 2020.30f1:**
https://unity3d.com/unity/whats-new/2020.3.0

**Download the CV Ball Tracking Game Unity Folder and place it in a new folder called Unity in the root directory:**
https://www.mediafire.com/folder/56ctovga52bwc/CV_Ball_Tracking_Game

**Install the LeanTween asset for Unity from the asset store:**
https://assetstore.unity.com/packages/tools/animation/leantween-3595

**Install the following Python libraries in your Virtual Environment using PIP**.

*Note: The library names are **CASE-SENSITIVE** for PIP installations below. Make sure your type them correctly.*

*Install OpenCV for Python*
```Python
pip install opencv-python
```

*Install Numpy for Python*
```Python
pip install numpy
```
Download a copy of this repository onto your local machine and extract it into a suitable folder.
- Create a Virtual Environment in that folder.
- Install all the required Python libraries mentioned above.
- Install Unity Hub & Unity Editor using the links above.
- After the previous step, download the CV Ball Tracking Game folder from the MediaFire link provided above and place it into a new folder called Unity in the root directory.
- Select the **CV Ball Tracking Game** folder to open in Unity Editor.
- Install the LeanTween asset from the asset store from the link above.
- Open a Command Prompt/Terminal in the **Root Directory** of the Project.
- Type the following command in the terminal to run the Python script.
```Python
python CVBallTrackingGame.py
```
- Simultaneously, click on the run button in the opened Unity project.
- get a red ball to use in the game.

- Enjoying playing the game!
