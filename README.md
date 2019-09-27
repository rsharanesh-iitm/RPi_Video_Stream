# RPi Video Stream
### Motion
`sudo apt install motion lsusb`

### On RPi
```
sudo apt install git
git clone https://github.com/aswinkumar1999/RPi_Video_Stream.git
cd RPi_Video_Stream
chmod u+x install.sh
./install.sh
```
To Stream Video from RPi :

#### IMAGEZMQ
Open the File and Chnage the IP which you need to connect to and Save the File

`python3 rpi_send_jpg.py`

#### FFMPEG
`node app.js`
```
python cam.py | ffmpeg -y -f rawvideo -vcodec rawvideo -pix_fmt bgr24 -s 640x480 -i - -c:v libx264 -pix_fmt yuv420p -preset ultrafast -framerate 10 -f flv rtmp://127.0.0.1
```
### On Computer
#### IMAGEZMQ
##### Linux
```
git clone git@github.com:aswinkumar1999/RPi_Video_Stream.git
cd RPi_Video_Stream
sudo apt install opencv-python
pip3 install imutils pyzmq
```
To Recieve Images :
```
python3 recieve_jpg.py
```
FFMPEG
Open VLC and Open Network Stream -> and type in

`rtmp://pi-ip-address:1935`
