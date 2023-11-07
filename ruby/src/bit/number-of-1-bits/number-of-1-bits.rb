# @param {Integer} n, a positive integer
# @return {Integer}
def hamming_weight(n)
  # convert integer to binary representation and count number of 1s
  n.to_s(2).count('1')
end
