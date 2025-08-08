xsize = 1280
ysize = 720
with open('data.out', 'wb') as f:
  for y in range(0,ysize):
    for x in range(0,xsize):
      r = 0#int(min(x / (xsize/2 ** 5),2 ** 5 - 1))
      g = 0#int(min(y / (ysize/2 ** 6),2 ** 6 - 1))
      b = 0
      f.write((b).to_bytes(5, byteorder='little'))
      f.write((g).to_bytes(6, byteorder='little'))
      f.write((r).to_bytes(5, byteorder='little'))
      f.write((0).to_bytes(0, byteorder='little'))