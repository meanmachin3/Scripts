#!/bin/bash
# Converts a MP4 video to MPEG-2
ffmpeg -i test.mp4 -an -vcodec libx264 -crf 23 test.h264
# Gets MPEG-2 video frame list
ffprobe -selectstreams v -showframes -showentriesframe=picttype -of csv input.h264 > framelist.txt
