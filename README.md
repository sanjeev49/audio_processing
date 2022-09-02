# audio_processing
We can utilize this repository to process audio data. 



- This repository represents **" Basic Audio processing"**  "**.
- With the help of this project we can record, play , plot , denoise, perform declipping on audio data. 
  
## 📝 Description
- This implemantation is based on processing of audio data.
- In this project we have used **pygame** and **pyaudio** for audio processing.



## :desktop_computer:	Installation


### :hammer_and_wrench: Requirements
* Python 3.8+
* fastapi==0.81.0
* pyAudio==0.2.12
* noisereduce==2.0.1
* uvicorn==0.18.3
* pygame==2.1.2



## :gear: Setup
1. Create virtual enviroment
```bash
$ conda create --prefix ./env python=3.8.13 -y
```
2. Activate conda enviroment 
```bash
$ conda activate ./env
```

3. Install Required libraries
```bash
$ pip install requirements.txt
```

4. Initalize the uvicorn server 
```bash
$ uvicorn main:app --reload
```

## 🎯  demo

1. Testing with **Images** (Put test inages in anywhere and give the location of this image to **img_path** parameter inside prediction model function in src/infrence.py file)

![infrence_example](https://github.com/sanjeev49/aiClassification/blob/master/docs/img/infrence_example2.png)



## Contributor <img src="https://raw.githubusercontent.com/TheDudeThatCode/TheDudeThatCode/master/Assets/Developer.gif" width=35 height=25> 
- Sanjeev Kumar