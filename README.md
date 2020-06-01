# Tweepy-Scripts
**Neil Kyne**

### About the project
Just a couple of python scripts using tweepy to access the Twitter API. They were made to allow for easy management of an account, such as to unfollow in bulk, or delete old tweets etc.

### Environment setup
See the requirements.txt file in order to see the full list of packages and their versions I had installed while develooping the project. All package installation was done in a virtual environment for easy management. The only notable dependency is **tweepy**.

### Technologies used
This project was done solely in Python.

### How to run
Clone or download the project to your machine. to clone the project use the command: "git clone https://github.com/NeilK-94/Tweepy-Scripts.git"

You will need to create a twitter app at the following link: https://developer.twitter.com/en/apps

Once this is done, you should create a secrets file and declare your authentication and consumer keys/secrets there. Then import the secrets file into each script.

From this directory you must run the below command on the command line to run the script.
```python
$ python <script name>
```

You can tweak each script as you see fit, such as changing search terms or reconfiguring parameters for following an account etc.
