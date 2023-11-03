def maxmin(nums):
    cur_min = None
    cur_max = None

    cur_min = nums[1] if cur_min == None or cur_min > nums[1] else cur_min
    

def nilai_maksimal (list):
  nilai_terbesar = list[0]

  if len(list) > 1:
    # proses rekursif
    next_nilai_terbesar = nilai_maksimal(list[1:])

    if next_nilai_terbesar > nilai_terbesar:
      nilai_terbesar = next_nilai_terbesar

  return nilai_terbesar

print(nilai_maksimal([7,9,12,-2,-22,23]))