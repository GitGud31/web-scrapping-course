# Projet
* The goal is to try and scrap ***YouTube*** and get Titles, and video links.
* Store the results in a **.csv** file.
* Store the reuslts in a **Postgres database** in a **Docker container**.

## TODO
- [x] Choix du site web et des données.
- [x] Problématique pertinente.
- [x] Outil de scrapping.
- [x] Documentation dans un Jupyter Notebook.
- [x] Documentation dans un README.md.
- [x] Enregistrement des données dans une base de données.
- [x] Analyse rapide des données.
- [x] Paquetage dans un conteneur Docker.

## Tools needed
* Visual Studio Code installed, (best with Jupyter extension).
* Python environment **or** Jupyter Notebook installed.
* Have the following libraries: bs4, pandas, selenium, time and tqdm
* Docker Desktop installed.

## How to run 
* Clone the repo.
* Start Docker daemon.
* Open the .ipynb file and follow the steps in the screenshots bellow.

### Step 0 - Run your docker container
* Run ``` docker run --name my_postgres -e POSTGRES_PASSWORD=YOUR_PASSWORD_HERE -d -p 5431:5432 postgres ```
* and ``` docker exec -it my_postgres bash ```

  **OR** 

* Run ``` docker compose up ```

* Then connect to your database: ``` psql -h localhost -p 5432 -U postgres -d postgres ```
* Check if you have a database called 'youtube_videos' by typing ``` \l ```. ![alt text](/showcase/db.png)
* if you don't create it by typing : ``` CREATE DATABASE youtube_videos ``` then check again with ``` \l ```.

#### Step 1 - Import the necessary libraries
![alt text](/showcase/step1.png)

#### Step 2 - Initialize a Chrome WebDriver instance
This will open a chrome page
![alt text](/showcase/step2.png)

#### Step 3 - Initialize a Chrome WebDriver instance
This will open a textfield input in Visual Studio Code, where you can enter the YouTube channel.
![alt text](/showcase/step3.png)

#### Step 4 - Build a Google seach link from the the channelName
![alt text](/showcase/step4.png)

#### Step 5 - Open the built link in the chrome tab
accept/reject the popup of Chrome's Terms of Service and Cookies when asked.
![alt text](/showcase/step5.png)

#### Step 6 - Parse the HTML of the Google page result
![alt text](/showcase/step6.png)

#### Step 7 - Extract the link of the first Google result
![alt text](/showcase/step7.png)

#### Step 8 - Open the channel in the browser
accept/reject the popup of Youtube's Terms of Service and Cookies when asked.
![alt text](/showcase/step8.png)

#### Step 9 - Parse the HTML of the page
(Optionally) you can print the result.
![alt text](/showcase/step9.png) 

#### Step 10 - Load more videos
This loop is to simulate scrolling behavior on the webpage. By scrolling down the page in increments of 1000 pixels, it triggers the loading of more videos dynamically.
![alt text](/showcase/step10.gif)

#### Step 11 - Parse the page again after scrolling
![alt text](/showcase/step11.png)

#### Step 12 - Get all the video items on that page
![alt text](/showcase/step12.png)

#### Step 13 - Extract the data 
In this example we Get : link, title, views and uploadTime.

(Optionally) you can print the result.
![alt text](/showcase/step13.png)
* ```
  link = "https://www.youtube.com/" + item.find('a', class_='yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media').get('href')
  ```
  This line finds the < a > element within the video_item that contains the URL (href) of the video. It then constructs the complete YouTube video link by appending the relative URL to the base YouTube URL. This link is stored in the variable link. 

* ```
    title = item.find('a', class_='yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media').get('title')
  ```
   This line finds the < a > element within the video_item that contains the title of the video (title attribute) and retrieves its text content. The title of the video is stored in the variable title.

* ```
    views = (item.find('span', class_="inline-metadata-item style-scope ytd-video-meta-block").text.split(" ")[0])
  ```
  This line finds the < span > element within the video_item that contains the number of views of the video. It retrieves the text content, splits it by space, and selects the first part (which represents the number of views). The number of views is stored in the variable views.

* ```
  upload_time = (item.find_all('span', class_="inline-metadata-item style-scope ytd-video-meta-block")[1].text)
  ```
  This line finds all < span > elements within the video_item that contain metadata about the video. It retrieves the text content of the second < span > element (index [1]), which typically represents the upload time of the video. The upload time is stored in the variable upload_time.

* ```
    data.append([link, title, views, upload_time])
  ```
  This line appends a list containing the extracted information (link, title, views, upload_time) for each video to the data list. The data list will be used later to create a DataFrame and store the information in a CSV file.

#### Step 14 - Save the data in a CSV file
![alt text](/showcase/step14.png)
CSV file 
![alt text](/showcase/step14_1.png)

### Step 15 - Plot results

![alt text](/showcase/step15.png)

In this example we can see : 
* Range of Views: The views vary widely among the videos, ranging from a few thousand to several million views. 
* Highly Viewed Videos: There are several videos with high view counts, such as "Race Highlights | ..."

#### Step 16 - Save data in Postgres database that's running in a docker container

![alt text](/showcase/step16_1.png) 
![alt text](/showcase/step16_2.png)
![alt text](/showcase/step16_3.png)
![alt text](/showcase/step16_4.png)

- Result From docker database.
![alt text](/showcase/step16_5.png)
- Get Result from docker database and printed in Jupyter.
![alt text](/showcase/step16_6.png)

