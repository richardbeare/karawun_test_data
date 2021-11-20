from karawun import save_trackfile
import numpy as np

ll = list()
for i in range(100):
    z=60.0 - i
    lt=np.array([
        [-23.0,-23.0,-65.0],
        [10.0,-50.0, -50.0],
        [z,z, z]], dtype='float32')

    ll.append(lt)

    ll.append(lt + 0.1)
    ll.append(lt - 0.1)

for i in range(100):
    z=60.0 - i
    lt=np.array([
        [50, 46, 21, 10, 38, 14],
        [-55, 10, 10, 0, -15, -50],
        [z, z, z, z, z, z]], dtype='float32')

    ll.append(lt)

    ll.append(lt + 0.1)
    ll.append(lt - 0.1)
    


left={'datatype' : { 'letter' : 'f', 'endian' : '<', 'size': 4},
      'tracks' : ll}
save_trackfile(left, 'letters.tck')

