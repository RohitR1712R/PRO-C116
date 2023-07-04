import cv2
import numpy as np

img = cv2.imread("Solar-system.jpg")
cv2.putText(img,
            "Sun",
            (67,70),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (255,255,255)
            )

cv2.putText(img,
            "Mercury",
            (110,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (190,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Earth",
            (290,265),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Moon",
            (320,160),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            )

cv2.putText(img,
            "Mars",
            (385,175),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (550,375),
            cv2.FONT_HERSHEY_COMPLEX,
            0.75,
            (255,255,255)
            )

cv2.putText(img,
            "Saturn",
            (750,310),
            cv2.FONT_HERSHEY_COMPLEX,
            0.75,
            (255,255,255)
            )

cv2.putText(img,
            "Uranus",
            (955,295),
            cv2.FONT_HERSHEY_COMPLEX,
            0.75,
            (255,255,255)
            )

cv2.putText(img,
            "Neptune",
            (1095,295),
            cv2.FONT_HERSHEY_COMPLEX,
            0.75,
            (255,255,255)
            )

cv2.putText(img,
            "Rohit",
            (1190,400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.75,
            (255,255,255)
            )
cv2.imshow("SOLAR SYSTEM", img)
cv2.waitKey(0)
cv2.imwrite("Solar_system_named.jpg",img)