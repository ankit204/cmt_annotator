# cmt_annotator
Simple dataset generation tool built over CMT (online tracking algorithm: https://www.gnebehay.com/cmt/).

To generate a dataset, run it by passing the directory containing .jpg images as command line argument:

`$ python run.py ~/ImageFolder`

The run should generate a `labels` file and a directory `frames`. labels are indexed by unique ids and correspond to the frame present in frames. The other four parameter in the frame indicate x and y co-ordinates of top-left and bottom-right of the bounding box.  
