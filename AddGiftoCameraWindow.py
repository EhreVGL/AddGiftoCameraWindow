import cv2
import numpy as np

cap = cv2.VideoCapture(0)
i = 0
j = 0
z = 0
gif_sayac = 0
i1 = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # resize
    width = int(1280)
    height = int(853)
    # dsize
    dsize = (width, height)
    # resize image
    frame = cv2.resize(frame, dsize)
    img1_kopya = frame.copy()
    img1_we, img1_he, _ = frame.shape
    if z == 0:
        sutun = img1_he - 150
        z = 1


    img2 = cv2.imread('images/frame%d-re.jpg'%i)
    frame = img1_kopya.copy()

    # gif resmini koyarken ekrana ilk geri attığı nokta burası ondan burada uygun düzeyde ileri sarıyoruz.
    if i == 5:
        sutun -= 60

    # Koymak istediğim görsellerin konumunun ayarlanması
    rows, cols, channels = img2.shape
    roi = frame[500:rows + 500, sutun:cols + sutun]

    # Görsellerin maskesinin ve ters maskesinin oluşturulması
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # Görselin alanını roi üzerinde karartma
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    # Görsel üzerinden sadece region'ların alımı
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
    # Modifiye edilmiş roi'nin ana ekrana eklenmesi
    dst = cv2.add(img1_bg, img2_fg)
    frame[500:rows + 500, sutun:cols + sutun] = dst


    if i < 10:
        i += 1
    else:
        i = 0
        # gif'i ilk oynatışı veya 10. oynatısıysa sağdan başlat, değilse her tekrarda -50 piksel sil
        if gif_sayac == 0 or gif_sayac == 10:
            sutun = img1_he - 150
            gif_sayac = 0
        else:
            sutun -= 57

        gif_sayac += 1

    # BABY DRAGON
    # sutun1


    img_dragon = cv2.imread('images/dragon%d.jpg'%i1)
    # Ekranın %50'sinin hesaplanması
    width = int(img_dragon.shape[1] * 0.5)
    height = int(img_dragon.shape[0] * 0.5)

    # dsize
    dsize = (width, height)

    # resize image
    img_dragon = cv2.resize(img_dragon, dsize)
    print(img_dragon.shape)

    # Gif'in frame'i roi'e ekleniyor.
    rows1, cols1, channel1 = img_dragon.shape
    print(rows1, cols1, channel1)
    roi1 = frame[100:rows1 + 100, 225:cols1 + 225]
    print(roi1.shape)
    # Görsellerin maskesinin ve ters maskesinin oluşturulması
    img2gray1 = cv2.cvtColor(img_dragon, cv2.COLOR_BGR2GRAY)
    ret1, mask1 = cv2.threshold(img2gray1, 10, 255, cv2.THRESH_BINARY)
    mask_inv1 = cv2.bitwise_not(mask1)
    # Görselin alanını roi üzerinde karatma
    img1_bg1 = cv2.bitwise_and(roi1, roi1, mask=mask_inv1)

    # Görsel üzerinden sadece region'ların alımı
    img2_fg1 = cv2.bitwise_and(img_dragon, img_dragon, mask=mask1)
    # Modifiye edilmiş roi'nin ana ekrana eklenmesi
    dst1 = cv2.add(img1_bg1, img2_fg1)
    frame[100:rows1 + 100, 225:cols1 + 225] = dst1


    if i1 == 59:
        i1 = 0
    else:
        i1 += 1

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(75) & 0xFF == ord('q'):
        break

# Her şey bittiğinde (q tuşuna basıldığında) ekran kapatılır.
cap.release()
cv2.destroyAllWindows()
