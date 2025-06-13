# Picture Taker
- Picture Taker is a simple Python script for taking pictures with OpenCV and a connected camera. The script makes it easy to collect images for training a machine learning vision model.

## Requirements
- To use Picture Taker, you need to install OpenCV-Python.
- You'll also need to have a camera (such as a USB webcam) connected to your system.

## Usage for Windows user
- First, download my repository [Link](https://github.com/kaizen-2004/OpenCV_Image_Capturing/archive/refs/heads/main.zip) to a convenient location on your computer. Navigate to the location of the downloaded zip and extract it.
- If Python is not installed, navigate to this [Link](https://www.python.org/downloads/windows/) to download Python on your system.
	- Run the installer
	- IMPORTANT: Check the box that says **“Add Python to PATH”**
	- Click **Install Now**
	- Run this in Command Prompt to verify the installation
	```bash
	python --version
	```
- After downloading my repository and installing the Python (if not installed) navigate to the folder and open command prompt there.  To navigate to Command Prompt on the folder, just type "cmd" on the address bar
 ![[Pasted image 20250613083758.png]]
- Like this and hit "Enter"
![[Pasted image 20250613083829.png]]
- Activate the Virtual Environment by running this on the Command Prompt
```bash
venv\Scripts\activate
```
- You will see:
```bash
(venv) C:\Your\Path>
```
- Then run
```python
pip install -r requirements.txt
```
- Wait for the installation and Run the Script
```Python
python main.py
```



A window will open showing the camera's view. Press `p` on the keyboard to take a picture. The first picture will be saved in a folder called "image" as filename `image_1.jpg`. If the "image" folder doesn't exist, it will be created automatically. Continue pressing `p` to take more pictures. Each additional picture will be saved as `image_2.jpg`, `image_3.jpg`, and so on. Press `q` to quit.

If `image_1.jpg` already exists in the iamge folder, the program will automatically increase the picture number until it reaches a filename that doesn't exist. (For example, if `image_1.jpg` through `image_20.jpg` already exist in the "image" folder, the program will start with `image_21.jpg` for the first saved picture.) This way, you can take pictures without having to worry about overwriting existing pictures.

### Command Arguments
By default, the script runs at a resolution of 1920x1080, saves pictures in a folder called "image", and uses "image" as the base filename for the pictures. The defaults can be changed using the following command arguments:
* `--res` : specify the camera resolution in WxH to change the resolution
* `--imgdir` : specify the folder to save pictures in (and to use as the base filename for the pictures)

For example, to take pictures at a 1920x1080 resolution and save them in a folder called "Items", issue the following command:

```python main.py --res=1920x1080 --imgdir=Items```
