# MyAddys-Custom-Background
Allows you to have a custom background on https://myaddys.com

# Usage

Once it's running, it'll ask your for your "Session Cookie", once that's input it'll, ask for a link to your image (must be i.imgur.com) and once thats input, it will set your background to whatever image you inputted

# Setup
1. Install python if you haven't already (https://www.python.org/)
2. Make sure you have some sort of software that can extract a .zip file, I use https://www.win-rar.com/ personally
3. Download the entire repository as a .zip file & extract it to its own folder by using your extraction software by clicking on and then right clicking on the .zip file & clicking extract
4. In the directory of the folder run this command in command terminal: `pip install requests`
7. In the directory of the folder run this command in command terminal: `python main.py`
8. Then paste in your "Session Cookie", I've showed [how to get it below]()

# How To Get Session Cookie
1. Go to https://myaddys.com
2. Create an account if you haven't already
3. Open developer tools/inspect element
4. Find the application tab at the top of that (if it isn't any of the tabs already showing, click on the arrows next to those and find it there)
5. Then in that, find "Cookies" and expand that, then click on the first element
6. Find the cookie "Secure-next-auth.session-token" and copy it's value
7. You now have the session cookie

# How To Get Image Url
