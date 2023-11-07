# @param {Integer} n
# @return {Integer}
def climb_stairs(n)
  table = Array.new(n + 1, 0)
  table[0] = 1
  table[1] = 1

  (2..n).each { |i|
    table[i] = table[i - 1] + table[i - 2]
  }

  table[n]
end
