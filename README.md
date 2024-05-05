#  Flight-Search-Web-App

Web Application for finding cheapest flights, based on user-defined criteria. Made with Python 3.12 backend in Flask and frontend in React.js integrated with external [Tequilla API](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwj6kNT7jJSFAxXwcvEDHXhJArcQFnoECA8QAQ&url=https%3A%2F%2Ftequila.kiwi.com%2F&usg=AOvVaw0cgCMmCdXi_Q61rVhtC__G&opi=89978449).

  

#  Exercises

![chart](https://raw.githubusercontent.com/Hampter-wojkur/Flight-Search-Web-App/exercises/screenshots/chart.png)

## Exercise 1
Create Sample flask app with `POST` method which will return some kind of message in `JSON` format. 
To test it we recommend [Thunder Client](https://www.thunderclient.com/) to install it as a vscode extension. 
Install dependencies by: 
`pip install -r requirements.txt`
You can run app by: 
`python3 server.py`
## Exercise 2
Create Frontend React app with Button. Add event handler to it and change state. Display current state value before and after clicking button. You can easily create React app with: 
`npx create-react-app exercise2`
Expected output will be someting like that:
Before:
![before](https://raw.githubusercontent.com/Hampter-wojkur/Flight-Search-Web-App/exercises/screenshots/before.png)
After:
![after](https://raw.githubusercontent.com/Hampter-wojkur/Flight-Search-Web-App/exercises/screenshots/after.png)
## Exercise 3
Connect frontend and backend by sending request after clicking button. 
Receive message from backend and change actual state. 
Display message which backend sent to You, as a updated state. 
You can access your backend url by:
`http://localhost:<PORT_IN_YOUR_FLASKAPP>`
