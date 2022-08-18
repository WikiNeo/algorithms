import {describe, it} from "mocha";
import {expect} from "chai";
import LongestRepeatingCharacterReplacement
  from "../../../src/TwoPointers/LongestRepeatingCharacterReplacement/LongestRepeatingCharacterReplacement";

describe("Longest Repeating Character Replacement", () => {

  describe("exec", () => {
    it('should return the correct value with s = AABABBA, k = 1', () => {
      const s: string = "AABABBA"
      const k: number = 1

      const longestRepeatingCharacterReplacement: LongestRepeatingCharacterReplacement = new LongestRepeatingCharacterReplacement(s, k);

      expect(longestRepeatingCharacterReplacement.exec()).equal(4)
    })
  })

  describe('exec2', () => {
    it('should return the correct value with s = AABABBA, k = 1', () => {
      const s: string = "AABABBA"
      const k: number = 1

      const longestRepeatingCharacterReplacement: LongestRepeatingCharacterReplacement = new LongestRepeatingCharacterReplacement(s, k);

      expect(longestRepeatingCharacterReplacement.exec2()).equal(4)
    })
  })
})
