from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2


cap = cv2.VideoCapture(0)



while True:

    ret, frame = cap.read()
    #frame = imutils.resize(frame, width=400)
    # find the barcodes in the image and decode each of the barcodes
    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:

		# extract the bounding box location of the barcode and draw
		# the bounding box surrounding the barcode on the image
		(x, y, w, h) = barcode.rect
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
		# the barcode data is a bytes object so if we want to draw it
		# on our output image we need to convert it to a string first
		barcodeData = barcode.data.decode("utf-8")
		print(barcodeData)
		barcodeType = barcode.type
 
		# draw the barcode data and barcode type on the image
		text = "{} ({})".format(barcodeData, barcodeType)
		cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
 
    cv2.imshow("Barcode Scanner", frame)
    key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
    if key == ord("q"):
	    break
cap.release()
cv2.destroyAllWindows()

