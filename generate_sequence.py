import math

def get_sequence():
  pg = int(input())
  sh = math.ceil(pg/8)
  mid = math.floor(pg/2)
  seq = []
  for fp_sh in range(sh):
    seq.append(mid-4*fp_sh)
    seq.append(mid+1+4*fp_sh)
    seq.append(mid-2-4*fp_sh)
    seq.append(mid+3+4*fp_sh)
  for bp_sh in range(sh):
    seq.append(mid+2+4*bp_sh)
    seq.append(mid-1-4*bp_sh)
    seq.append(mid+4+4*bp_sh)
    seq.append(mid-3-4*bp_sh)
  return [0 if x not in range(pg+1) else x for x in seq]

print(get_sequence())
