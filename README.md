# Travel-predictor
This is a simple random travel predictor just for fun. Where are you heading this summer?


It will track your face, give you a nice little random flag on top of your head and randomly pick a place you'll travel to in 2020. 

![ezgif com-video-to-gif](https://user-images.githubusercontent.com/47258547/80616583-ffa49800-8a38-11ea-9e83-b2081ed8cc48.gif)


Now, here is the trick. If you want it to always show home as the predicted place to travel too you should use --unlock_home when calling the script in terminal.


If you want to use this with your android phone as an external camera. You need to install ipwebcam on your phone
and have both your computer and phone on the same wifi.
Then, you can just add the --ipwebcam <link to local stream/video> which you'll find the link once you have
started the server on your phone.

You can also enable recording a video by using --enable_record in terminal.
--out_path enables you to choose the path and name for the recorded video

You can add asmany countries as you want, do put them in the images folder and make sure to rename them as a proper
country name. You don't want the program to say Congragulations! you're going to  dlknsdfjksndfjqnflnsf-img

Dependencies:
opencv-python
you can dowload it using pip

pip install opencv-python (run this in terminal or in anaconda prompt)




