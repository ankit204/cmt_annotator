import os
PWD = os.getcwd()
FRAMES = os.path.join(PWD, 'frames')
LABELS = os.path.join(PWD, 'labels')
LABELS2 = os.path.join(PWD, 'labels2')
rem_ids = []
valid_ids = set([])
with open(LABELS, 'r') as lfile:
    with open(LABELS2, 'w') as lfile2:
        for count, l in enumerate(lfile):
            frame_id, t_x, t_y, b_x, b_y = l.strip().split(',')
            t_x, t_y, b_x, b_y = int(t_x), int(t_y), int(b_x), int(b_y)
            if (all(i > 0 for i in [t_x, t_y, b_x, b_y]) > 0 and os.path.exists(os.path.join(FRAMES, frame_id + '.jpg'))):
                lfile2.write(l)
                valid_ids.add(frame_id)
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

all_frames = set([id_.split('.')[0] for id_ in os.listdir('frames')])
rem_ids = all_frames - valid_ids
for rem_id in rem_ids:
    os.remove(os.path.join(FRAMES, rem_id+'.jpg'))
