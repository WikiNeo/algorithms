import {describe, it} from "mocha";
import {expect} from "chai";
import ThreeSum from "../../../src/TwoPointers/ThreeSum/ThreeSum";

describe("Three Sum", () => {
   describe("exec", () => {
       it('should return the correct value', () => {
           const nums: number[] = [-1,0,1,2,-1,-4]

           const threeSum: ThreeSum = new ThreeSum(nums);

           expect(threeSum.exec()).deep.equal([[-1, -1, 2], [-1, 0, 1]])
       })
   })
})
