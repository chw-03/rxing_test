#!/bin/bash

CAM_PID=""
TEMP_IMG="capture.png"
RUN=true
FRAME=0
SIDE=500

terminate() {
    RUN=false
    # kill cam
    if [ -n "$CAM_PID" ]; then
        kill -0 "$CAM_PID" 2>/dev/null
        wait "$CAM_PID" 2>/dev/null
    fi

    # delete temp files
    rm "$TEMP_IMG" 2>/dev/null
    echo "end proc"
    exit 0
}

trap terminate SIGINT
trap terminate EXIT

echo "start stream w focus"

#run stream
rpicam-hello --timeout 10 --preview 100,100,"$SIDE","$SIDE"  --viewfinder-width "$SIDE" --viewfinder-height "$SIDE" --framerate 1 --verbose 0 &
CAM_PID=$!

while $RUN; do
    sleep 1

    #capture still via screenshot of framebuffer
    fbgrab -d /dev/fb0 "$TEMP_IMG" & 
    wait
    #runs a preview for X time then snaps picture
    #rpicam-still --verbose 0 --width "$SIDE" --height "$SIDE" --encoding png --output "$TEMP_IMG" --timeout 500  --preview 100,100,"$SIDE","$SIDE" --viewfinder-width "$SIDE" --viewfinder-height "$SIDE" &
    
    #no preview, snaps picture instantly
    #rpicam-still --verbose 0 --width "$SIDE" --height "$SIDE" --encoding png --output "$TEMP_IMG" --immediate &
    
    if [[ $? -eq 0 && -f "$TEMP_IMG" ]]; then
        ./rxing_test "$TEMP_IMG" true
    else
        echo "Frame $FRAME: Capture failed"
    fi

    if ! kill -0 $CAM_PID 2>/dev/null; then
        echo "cam died"
        break
    fi

done
terminate
