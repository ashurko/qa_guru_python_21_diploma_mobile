# 🎓 QA.GURU Mobile Wiki Project

*Небольшой проект по автоматизации на основе приложения Wikipedia, базовой проверке нескольких кейсов*
# <img width="10%" title="wiki_logo" src="data/logo/icons8-wikipedia-48.png" />
## О проекте

Этот проект является дипломной работой по курсу QA.GURU и представляет собой фреймворк для автоматизации тестирования приложения ["Wikipedia"](https://www.wikipedia.org). В реализации использованы инструменты и библиотеки:

<p  align="center">
  
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="70" width="70"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="70" width="70"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" height="70" width="70"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" height="70" width="70"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" height="70" width="70"/>
  <img width="9%" title="Selene" src="data/logo/selene.png" alt="selene"/>
  <img width="8%" title="Allure Report" src="data/logo/allure_report.png" alt="allure">
  <img width="8%" title="Selenoid" src="data/logo/selenoid.png" alt="selenoid">
  <img width="8%" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/browserstack/browserstack-original-wordmark.svg" />
  <img width="8%" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/androidstudio/androidstudio-original.svg" />



</p>

## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="20" width="20"> Запуск тестов локально

1) Клонировать репозиторий: git clone https://github.com/ashurko/qa_guru_python_21_diploma_mobile
2) Установить зависимости: pip install -r requirements.txt
3) Запуск тестов с выбором параметра источника запуска тестов: pytest --context={enviroment} (где enviroment = bstack / local_emulator / local_real_device)

##   <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="20" width="20"/> Создание сборки на удаленном сервере - Jenkins

1) Авторизоваться в Jenkins
2) Перейти в джобу https://jenkins.autotests.cloud/job/anton_shurko_diploma_mobile/
3) Для запуска тестов в Jenkins нажать "Build With Parameters"
4) Выбрать необходимые параметры
5) Нажать Run Build

<p><img title="jenkins_build" src="data/logo/jenkins_flow1.png"></p>

<p><img title="jenkins_build" src="data/logo/jenkins_flow2.png"></p>

## <img width="4%" title="allure" src="data/logo/allure_report.png"> Визуализация результатов (Allure Reports)

Для просмотра результатов тестового запуска в Allure необходимо кликнуть на соответствующую ему иконку

<p><img title="Allure" src="data/logo/allure_result2.png"></p>
<p><img title="Allure" src="data/logo/allure_result1.png"></p>


## Если тесты запускались локально, то результаты можно посмотреть командой: 

```bash
allure serve reports/allure-results
```



## <img width="4%" title="tg" src="data/logo/tg.png"> Интеграция с Telegram в Jenkins для автоматической отправки результатов тестового прогона через бота

<p><img title="telegram" src="data/logo/report_tg.png"></p>