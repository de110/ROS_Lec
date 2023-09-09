# ROS_Lec
###### 2020-2 로봇운영체제 강의 과제 저장소

##### Webots 프로젝트

### 1. Node
&nbsp;&nbsp;
사용된 노드(Node)는 다음과 같다.

&nbsp;&nbsp;
<img width="500" alt="pub_sub" src="https://github.com/de110/ROS_Lec/assets/67581448/f192e695-05a4-4471-9907-a391361d0853"> 

&nbsp;&nbsp;&nbsp;&nbsp;
[그림 1]  사용된 노드  

&nbsp;&nbsp;
속도 값을 전달받기 위한 /cmd_vel_publisher, epuck을 제어하기 위한 /epuck_driver, 적외선 센서 값을 전달받는 /subscriber_tof,<br/>&nbsp;&nbsp; 로봇의 현재 상태를 나타내는 /robot_state_publisher 까지, 총 네 개의 노드가 사용되었다.

### 2. Topic/service

&nbsp;&nbsp;
토픽(Topic) 구성은 다음과 같이 네 단계로 확인하였다. 우선 Publisher와 Subscriber를 제외한 초기 토픽을 확인하고, <br/>&nbsp;&nbsp; 두 번째와 세 번째는 각각 Publisher와 Subscriber를 포함한 토픽 구성을 확인하였다. <br/>&nbsp;&nbsp; 이후 마지막으로 앞선 세 단계를 모두 동시에 포함한 토픽을 확인하였다.

##### 2.1 e-puck 초기 토픽<br/>
&nbsp;&nbsp;
e-puck 예제 프로젝트의 초기 토픽과 노드 구성은 [그림 2]와 같으며, 토픽 Joint_states은 epuck_driver에 의해 송신된다.

&nbsp;&nbsp;&nbsp;&nbsp;
      <img width="500" alt="Epuck_initial2" src="https://github.com/de110/ROS_Lec/assets/67581448/f80bb87a-e1df-420d-bb52-17cc9ec5fcce"><br/>
      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[그림 2]  e-puck 초기 토픽 및 노드 구성

##### 2.2 Publisher 실행<br/>
&nbsp;&nbsp;
Publisher 실행에 따른 노드와 토픽 구성은 [그림 3]과 같다.

&nbsp;&nbsp;
master_node와 cmd_vel_publisher가 n:1 구성으로 cmd_vel 토픽에 접근하여 epuck_driver로 전달된다.

&nbsp;&nbsp;
<img width="500" alt="add_publish_vel3" src="https://github.com/de110/ROS_Lec/assets/67581448/001e050f-b089-4339-948e-8944ebed14f9">

&nbsp;&nbsp;&nbsp;&nbsp;
[그림 3] Publisher 토픽 및 노드 구성
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
##### 2.3 Subscriber 실행

&nbsp;&nbsp;
[그림 4]는 Subscriber를 실행했을 시 노드와 토픽 구성을 나타낸다.

&nbsp;&nbsp;
적외선 센서 값인 토픽 tof가 epuck_driver에 의해 전달되어 subscriber인 subscriber_tof 노드로 송신된다.  

&nbsp;&nbsp;
<img width="500" alt="add_subscriber_tof2" src="https://github.com/de110/ROS_Lec/assets/67581448/2d77a13d-4dcf-4454-be01-35321c726f05">  

&nbsp;&nbsp;&nbsp;&nbsp;
[그림 4] Subscriber 토픽 및 노드 구성

##### 2.4 Publisher, Subscriber 실행  
  
&nbsp;&nbsp;
Publisher와 Subscriber를 함께 실행한 노드, 토픽 구성은 [그림 5]와 같다.

&nbsp;&nbsp;
cmd_vel_publisher가 토픽 cmd_vel을 epuck_driver로 송신하며,

&nbsp;&nbsp;
노드 epuck_driver는 Joint_states와 tof 값을 각각 robot_state_publisher 노드와 subscriber_tof 노드로 송신한다.
    
&nbsp;&nbsp;
<img width="500" alt="pub_sub2" src="https://github.com/de110/ROS_Lec/assets/67581448/3a663ae7-1fdf-4485-b2b4-1bd2edb1f267">
    
&nbsp;&nbsp;&nbsp;&nbsp;
[그림 5] Publisher, Subscriber 토픽 및 노드 구성

### 3. 기능 추가 및 결과
&nbsp;&nbsp;
로봇의 속도와 로봇에 장착된 적외선 센서 값을 받기 위해 publisher_vel.py와 subs_tof.py 를 추가했다.

##### 3.1 구현 결과
&nbsp;&nbsp;
![Epuck_result](https://github.com/de110/ROS_Lec/assets/67581448/a709c687-f343-44aa-ad6b-07c7787040bd)

&nbsp;&nbsp;&nbsp;&nbsp;
[그림 6] e-puck 초기 실행 화면


&nbsp;&nbsp;
![publisher_result](https://github.com/de110/ROS_Lec/assets/67581448/19504808-f728-4b77-8f7c-20dd6b0d4cf2)

&nbsp;&nbsp;&nbsp;&nbsp;
[그림 7] publisher 실행 화면


&nbsp;&nbsp;
![subscriber_result](https://github.com/de110/ROS_Lec/assets/67581448/53a69ae3-e611-4236-b178-3f431709216c)

&nbsp;&nbsp;&nbsp;&nbsp;
[그림 8] subscriber 실행 화면

&nbsp;&nbsp;
프로젝트 실행 결과, 기존 예제 e-puck 프로젝트를 실행할 시에는 [그림 6]과 같이 월드의 중간에 위치해 있음을 확인하였다.

&nbsp;&nbsp;
publisher를 실행하였을 시 지정한 값에 따라 e-puck 로봇이 맵 위를 움직였다.<br/>&nbsp;&nbsp; subscriber 실행 시 [그림 6]과 [그림 7]의 초록색 실선으로 나타나는, 로봇의 적외선 센서가 물체를 인식함을 확인할 수 있었으며, <br/>&nbsp;&nbsp; 그 인식값은 [그림 8]과 같다.
