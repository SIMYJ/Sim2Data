# Unreal Engine + Airsim 환경에서 detection를 해보자. 

## 1.하고자 하는 방향
- Unreal Engine + Airsim를 활용하여 가상환경에서 Person를 dettioin(BBOX)

## 2.시작하기 전에
- window환경에서 Airsim 설치 (Unreal Engine4.25, epicgames 설치,landscapes 다운로드, 환경설정 등등)
- Unreal Engine4.25에서 Person 클래스 생성(C++)
- [detection.py](https://github.com/microsoft/AirSim/blob/master/PythonClient/detection/detection.py
) 코드 사용 

## 3.코드 설명

|📅날짜|📒파일명|🔊설명|
|---|----|----|
| 2021.xx.xx|[setup_path.py](https://github.com/SIMYJ/Sim2Data/blob/main/Airsim_detection/code/setup_path.py)| 실행할 모듈(.py)과 같은 폴더에 존재 해야된다.|
| 2021.xx.xx|[detection_cylinder.py](https://github.com/SIMYJ/Sim2Data/blob/main/Airsim_detection/code/detection_cylinder.py)| Airsim에서 기본 제공하는 코드|
| 2021.xx.xx|[detection_person00.py](https://github.com/SIMYJ/Sim2Data/blob/main/Airsim_detection/code/detection_person00.py)| 기본제공 코드에서 cylinder -> person 변경|
| 2021.08.11|[detection_person01.py](https://github.com/SIMYJ/Sim2Data/blob/main/Airsim_detection/code/detection_person01.py)| 원본이미지, bbox좌표 JSON파일, bbox적용된 이미지 파일 생성코드 추가  |



