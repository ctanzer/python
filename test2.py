import matplotlib.pyplot as plt
import numpy as np
data = np.arange(3000).reshape((100,30))
fig = plt.figure()
plt.imshow(data)
# fig.tight_layout()
# plt.savefig('test.png', bbox_inches='tight')
plt.show()
