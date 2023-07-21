from django.shortcuts import render
from candidatereg.models import Candidates
from voter.models import VoterList
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
import cv2
from pyzbar import pyzbar


not_voted=None
@user_passes_test(not_voted)
def voting(request,voter_roll_no):
    candidates=Candidates.objects.all()
    template='voting/voting.html'
    data={'candidates':candidates}
    if request.method=='POST':
        voted_roll_no=request.POST['choice']
        voted_candidate=Candidates.objects.get(roll_no=voted_roll_no)
        voted_candidate.votes+=1
        voted_candidate.save()
        voter=VoterList.objects.get(rno=voter_roll_no)
        voter.voted=True
        voter.save()
    return  render( request,template,data)

def has_voted(request,voter_roll_no):
    not_voted= not VoterList.objects.get(rno=voter_roll_no)
    voting(request,voter_roll_no)
def decode_barcode(frame,request):
    # Find and decode barcodes
    barcodes = pyzbar.decode(frame)

    # Process each barcode found
    for barcode in barcodes:
        # Extract the bounding box location of the barcode
        (x, y, w, h) = barcode.rect

        # Draw a rectangle around the barcode
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Convert barcode data to string format
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        # Print barcode information
        print(barcode_data)
        #print("Barcode Type:", barcode_type)
        has_voted(request,barcode_data)
        return True  # Set flag to True if a barcode is detected

    return False  # Set flag to False if no barcode is detected

def main(request):
    # Initialize the video stream
    video_capture = cv2.VideoCapture(0)

    barcode_detected = False  # Flag to track if barcode is detected

    while True:
        # Read the current frame from the video stream
        ret, frame = video_capture.read()

        # Resize the frame for better processing speed
        frame = cv2.resize(frame, None, fx=0.6, fy=0.6)

        # Convert the frame to grayscale for barcode detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Call the barcode decoding function
        barcode_detected = decode_barcode(gray,request)

        # Display the resulting frame
        cv2.imshow("Barcode Scanner", frame)

        # Exit the loop if barcode is detected and processed
        if barcode_detected:
            break

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video stream and close all windows
    video_capture.release()
    cv2.destroyAllWindows()

def scan(request):
    main(request)



