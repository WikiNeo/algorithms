# store character to count for first string, then check it with the second
#
# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)
  # base case
  return false if s.length != t.length

  char_to_count = {}

  # store character to count for s
  s.chars.each do |char|
    count = char_to_count.key?(char) ? char_to_count[char] : 0
    char_to_count[char] = count + 1
  end

  # check character to count for t
  t.chars.each do |char|
    count = char_to_count.key?(char) ? char_to_count[char] : 0
    # return false if we can't find the char
    return false if count == 0
    # update the hash
    char_to_count[char] = count - 1
  end

  true
end