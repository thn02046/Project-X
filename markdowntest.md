로그 분석을 통한 사고원인 분석
=============

> 남아있는 로그파일을 활용해 기지 폭발의 원인을 분석하기위해 
> 파이썬과 파이썬 개발도구를 설치하고 로그파일을 출력하였다..

## 1. 출력한 로그파일 원문
```
timestamp,event,message
2023-08-27 10:00:00,INFO,Rocket initialization process started.
2023-08-27 10:02:00,INFO,Power systems online. Batteries at optimal charge.
2023-08-27 10:05:00,INFO,Communication established with mission control.
2023-08-27 10:08:00,INFO,Pre-launch checklist initiated.
2023-08-27 10:10:00,INFO,Avionics check: All systems functional.
2023-08-27 10:12:00,INFO,Propulsion check: Thrusters responding as expected.
2023-08-27 10:15:00,INFO,Life support systems nominal.
2023-08-27 10:18:00,INFO,Cargo bay secured and sealed properly.
2023-08-27 10:20:00,INFO,Final system checks complete. Rocket is ready for launch.
2023-08-27 10:23:00,INFO,Countdown sequence initiated.
2023-08-27 10:25:00,INFO,Engine ignition sequence started.
2023-08-27 10:27:00,INFO,Engines at maximum thrust. Liftoff imminent.
2023-08-27 10:30:00,INFO,Liftoff! Rocket has left the launchpad.
2023-08-27 10:32:00,INFO,Initial telemetry received. Rocket is on its trajectory.
2023-08-27 10:35:00,INFO,Approaching max-Q. Aerodynamic pressure increasing.
2023-08-27 10:37:00,INFO,Max-Q passed. Vehicle is stable.
2023-08-27 10:40:00,INFO,First stage engines throttled down as planned.
2023-08-27 10:42:00,INFO,Main engine cutoff confirmed. Stage separation initiated.
2023-08-27 10:45:00,INFO,Second stage ignition. Rocket continues its ascent.
2023-08-27 10:48:00,INFO,Payload fairing jettisoned. Satellite now exposed.
2023-08-27 10:50:00,INFO,Orbital insertion calculations initiated.
2023-08-27 10:52:00,INFO,Navigation systems show nominal performance.
2023-08-27 10:55:00,INFO,Second stage burn nominal. Rocket velocity increasing.
2023-08-27 10:57:00,INFO,Entering planned orbit around Earth.
2023-08-27 11:00:00,INFO,Orbital operations initiated. Satellite deployment upcoming.
2023-08-27 11:05:00,INFO,Satellite deployment successful. Mission objectives achieved.
2023-08-27 11:10:00,INFO,Initiating deorbit maneuvers for rocket's reentry.
2023-08-27 11:15:00,INFO,Reentry sequence started. Atmospheric drag noticeable.
2023-08-27 11:20:00,INFO,Heat shield performing as expected during reentry.
2023-08-27 11:25:00,INFO,Main parachutes deployed. Rocket descent rate reducing.
2023-08-27 11:28:00,INFO,Touchdown confirmed. Rocket safely landed.
2023-08-27 11:30:00,INFO,Mission completed successfully. Recovery team dispatched.
2023-08-27 11:35:00,INFO,Oxygen tank unstable.
2023-08-27 11:40:00,INFO,Oxygen tank explosion.
2023-08-27 12:00:00,INFO,Center and mission control systems powered down.

Process finished with exit code 0
```

## 2. 원문 분석 결과
**분석 결과 아래의 세 문장을 통해 모종의 이유로 산소탱크가 불안정해져 폭발한것이 이번 참사의 원인임을 확인하였다.**
```
2023-08-27 11:35:00,INFO,Oxygen tank unstable.
2023-08-27 11:40:00,INFO,Oxygen tank explosion.
2023-08-27 12:00:00,INFO,Center and mission control systems powered down.
```
