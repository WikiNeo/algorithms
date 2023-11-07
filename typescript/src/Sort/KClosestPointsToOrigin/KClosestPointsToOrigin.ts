class KClosestPointsToOrigin {
    points: number[][]
    k: number

    constructor(points: number[][], k: number) {
        this.points = points
        this.k = k;
    }

    /**
     * The sort solution complexity is O(NLogN), but it runs faster than priority queue solution in LeetCode
     */
    exec(): number[][]{
        // create map of points to distance
        const pointsToDistance: Map<number[], number> = this.points
            .reduce((acc: Map<number[], number>, cur: number[]) => {
                acc.set(cur, cur[0]*cur[0] + cur[1]*cur[1])
                return acc
            }, new Map<number[], number>())
        return [...pointsToDistance.entries()]
            .sort((a: [number[], number], b: [number[], number]) => a[1] - b[1])
            .slice(0, this.k)
            .map(d => d[0])
    }
}

export default KClosestPointsToOrigin
