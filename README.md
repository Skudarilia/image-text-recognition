# image-text-recognition
## Веб-сервис image-text-recognition на базе фреймворка __EasyOCR__, в качестве REST API был взят __Flask__

Данный сервис позволяет __загружать изображение и получать с него текст__ (если он есть). Распознаются русский и английский языки.

Модель easyocr может рабоать как на gpu (быстрее), так на cpu (медленнее). В данном примере я отключил gpu.

При запуске приложения запускается сервер, на который можно перейти по http://127.0.0.1:5000/

Больше о EasyOCR: https://github.com/JaidedAI/EasyOCR

Примеры работы:

![image](https://user-images.githubusercontent.com/55200466/146583429-4532e7e9-dbc2-429f-8a5d-3b5438290fe3.png)
![image](https://user-images.githubusercontent.com/55200466/146581668-bc443ce8-d17c-485b-a272-7e85de3adda8.png)
