import os
PWD = os.getcwd()
FRAMES = os.path.join(PWD, 'frames')
LABELS = os.path.join(PWD, 'labels')
LABELS2 = os.path.join(PWD, 'labels2')
rem_ids = []
with open(LABELS, 'r') as lfile:
    with open(LABELS2, 'w') as lfile2:
        for count, l in enumerate(lfile):
            frame_id = l.split(',')[0]
            if os.path.exists(os.path.join(FRAMES, frame_id + '.jpg')):
                lfile2.write(l)
                if count % 5 == 0: print('{} ... ok'.format(frame_id))
            else:
                rem_ids.append(frame_id)

os.remove(LABELS)
os.rename(LABELS2, LABELS)
print('Dataset:\n'+ '-'*8)
print('frames: {}'.format(count))
print('inconsistent frames: {}'.format(len(rem_ids)))
if rem_ids:
    print('Inconsistent labels were purged.')
