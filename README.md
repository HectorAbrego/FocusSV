# FocusSV
Python Backend Developer Test

How the code is structured
For this the solution it's necessary only one folder, named with your preferred name where you must to add the files specified in this solution.
The server used is the one used by default with port 5000. localhost/5000
In the solution, there are only 2 .py files. The podcast.py contains the JSON and the app.py which contains all necessary code to implement the solution.
In the app.py is started the server using the port 5000 as default and contains the next routes:
	1. '/podcasts' Is used to show all JSON 
	2. '/podcasts' Receive as a filter the "podcast name". This route is used to filter the JSON and show an especific element. 
	3. '/podcastsname' Receive as a filter the "podcast artist name". This route is used to filter the JSON and show an especific element. 
	4. '/podcaststop20' this route will help us to create a file with the top 20 podcasts.
	5. '/podcastsbottom20' this route will help us to replace the top 20 podcasts with the bottom 20 podcasts.
	6. '/podcastsdelete' Receive as a filter the "podcast artist name". This route is used to delete a JSON's element and create a new file without the deleted element
All files used in this solution are in the Python_Exercise folder in this GitHub.


How to run each solution
Resolution of first exercise: A service to provide a search lookup within the podcasts.
  1. Create a folder with the name that you prefer, in this case was named Python_Exercise
  2. Inside the folder you most to copy the next files. 
      podcast.py which contains the JSON.
      app.py which contains the routes with their different filters by podcast name and podcast artist name, also contains the configuration of Server's port.
  3. Using the framework of your preference, you can visualize both files. In this case, Visual Studio Code was used.
  4. Using the terminal you write the next instruction: python app.py
  5. Open your preferred browser and write in the url bar the next example url http://localhost:5000/podcasts/Nice%20White%20Parents to filter by podcast name
  5. Open your preferred browser and write in the url bar the next example url http://localhost:5000/podcastsname/The%20New%20York%20Times to filter by podcast artist name

Resolution of second exercise: A service that would allow to save the top 20 podcasts to a separate JSON File
  1. The file app.py was modified, it was added the route '/podcaststop20'
  2. Using the framework of your preference, you can visualize the file. In this case, Visual Studio Code was used.
  3. Using the terminal you write the next instruction: python app.py
  4. Open your preferred browser and write in the url bar the next example url http://localhost:5000/podcaststop20 
  5. Once the process finished, the file podcastTop20.json is created in the main folder.
 
Resolution of third exercise: A service to replace the top 20 podcasts for the bottom 20 to said JSON File
  1. The file app.py was modified, it was added the route '/podcastsbottom20'
  2. Using the framework of your preference, you can visualize the file. In this case, Visual Studio Code was used.
  3. Using the terminal you write the next instruction: python app.py
  4. Open your preferred browser and write in the url bar the next example url http://localhost:5000/podcastsbottom20
  5. Once the process finished, the file 20podcasts.json is updated in the main folder.

Resolution of fourth exercise: A service to remove a podcast, using a given identifier (defined by you)
  1. The file app.py was modified, it was added the route '/podcastsdelete'
  2. Using the framework of your preference, you can visualize the file. In this case, Visual Studio Code was used.
  3. Using the terminal you write the next instruction: python app.py
  4. Open your preferred browser and write in the url bar the next example url http://localhost:5000/podcastsdelete/Duolingo
  5. Once the process finished, the file newjson.json is created in the main folder.
