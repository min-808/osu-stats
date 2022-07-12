<ins>**Detailed explanation on how it works**</ins>

The program **always** calls the askforAPI() function first, which checks if the api.txt file is empty or if the variable "editAPI" is True. <ins>If the result is true</ins>, then the program asks the user to set an API key and presents instructions on how to obtain one. After something is entered, it puts the information inside the api.txt file and calls the askforName() function. <ins>If the result is false</ins>, then the else function does nothing, and so the program moves onto the askforName() function at the very bottom.

The askforName() function first takes the API key found in the api.txt file and assigns it to readapiKey. Then it asks for the user's name, and checks if it's valid by doing a test call to the osu! API with the username. <ins>If it responds with either a blank message or an API error</ins>, it calls the foundError() function and tells the user that the Username or the API key is invalid. Then, it tells them to either edit their API key, or enter a new username. The option is decided with the fix function. <ins>If it doesn't respond with either of those</ins>, then it takes the country and correctly capitalizes the player's username and welcomes them. Then, it displays the possible options the user could choose from.

The rest of the code in each of the options should be fairly straightforward, with chosenOption being the variable the user selects, and elif statements allowing for the other options. <ins>sys.exit</ins> is used to close out of the application.

Also, I can definitely make the code much more compact by making askagainOptions() a global function that can be called repeatedly. Instead, the function is being made each time a new option is selected. I'll fix that eventually. + make sure to change to cls clear instead of "clear"

Debug1 shows the get_user response

Debug2 shows the get_user_best response

Debug3 shows the get_user_recent response

<h1>Currently in the middle of making best/recent scores. this will require additional calls to the API with more variables aaaaa</h1>
<h1>done^^</h1>
