# AddGiftoCameraWindow - Python Uygulaması

## Herkese Selamlar

Bu proje, Python ile kodlanmış bir görüntü işleme uygulamasıdır. 

Bu projeyi yapmamdaki amaç; OpenCV kütüphanesini kullanarak laptop kamerasından alınan canlı görüntüye farklı gif görüntüleri eklemek ve bu süreç içerisinde yaşanabilecek sorunları görmekti.

Gif uzantılı görsel gruplarını istenilen şekilde ve konumda canlı görüntü üzerine nasıl ekleyebileceğimi denemek istedim. Sonuç olarak böyle bir uygulama ortaya çıktı.

## İçindekiler

0. [Herkese Selamlar](#herkese-selamlar)
1. [Uygulama Hakkında](#uygulama-hakkında)
2. [Yüklenmesi Gereken Kütüphaneler](#yuklenmesi-gereken-kutuphaneler)
3. [Youtube Linki](#youtube-linki)

## Uygulama Hakkında

Uygulama çalıştırıldığı anda itibaren gifler canlı kamera görüntüsü üzerine eklenerek gösterilir. Çıkış yapmak için Q tuşuna basmak yeterlidir.

![](./examples/image.gif)

Laptop kamera görüntüsü aşağıdaki kod parçacığındaki **VideoCapture(0)** ile alınmaktadır. Başka bir kamera eklemek isterseniz 0 değerini değiştirmeniz gerekir. Uygulama çalıştırıldığın da kamera açılmazsa kameranızın ulaşılabilirliğinin açık olduğundan emin olun.

```
cap = cv2.VideoCapture(0)

```

## Yuklenmesi Gereken Kutuphaneler

- Opencv kütüphanesi

```
pip install opencv-python

```
- Numpy kütüphanesi

```
pip install numpy

```


## Youtube Linki

Youtube üzerinden paylaştığım uygulama videosuna [bu linkten](https://youtu.be/x6Xca0RRyYI) ulaşabilirsiniz.
