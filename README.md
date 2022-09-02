# audio_processing
We can utilize this repository to process audio data. 



- This repository represents **" Basic Audio processing"**  "**.
- With the help of this project we can record, play , plot , denoise, perform declipping on audio data. 
  
## 📝 Description
- This implemantation is based on processing of audio data.
- In this project we have used **pygame** and **pyaudio** for audio processing.
- There are four routes for this api
- record_and_save
- play
- plot_audio
- denoise
- declipping



## :desktop_computer:	Installation


### :hammer_and_wrench: Requirements
* Python 3.8+
* fastapi==0.81.0
* pyAudio==0.2.12
* noisereduce==2.0.1
* uvicorn==0.18.3
* pygame==2.1.2
* PyYAML==6.0.0



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
$ pip install -r requirements.txt
```

4. Initalize the uvicorn server 
```bash
$ uvicorn app:app --reload
```

## 🎯  demo

1. Testing with **Recording voice and saving it at location predefined** (after starting server write `localhost:8000/record_save` in browser url to get a glace of the application)

![infrence_example](https://github.com/sanjeev49/audio_processing/blob/main/docs/Screenshot%202022-09-02%20124817.png)



## Contributor <img src="https://raw.githubusercontent.com/TheDudeThatCode/TheDudeThatCode/master/Assets/Developer.gif" width=35 height=25> 
- Sanjeev Kumar